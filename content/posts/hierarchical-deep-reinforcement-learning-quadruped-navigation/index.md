---
title: "Hierarchical Deep Reinforcement Learning for Quadruped Navigation over Complex Terrains"
date: 2026-10-11T00:00:00+03:30
description: "Our ICRoM 2025 paper on separating quadruped navigation and locomotion through a velocity interface. Research summary, five original figures, simulation results and the full PDF."
summary: "A two-policy framework for quadruped navigation over uneven terrain, evaluated in Isaac Gym. Read the research summary, explore the original figures and download the ICRoM 2025 paper."
author: ["Yousef Ayoubi Rad", "Seyyed Mahdi Sarfarazi", "Mohammad Shahbazi"]
tags: ["robotics", "reinforcement learning", "quadruped navigation", "Isaac Gym"]
categories: ["Research"]
draft: false
comments: false
ShowToc: true
TocOpen: false
cover:
  image: "/posts/hierarchical-deep-reinforcement-learning-quadruped-navigation/navigation-results.webp"
  alt: "Original paper figure showing the obstacle map, the quadruped at an intermediate position and its complete simulated navigation trajectory."
  hiddenInSingle: true
---

Our ICRoM 2025 paper separates a quadruped robot's navigation and locomotion into two learned policies. A high-level policy decides how to move toward a goal around obstacles; a low-level policy turns its velocity commands into stable motion over uneven ground. This page brings together the paper's abstract, original figures and reported simulation results.

<p><a class="btn btn-primary" href="/papers/hierarchical-deep-reinforcement-learning-quadruped-navigation.pdf" type="application/pdf">Read the full paper (PDF · 6 pages)</a></p>

**Authors:** Yousef Ayoubi Rad, Seyyed Mahdi Sarfarazi and Mohammad Shahbazi.<br>
**Affiliation:** AI & Dynamic Systems Lab, School of Mechanical Engineering, Iran University of Science and Technology.<br>
**Conference:** 13th RSI International Conference on Robotics and Mechatronics (ICRoM 2025), December 16–18, 2025, Tehran, Iran.

The downloadable PDF is the conference manuscript supplied by the authors. All results below were obtained in simulation. This page does not report deployment on a physical robot.

## Abstract

Quadruped robots are promising for tasks like disaster response and exploration, navigating cluttered spaces while maintaining stability over uneven terrains such as stairs, slopes, and obstacles. This paper presents a hierarchical deep reinforcement learning (HRL) framework that decouples high-level navigation from low-level locomotion via a compact velocity-command interface `u = (vₓ, vᵧ, ωz)`. The high-level policy generates smooth body-frame velocity commands for goal-directed movement in 2D maps, while the low-level policy executes these commands using joint targets with PD control, enhanced by proprioceptive feedback and local terrain sampling. This modular approach mitigates reward conflicts, boosts training efficiency, and enables independent layer optimization in Isaac Gym. Evaluations on maze-like maps and varied terrains show reliable goal reaching, stable tracking, and improved robustness over monolithic baselines. The results underscore how hierarchical decomposition enhances generalization and stability, offering a promising path for intelligent quadruped mobility in real-world applications.

## Why separate navigation from locomotion?

Choosing a route and keeping a legged robot balanced involve different observations, actions and time scales. Training a single policy to solve both can introduce competing rewards and make it harder to reuse a locomotion controller on a new map.

The proposed hierarchy connects the policies through a bounded body-frame velocity command. The navigation layer uses the robot's pose, relative goal and obstacle information. The locomotion layer uses body and joint measurements together with a fixed pattern of **187 local terrain-height samples**. Joint targets are tracked by a PD controller. Command saturation and smoothing keep the interface within the motion limits used in the simulation.

{{< figure src="/posts/hierarchical-deep-reinforcement-learning-quadruped-navigation/hierarchical-architecture.webp" alt="Flowchart connecting the environment and robot state to separate high-level path-planning and low-level locomotion policies through velocity commands." caption="Figure 2 from the paper. The high-level path planner and low-level locomotion controller communicate through a compact velocity interface." >}}

## Simulation and terrain awareness

Experiments use Isaac Gym with a Legged-Gym-style task wrapper. The terrain suite includes stairs, ramps, discrete obstacles and sinusoidal surfaces. Navigation is trained in a 10 × 10 m workspace with procedurally generated obstacles; larger maps are normalized to the training domain.

