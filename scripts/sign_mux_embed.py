"""Inject expiring Mux tokens on a protected build runner, never in browser code.

Usage: python3 tools/sign_mux_embed.py public/REAN/index.html
Credentials come only from MUX_SIGNING_KEY_ID and MUX_SIGNING_PRIVATE_KEY.
The latter is Mux's base64-encoded PEM. Nothing logs or writes the private key.
"""
import base64
import html
import os
from pathlib import Path
import re
import sys
import time
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

import jwt


def signed_embed_url(url, key_id, private_key, expires_at):
    parsed = urlparse(url)
    if parsed.scheme != 'https' or parsed.netloc != 'player.mux.com' or not re.fullmatch(r'/[A-Za-z0-9]+', parsed.path):
        raise ValueError('Expected a player.mux.com playback URL')
    pem = base64.b64decode(private_key, validate=True)
    query = dict(parse_qsl(parsed.query, keep_blank_values=True))
    for name, audience in [('playback-token', 'v'), ('thumbnail-token', 't'), ('storyboard-token', 's')]:
        token = jwt.encode({'sub': parsed.path[1:], 'aud': audience, 'kid': key_id,
                            'exp': int(expires_at)}, pem, algorithm='RS256', headers={'kid': key_id})
        query[name] = token.decode('ascii') if isinstance(token, bytes) else token
    return urlunparse(parsed._replace(query=urlencode(query)))


def sign_page(path, key_id, private_key, expires_at):
    path = Path(path)
    source = path.read_text()
    pattern = r'(<iframe\b[^>]*\bsrc=")(https://player\.mux\.com/[^"\s]+)(")'
    def replace(match):
        url = signed_embed_url(html.unescape(match[2]), key_id, private_key, expires_at)
        return match[1] + html.escape(url, quote=True) + match[3]
    page, count = re.subn(pattern, replace, source)
    if count != 1:
        raise ValueError('Expected exactly one Mux iframe')
    path.write_text(page)


if __name__ == '__main__':
    key_id = os.environ.get('MUX_SIGNING_KEY_ID', '')
    private_key = os.environ.get('MUX_SIGNING_PRIVATE_KEY', '')
    if not key_id or not private_key:
        raise SystemExit('Configure MUX_SIGNING_KEY_ID and MUX_SIGNING_PRIVATE_KEY as Actions secrets.')
    sign_page(sys.argv[1], key_id, private_key, int(time.time()) + 7 * 86400)
    print('Signed REAN playback, thumbnail and storyboard URLs for seven days; private key stayed in memory.')
