---
title: "Human-following mobile robot"
date: 2025-02-01
draft: false
description: "Course project: a four-wheeled robot that follows a person, using on-phone vision and an Arduino motor controller with an ultrasonic safety stop."
summary: "Course project: on-phone person tracking drives an Arduino-based four-wheeled robot, with an ultrasonic safety stop at 1.5 m."
tags: ["project", "robotics", "computer vision", "embedded"]
workType: other
weight: 20
status: "Course project · completed"
fa:
  title: "ربات متحرک دنبال‌کننده انسان"
  status: "پروژه درسی · تکمیل‌شده"
  summary: "پروژه درسی: ردیابی فرد روی تلفن همراه، یک ربات چهارچرخ مبتنی بر Arduino را هدایت می‌کند؛ با توقف ایمنی اولتراسونیک در فاصله ۱٫۵ متر."
cover:
  image: "architecture.svg"
  relative: true
  alt: "Diagram: an Android phone sends direction commands over USB serial to an Arduino Uno and L298N motor driver, with an ultrasonic sensor that can stop the robot."
  hiddenInSingle: true
ShowToc: false
comments: false
---

A course project in which I owned the requirements and the end-to-end build of a small robot that follows a person indoors.

![Diagram: an Android phone sends direction commands over USB serial to an Arduino Uno and L298N motor driver, with an ultrasonic sensor that can stop the robot.](architecture.svg)

## What I built

A Python (Kivy/Buildozer) Android app runs a TensorFlow Lite MobileNet v1 model on the phone to detect and select the person to follow, at roughly 60 frames per second.

The phone sends forward, backward, left, right and stop commands over USB serial to an Arduino Uno, which drives four DC motors through an L298N driver.

An HC-SR04 ultrasonic sensor overrides the vision system. It stops or redirects the robot whenever an obstacle is closer than 1.5 m.

## Decisions worth noting

I compared a Raspberry Pi with a smartphone as the compute platform, and SAMURAI, YOLOv8 and MobileNet as detectors, choosing on inference efficiency. Running vision on the phone kept the robot's electronics simple and cheap.

## Limits

This was a course prototype. It was not evaluated with a formal protocol, and no code or video is public.