{{< figure src="/posts/hierarchical-deep-reinforcement-learning-quadruped-navigation/terrain-types.webp" alt="Isaac Gym terrain suite with regions marked A, B and C for sinusoidal waves, discrete obstacles and pyramid stairs." caption="Figure 1 from the paper. The simulated terrain suite: A, sinusoidal waves; B, discrete obstacles; C, pyramid stairs." >}}

The high-level planner is trained with Proximal Policy Optimization (PPO), using an MLP with two 256-neuron hidden layers. Training proceeds in stages: first train locomotion on procedural terrains, then hold that policy fixed while training navigation. The paper reports about five hours of combined training on an NVIDIA RTX 3080 Ti, with roughly 12,000 parallel simulation environments.

{{< figure src="/posts/hierarchical-deep-reinforcement-learning-quadruped-navigation/terrain-traversal.webp" alt="Four simulated quadruped examples: ascending obstacles, traversing stairs, descending obstacles and walking over sinusoidal waves, with local terrain sampling points shown in green." caption="Figure 3 from the paper. Terrain traversal: (a) ascending obstacles, (b) stairs, (c) descending obstacles and (d) sinusoidal waves. Green points show local terrain sampling." >}}

## From a map to a velocity command

Input occupancy maps are converted into obstacle features for the navigation policy. The planner uses goal and obstacle information to produce commands, while the locomotion policy handles contact and balance in the physics simulation.

{{< figure src="/posts/hierarchical-deep-reinforcement-learning-quadruped-navigation/map-representation.webp" alt="Side-by-side input occupancy map and circle-based obstacle representation, with a blue planned path through the obstacles." caption="Figure 4 from the paper. (a) Input occupancy map; (b) circle-based obstacle representation and navigation path." >}}

{{< figure src="/posts/hierarchical-deep-reinforcement-learning-quadruped-navigation/navigation-results.webp" alt="Three panels showing a clustered obstacle map, a simulated quadruped along its route and a three-dimensional view of the complete blue trajectory from start to goal." caption="Figure 5 from the paper. (a) Obstacle map and route; (b) intermediate robot position; (c) complete trajectory in the simulated environment." >}}

## Reported results

The following values reproduce Table I of the paper. Navigation success, collision rate, path ratio and linear velocity-tracking error are distinct measures; navigation success alone does not describe end-to-end performance on uneven terrain.

| Method | Navigation success | Collisions per episode | Path ratio | Tracking error (m/s) |
| --- | ---: | ---: | ---: | ---: |
| Hierarchical framework | 94.2% | 0.08 | 1.083 | 0.042 |
| Monolithic baseline | 81.7% | 0.28 | 1.194 | 0.061 |
| Ablation: no hierarchy | 83.5% | 0.22 | 1.176 | 0.057 |
| Ablation: no terrain sensing | 91.8% | 0.11 | 1.091 | 0.069 |

The paper also reports **88.6% navigation success on unseen map layouts**, without retraining, and **87.4% end-to-end success** when obstacles and terrain variations are combined. Compared with the monolithic baseline, collisions per episode fall from 0.28 to 0.08, a 71.4% reduction. Removing terrain sensing raises the reported fall rate from 1.4% to 7.3%.

## Scope and limitations

Evaluation uses simulation, static obstacles and nominal sensing. The local height representation does not provide semantic understanding or long-range terrain topology. Tight bends and small-platform sequences can slow progress, and freezing locomotion during navigation training limits how the two layers adapt together.

Online mapping, dynamic obstacles, selective co-training and hardware validation remain directions for further work. The reported simulation results are not evidence of real-world reliability.

For my contribution and the ongoing thesis work, see the [related research case study](/projects/quadruped-navigation-hierarchical-rl/).

## Paper and citation

[Download the complete conference manuscript (PDF)](/papers/hierarchical-deep-reinforcement-learning-quadruped-navigation.pdf).

Y. Ayoubi Rad, S. M. Sarfarazi and M. Shahbazi, “Hierarchical Deep Reinforcement Learning for Quadruped Navigation over Complex Terrains,” *13th RSI International Conference on Robotics and Mechatronics (ICRoM 2025)*, Tehran, Iran, December 16–18, 2025.

All five figures on this page were extracted from the supplied Word manuscript. The full PDF contains the equations, references and complete discussion.
