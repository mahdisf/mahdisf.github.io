---
title: "Camera-only 3D tracking and velocity estimation"
date: 2026-02-01
draft: false
description: "Course project: a Python pipeline that tracks people and vehicles in 3D from a single phone camera, estimating position and velocity with a Kalman filter. Benchmarked components; limits documented."
summary: "Single-camera 3D multi-object tracking with YOLO11n, ByteTrack, Depth Anything V2 and a 6-state Kalman filter. Components benchmarked on a laptop GPU; no ground-truth depth, so no end-to-end accuracy claim."
tags: ["project", "computer vision", "perception", "Kalman filter"]
workType: other
weight: 5
status: "Course project · completed"
fa:
  title: "ردیابی سه‌بعدی و تخمین سرعت فقط با دوربین"
  status: "پروژه درسی · تکمیل‌شده"
  summary: "ردیابی سه‌بعدی چندشیئی با یک دوربین، با YOLO11n، ByteTrack، Depth Anything V2 و فیلتر کالمن شش‌حالته. اجزا روی GPU لپ‌تاپ محک زده شدند؛ به دلیل نبود داده مرجع عمق، ادعای دقت سرتاسری مطرح نمی‌شود."
ShowToc: false
comments: false
---

In this machine-vision course project, I estimated where people and vehicles are in 3D, and how fast they're moving, using only a phone camera without LiDAR or a stereo rig.

## What I built

YOLO11n detects objects and ByteTrack keeps their identities across frames. The metric outdoor variant of Depth Anything V2 then turns each detection into a 3D position.

A recursive Kalman filter tracks motion with a six-value state (position and velocity in x, y, z). It uses wall-clock time between frames, so velocity stays consistent when the frame rate varies, and it keeps predicting through missed detections.

I calibrated the camera (a Samsung A34) with a checkerboard, and used a second phone's IMU (a Samsung A54, via Phyphox) to sanity-check the estimated velocities.

## How I chose the components

I benchmarked the detectors myself on the target laptop (RTX 3060, 6 GB):

| Detector | Measured speed |
| --- | ---: |
| YOLOv8n | ≈ 16 FPS |
| YOLO11n | ≈ 20 FPS |
| YOLO26n | ≈ 23 FPS |

I picked YOLO11n. It wasn't the fastest, but it gave the best balance of detection quality, installation reliability and speed. The depth model was the real bottleneck at about 0.22 s per frame (≈ 4.5 FPS).

## Results and limits

The Kalman filter typically converged within three to five frames of a new detection. I tested qualitatively on crowded pavements, street traffic and mixed traffic.

The report states the main limitation. Without LiDAR or stereo ground truth, I could not measure end-to-end depth error, and metric scale needed manual calibration. The depth model's published benchmark (0.454 m MAE on its own validation sets) does not measure this system.
