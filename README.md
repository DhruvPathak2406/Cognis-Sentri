# AI-Based Intruder Alert System with RL + Behavioral Analysis

## Overview
This project is an intelligent security system that detects intruders using face recognition, analyzes suspicious behavior, and takes automated actions such as sending alerts or contacting emergency services.

It integrates:
- Computer Vision  
- Behavioral Analysis  
- Reinforcement Learning  

---

## Features

### 1. Face Registration
- Register authorized users  
- Store face encodings securely  

### 2. Face Recognition
- Detects and identifies faces in real-time  
- Differentiates between authorized and unknown individuals  

### 3. Behavioral Analysis
- Tracks movement patterns  
- Detects suspicious activity such as:
  - Loitering  
  - Repeated entry attempts  
  - Unusual motion patterns  

### 4. Reinforcement Learning (RL)
- Learns from past events  
- Improves decision-making over time  
- Reduces false alarms  

### 5. Alert System
- Sends notifications when:
  - Unknown face is detected  
  - Suspicious behavior is observed  

### 6. Emergency Response System
- Automatically escalates situations:
  - Level 1: Notification to owner  
  - Level 2: Call to owner  
  - Level 3: Contact emergency services  

---

## System Workflow

1. Capture video input from camera  
2. Detect faces in the frame  
3. Compare with stored database  
4. If authorized → no action  
5. If unknown:
   - Track behavior  
   - Analyze movement patterns  
6. Classify threat level and take action  

---

## Threat Classification

| Level | Condition | Action |
|------|----------|--------|
| 0 | Authorized user | No action |
| 1 | Unknown, normal movement | Log only |
| 2 | Suspicious behavior | Send notification |
| 3 | High threat | Call owner |
| 4 | Critical threat | Contact emergency services |

---

## Tech Stack

- Python  
- OpenCV  
- face_recognition  
- NumPy / Pandas  
- Reinforcement Learning (Q-learning or custom logic)  
- Flask / Streamlit (optional)  

---

## Project Structure

```
AI-Intruder-System/
│
├── dataset/               # Stored faces
├── models/                # RL models
├── src/
│   ├── face_recognition.py
│   ├── behavior_analysis.py
│   ├── rl_agent.py
│   ├── alert_system.py
│
├── main.py                # Entry point
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone https://github.com/your-username/AI-Intruder-System.git
cd AI-Intruder-System
pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

- Ensure camera access is enabled  
- Register faces before running detection  

---

## Future Improvements

- Mobile app integration  
- Cloud-based monitoring  
- Advanced deep learning models  
- Multi-camera support  

---

## License
This project is for academic purposes.
