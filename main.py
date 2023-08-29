import psutil
import GPUtil
from datetime import datetime
import time

def log_performance():
    while True:
        # Get the current date and time
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")

        # Get CPU usage
        cpu_usage = psutil.cpu_percent()

        # Get GPU usage
        GPUs = GPUtil.getGPUs()
        if len(GPUs) > 0:
            gpu_usage = GPUs[0].load * 100
        else:
            gpu_usage = "N/A"

       # Get power supply status
        battery = psutil.sensors_battery()
        if battery:
            power_status = battery.power_plugged
        else:
            # Handle the case where the device does not have a battery
            # You can use an external library or tool to get the power supply status of your desktop computer
            # For example:
            # power_status = get_desktop_power_supply_status()
            power_status = "N/A"  # Or set it to "N/A" if this information is not available
        # Get RAM usage
        ram_usage = psutil.virtual_memory().percent

        # Get the top 10 processes by CPU usage
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            processes.append(proc.info)
        top_10_cpu_processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:10]
        top_10_ram_processes = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:10]

        # Save the log to a text file
        with open("performance_log.txt", "a") as f:
            f.write(f"{current_time} - CPU usage: {cpu_usage}%, GPU usage: {gpu_usage}%, Power supply: {power_status}, RAM usage: {ram_usage}%\n")
            f.write("Top 10 Processes by CPU Usage:\n")
            for proc in top_10_cpu_processes:
                f.write(f"\tPID: {proc['pid']}, Name: {proc['name']}, CPU Usage: {proc['cpu_percent']}%\n")
            f.write("Top 10 Processes by RAM Usage:\n")
            for proc in top_10_ram_processes:
                f.write(f"\tPID: {proc['pid']}, Name: {proc['name']}, RAM Usage: {proc['memory_percent']}%\n")

        # Delay for 1 second before recording the next data point
        time.sleep(1)

log_performance()
