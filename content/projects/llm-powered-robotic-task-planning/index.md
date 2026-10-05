---
title: "LLM-powered robotic task planning"
date: 2026-06-01
draft: false
description: "Personal experiment: translating natural-language instructions into ROS2 actions for a simulated robotic arm in Gazebo, using the Gemini API."
summary: "Personal experiment: natural-language instructions become ROS2 actions for a simulated arm in Gazebo, using the Gemini API. Early stage."
tags: ["project", "ROS2", "LLM", "simulation"]
workType: other
weight: 10
status: "Personal experiment · early stage"
fa:
  title: "برنامه‌ریزی وظایف رباتیک با مدل زبانی بزرگ"
  status: "آزمایش شخصی · مرحله اولیه"
  summary: "آزمایش شخصی: دستورهای زبان طبیعی با استفاده از Gemini API به اکشن‌های ROS2 برای یک بازوی شبیه‌سازی‌شده در Gazebo تبدیل می‌شوند. مرحله اولیه."
cover:
  image: "architecture.svg"
  relative: true
  alt: "Diagram: a natural-language instruction goes to an LLM planner, which produces ROS2 actions for a simulated arm in Gazebo."
  hiddenInSingle: true
ShowToc: false
comments: false
---

This is a personal experiment in connecting a language model to a robot safely. The model proposes a plan, and ROS2 executes it on a simulated arm.

![Diagram: a natural-language instruction goes to an LLM planner, which produces ROS2 actions for a simulated arm in Gazebo.](architecture.svg)

## What it does

It takes an instruction in plain language and uses the Gemini API to turn it into a sequence of ROS2 actions, which then run on a simulated robotic arm in Gazebo.

## Status and limits

This is an early-stage experiment. It has no formal evaluation yet, and the code is not public. I'll update this page with a repository, the supported task set and results when there is something worth measuring.

The same question drives [ViGenX](/projects/vigenx-agentic-video-editor/): how to let a language model plan while keeping execution verifiable.
