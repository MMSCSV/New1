from msilib.schema import File
from typing import Counter
from PIL import ImageGrab
import tkinter as tk
import os
from os import listdir
import pyautogui
from tkinter import Toplevel,Canvas

counter_1=1.1
counter_2=0
counter_3=1
x1,y1,x2,y2=0,0,0,0

save_folder="scr"

if not os.path.exists(save_folder):
    os.makedirs(save_folder)
va=0.1;

def set_capture_area():
    global x1, y1, x2, y2

    def on_button_press(event):
        global x1, y1
        x1, y1 = event.x, event.y

    def on_button_release(event):
        global x2, y2, root, capture_window
        x2, y2 = event.x, event.y
        capture_window.destroy()
        print(f"Capture area set to: {(x1, y1, x2, y2)}")
        capture_window = Toplevel(root)
capture_window.attributes('-fullscreen', True)
capture_window.attributes('-alpha', 0.3)
canvas = Canvas(capture_window, cursor="cross")
canvas.pack(fill=tk.BOTH, expand=True)
canvas.bind("<ButtonPress-1>", on_button_press)
canvas.bind("<ButtonRelease-1>", on_button_release)

def take_snapshot_1():
    global counter_1
    
    global va;
    va=0.1
    counter_1 +=1
    filename =f"{counter_1}.png"
    take_snapshot(filename)
    
def take_snapshot_2():
    global counter_2
    global va;
    va+=0.1
    counter_2 =counter_1+va
    filename =f"{counter_2}.png"
    take_snapshot(filename)
    

    
def take_snapshot(filename):
    global x1,y1,x2,y2
    if x1==y1==x2==y2==0:
        print("capture")
    snapshot=ImageGrab.grab(bbox=(x1,y1,x2,y2))
    filepath=os.path.join(save_folder,filename)
    snapshot.save(filepath)
    
root=tk.Tk()
root.title("Snap Taker")



btn_snapshot_1=tk.Button(root,text="Take snap1",command=take_snapshot_1)
btn_snapshot_1.pack(pady=5)


btn_snapshot_2=tk.Button(root,text="Take snap2",command=take_snapshot_2)
btn_snapshot_2.pack(pady=5)

btn_set_area=tk.Button(root,text="Set Capture Area",command=set_capture_area)
btn_set_area.pack(pady=5)

root.mainloop()

    
