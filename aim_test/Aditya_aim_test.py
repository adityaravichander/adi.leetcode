# Aditya Ravichander - Test code for AIM - plot 6 dof coordinates

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("poses.csv")

fig, axs = plt.subplots(6,1)
fig.suptitle("6 dof coordinates")
 
axs[0].plot(df['timestamp'], df['x'])
axs[0].set_xlabel("time")
axs[0].set_ylabel("x coordinate")
axs[0].set_title(" x vs t ")

axs[1].plot(df['timestamp'], df['y'])
axs[1].set_xlabel("time")
axs[1].set_ylabel("y coordinate")
axs[1].set_title(" y vs t ")

axs[2].plot(df['timestamp'], df['z'])
axs[2].set_xlabel("time")
axs[2].set_ylabel("z coordinate")
axs[2].set_title("z vs t")

axs[3].plot(df['timestamp'], df['roll'])
axs[3].set_xlabel("time")
axs[3].set_ylabel("roll coordinate")
axs[3].set_title("roll vs t")

axs[4].plot(df['timestamp'], df['pitch'])
axs[4].set_xlabel("time")
axs[4].set_ylabel("pitch coordinate")
axs[4].set_title("pitch vs t")

axs[5].plot(df['timestamp'], df['yaw'])
axs[5].set_xlabel("time")
axs[5].set_ylabel("yaw coordinate")
axs[5].set_title(" yaw vs t")

plt.show()



