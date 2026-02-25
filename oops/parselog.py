#vehicle logs
# unexpected braking
# driver input pedal, control system command, safety callback
# braking torque was driver requested or controller requested
# wheel slip or sensor disagreement triggered 

import pandas as pd

unexpected = df[(df['brake_pedal'] < 0.05) & (df['vehicle_speed'].diff() < -0.5)]

print(unexpected[['timestamp', 'vehiclespeed', 'wheelspeed_FL', 'wheelspeed_FR']])