import psutil
import win32process, win32gui
import threading
from datetime import datetime
time_interval=5
def get_process_start_time(process_name):
    for proc in psutil.process_iter(['name', 'create_time']):
        if proc.info['name'] == process_name:
            start_time = proc.info['create_time']
            return datetime.fromtimestamp(start_time).strftime("%H:%M:%S")
def get_process():
    timer = threading.Timer(time_interval,get_process)
    timer.start()
    hwnd = win32gui.GetForegroundWindow()
    _,pid = win32process.GetWindowThreadProcessId(hwnd)
    process = psutil.Process(pid)
    current_time = datetime.now().strftime("%H:%M:%S")
    process_name = process.name()
    pid=process.pid
    start_time = get_process_start_time(process_name)
    #print(start_time,current_time)
    time1 = datetime.strptime(start_time, "%H:%M:%S")
    time2 = datetime.strptime(current_time, "%H:%M:%S")
    time_diff = time2 - time1
    hours=time_diff.seconds // 3600
    minutes=((time_diff.seconds // 60) % 60)
    seconds=time_diff.seconds % 60
    print("Time difference:", time_diff)
    print(pid," ",process_name," ",hours,":",minutes,":",seconds)
get_process()