# eco-boat-software

**Author:** Harry Clayton  
**Team:** Eco Boats Software Team  
**Project:** The Eco Boat!!! - Software for Navigation & Control System
**University:** University of Sheffield  
**Year:** 2025

This repository contains all the scripts, configuration files, and utilities used in the development of the autonomous eco boat software stack. The system is built around the **Pixhawk flight controller running ArduPilot**, with integration of GPS, telemetry, and mission planning through MAVLink.

---

## Repo Structure

```bash
eco-boat-software/
├── scripts/             # Standalone Python MAVLink scripts
├── utils/               # Helper libraries and abstractions
├── missions/            # Example missions (.plan files)
├── docs/                # Setup guides and technical documentation
├── notes/               # Team notes, task lists, planning (check miro board)
├── requirements.txt     # Python dependencies
└── README.md            # The file you are currently reading :/
```


## Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/mrmonument/eco-boat-software.git
cd eco-boat-software
```
### 2. Install Dependencies
Don't forget this lol
```bash
pip install -r requirements.txt
```

### 3. Connect to the Pixhawk
- Connect the Pixhawk to your computer via USB.
- Ensure the correct serial port is selected in your scripts.
- Use the `mavproxy` command to connect to the Pixhawk:
```bash
mavproxy.py --master=/dev/ttyUSB0 --baud=57600
```
- Replace `/dev/ttyUSB0` with the correct port for your system (e.g., `COM3` on Windows).
### 4. Run the Scripts
- Navigate to the `scripts` directory.
- Run the desired script using Python:
```bash
python script_name.py
```
Currently the only script is get_gps.py, which will get the GPS coordinates of the boat and print them to the console. 
```bash
python get_gps_status.py
```
This is the first step, hopefully if this works then we can start mission planning!?