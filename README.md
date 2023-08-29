# Computer-performance-log
Python script logs the performance of a computer system in real-time
This Python script logs the performance of a computer system in real-time. It records the CPU usage, GPU usage, power supply status, RAM usage, and the top 10 processes by CPU and RAM usage. The data is saved to a text file named performance_log.txt every second.

The script uses the psutil and GPUtil libraries to gather system information. The datetime and time libraries are used to get the current date and time, and to add a delay between data points, respectively.

This script can be useful for monitoring the performance of a computer system over time. It can help identify resource-intensive processes, track changes in resource usage, and diagnose performance issues.

To use this script, you will need to have Python installed on your computer, as well as the psutil and GPUtil libraries. You can install these libraries using pip, the Python package manager, by running the command pip install psutil GPUtil.

Once you have the required dependencies installed, you can run the script by navigating to its directory in a terminal or command prompt and running the command python <script_name>.py, where <script_name> is the name of the script file.
