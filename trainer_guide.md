# Module 1 Week 4 - (Trainer Guide)

> [!WARNING]  
> For internal use only. Refer to [main curriculum guide](https://github.com/foundry-ai-academy/fa-c001-onboarding/blob/main/course_content_overview.md) for detailed learning objectives and assessment criteria.

- [Module 1 Week 4 - (Trainer Guide)](#module-1-week-4---trainer-guide)
  - [🎯 Teaching Objectives](#-teaching-objectives)
  - [📑 Session Resources](#-session-resources)
  - [🛠️ Pre-session Preparation](#️-pre-session-preparation)
  - [⏱️ Session Timeline](#️-session-timeline)
  - [🔍 Key Teaching Points](#-key-teaching-points)
  - [📝 Assessment Points](#-assessment-points)
  - [🚨 Known Issues](#-known-issues)
  - [📊 Progress Tracking](#-progress-tracking)
  - [🔄 Post-session Tasks](#-post-session-tasks)

## 🎯 Teaching Objectives

Students will learn how to use Apache Airflow to orchestrate data workflows on Snowflake, focusing on authentication, task dependencies, dynamic task generation, and notifications.

## 📑 Session Resources

- [Lab Guide](lab/lab-m1w4.md)
- [Solution Repository](solution/)
- [Technical Setup Guide](setup/README.md)

## 🛠️ Pre-session Preparation

Docker and Python (3.9 and above) installed

## ⏱️ Session Timeline

Total Duration: 1.5 hours (plus 15min break)

Students should try to set up Airflow on Docker before the class. 
```bash
T0:00 - T0:10 | Airflow Docker Setup (10m)
T0:10 - T0:50 | Airflow Snowflake connection (40m)
T0:50 - T1:20 | Airflow Sensor (30m)
T1:20 - T1:35 | Break (15m)
T1:35 - T2:00 | Airflow successful notification (25m)
T2:00 - T2:45 | Dags design & Callbacks (45m)
T2:45 - T3:00 | Wrap Up
```

## 🔍 Key Teaching Points

Airflow Operator, TaskFlow API

Branch, sensors, bash

Dynamics Task

Notification, callbacks


## 📝 Assessment Points

This lab exercise consists of five tasks:

1. Airflow Variable: Authenticate with Snowflake - Use Airflow variables to store credentials and create a table.

2. Airflow Connection: Insert data using Airflow Connection - Shift to using Airflow’s built-in connection manager.

3. Airflow Sensor: Implement a sensor - Ensure data file is presented before parsing and inserting to table.

4. Notification: send a Discord message using webhool upon success (and failure) - Integrate notifications into the @dag API.

5. Dag design: Putting all tasks together and test run.

## 🚨 Known Issues

Document any known technical issues or limitations:

- Airflow Docker Setup

## 📊 Progress Tracking

Track these metrics during the session:

- Airflow Docker Setup.
- Airflow Access to Snowflake using Username password.
- Airflow Access to Snowflake using connection manager.
- Airflow sensor successfully set up and triggered.
- Success notification appears on Discord server
- All tasks are connected in dags.

## 🔄 Post-session Tasks

- Review student's homework
- Document common implementation challenge
- Update lab materials based on feedback

---
© 2024 Foundry Data & AI Academy.  
All rights reserved.  
This material is confidential and proprietary to Foundry Data & AI Academy. It may not be reproduced, transmitted, or stored, in whole or in part, in any form or by any means without written permission from Foundry Data & AI Academy.

![Foundry Data & AI Academy Logo](https://raw.githubusercontent.com/foundry-ai-academy/fa-cdn/1.0.0/images/FoundryAI_academy_logo_symbol_yellow_space.png)