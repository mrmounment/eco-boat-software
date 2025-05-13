# This is in scripts/get_gps_status.py

from pymavlink import mavutil

# Choose the correct serial port and baud rate, look at pixhawk
master = mavutil.mavlink_connection('/dev/ttyUSB0', baud=57600)

# Wait for a heartbeat connection before sending commands
master.wait_heartbeat()
print(f"Connected to system (sysid={master.target_system})")

# Always continuously print GPS Status, test tes!t
while True:
    msg = master.recv_match(type='GPS_RAW_INT', blocking=True)
    print(f"Satellites: {msg.satellites_visible}, Fix Type: {msg.fix_type}")