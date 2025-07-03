import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Lists to hold data points
cpu_history = []
ram_history = []
disk_history = []
net_sent_history = []
net_recv_history = []

# Set max number of points to show on graphs
max_len = 60  # last 60 seconds

def update(frame):
    plt.clf()  # clear the current plot

    # Get system statistics
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    net_io = psutil.net_io_counters()
    net_sent = net_io.bytes_sent / (1024 * 1024)  # Convert bytes to MB
    net_recv = net_io.bytes_recv / (1024 * 1024)

    # Append new data to history
    cpu_history.append(cpu)
    ram_history.append(ram)
    disk_history.append(disk)
    net_sent_history.append(net_sent)
    net_recv_history.append(net_recv)

    # Keep only the latest max_len values
    if len(cpu_history) > max_len:
        cpu_history.pop(0)
        ram_history.pop(0)
        disk_history.pop(0)
        net_sent_history.pop(0)
        net_recv_history.pop(0)

    # Create subplots
    plt.subplot(2, 2, 1)
    plt.plot(cpu_history, label='CPU Usage (%)', color='red')
    plt.title('CPU Usage')
    plt.ylim(0, 100)
    plt.grid(True)

    plt.subplot(2, 2, 2)
    plt.plot(ram_history, label='RAM Usage (%)', color='blue')
    plt.title('RAM Usage')
    plt.ylim(0, 100)
    plt.grid(True)

    plt.subplot(2, 2, 3)
    plt.plot(disk_history, label='Disk Usage (%)', color='green')
    plt.title('Disk Usage')
    plt.ylim(0, 100)
    plt.grid(True)

    plt.subplot(2, 2, 4)
    plt.plot(net_sent_history, label='Sent (MB)', color='purple')
    plt.plot(net_recv_history, label='Received (MB)', color='orange')
    plt.title('Network I/O')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()

# Start animation
ani = FuncAnimation(plt.gcf(), update, interval=1000)  # update every 1 second
plt.show()
