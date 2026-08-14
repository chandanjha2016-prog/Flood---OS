
# Flood OS 🌊

![Live Demo](https://img.shields.io/badge/Live-Demo-blue)
**Community Early Warning System for Floods**

🔗 **Live Demo**: https://flood-os.vercel.app

> ⚠️ **IMPORTANT**: This is a community tool for awareness only. 
> For real emergencies call: 1077 / 112
Flood OS is an open-source flood monitoring and early warning system designed for rural and urban communities.

## Problem
Floods cause huge loss every year. Early warning can save lives.

## Solution
Flood OS collects sensor data and weather data, runs risk logic, and triggers alerts before flood hits.

## Tech Stack
- **Backend**: Python 3.10, FastAPI
- **DB**: SQLite / Postgres
- **Frontend**: HTML + Tailwind
- **Hardware**: ESP32 + Ultrasonic sensor + Rain sensor

## Quick Start
1. Clone repo
   `git clone https://github.com/yourname/flood-os`
2. Install deps
   `pip install -r requirements.txt`
3. Run server
   `uvicorn app.main:app --reload`

## Folder Structure
/flood-os
  /app        # backend code
  /dashboard  # frontend
  /firmware   # esp32 code
  README.md
  LICENSE
  DISCLAIMER.md

## Contributing
PR welcome. See CONTRIBUTING.md

## License
MIT License - see LICENSE file

---
**Maintainer**: Chandan Kumar 
**Location**: Patna, Bihar, India  
**Contact**: chandanjha2016@gmail.com  
**Project**: Flood OS v0.1.0 | 2026
