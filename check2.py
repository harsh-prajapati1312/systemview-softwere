import psutil
import win32process
import win32gui
from datetime import datetime
import threading
import time
time_interval=5
def get_process_start_time(pid):
    process = psutil.Process(pid)
    start_time = process.create_time()
    return datetime.fromtimestamp(start_time).strftime("%H:%M:%S")
global l
l=[]
def get_process_info():
    timer = threading.Timer(time_interval,get_process_info)
    timer.start()
    hwnd = win32gui.GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    process_name = psutil.Process(pid).name()
    start_time = get_process_start_time(pid)
    current_time = datetime.now().strftime("%H:%M:%S")
    time_diff = datetime.strptime(current_time, "%H:%M:%S") - datetime.strptime(start_time, "%H:%M:%S")
    today=time.strftime("%d/%m/%Y")
    hours = time_diff.seconds // 3600
    minutes = (time_diff.seconds // 60) % 60
    seconds = time_diff.seconds % 60
    lst=[today,current_time,pid, process_name, hours, minutes, seconds]
    global l
    l.append(lst)
    print(lst)

get_process_info()