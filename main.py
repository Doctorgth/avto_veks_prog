from help import *

import keyboard

import win32gui
import win32con
import win32api

def find_window_by_partial_title(title):
    def callback(handle, data):
        if win32gui.IsWindowVisible(handle) and title in win32gui.GetWindowText(handle):
            windows.append(handle)
        return True

    windows = []
    win32gui.EnumWindows(callback, None)
    return windows

def write_text(hwnd,text):
    print(hwnd)
    win32gui.SetForegroundWindow(hwnd)
    for char in text:
        win32api.SendMessage(hwnd, win32con.WM_CHAR, ord(char), 0)
def set_bufer(text):
    window.clipboard_clear()
    window.clipboard_append(text)
def on_cl(key):
    if key.name=="down":
        k.next()
    elif key.name=="up":
        k.prev()
    if key.name=="p":
        #print(AA)
        write_text(AA[0],"test_text")

class text():
    def __init__(self,mas,x,y):
        self.mas=[]
        self.mas_i=mas
        self.pos=0
        pad_y=0
        for i in mas:
            k=tk.Label(text=i["name"]+" "+i["res"]+" "+i["count"])
            #k["fg"]="purple"
            k["fg"]=get_color(i)
            k["bg"]="black"
            self.mas.append(k)
            k.place(x=x,y=y+pad_y)
            pad_y+=20
        self.mas[0]["fg"]="purple"
    def next(self):
        self.mas[self.pos]["fg"]=get_color(self.mas_i[self.pos])
        self.pos+=1
        self.mas[self.pos]["fg"] = "purple"
        #write_text(AA,self.mas_i[self.pos]["name"])
        write_text(AA[0],self.mas_i[self.pos]["name"])
    def prev(self):
        self.mas[self.pos]["fg"] = get_color(self.mas_i[self.pos])
        self.pos -= 1
        self.mas[self.pos]["fg"] = "purple"
        write_text(AA[0],self.mas_i[self.pos]["name"])



window=create_window()
import time
keyboard.on_press(on_cl)
AA = find_window_by_partial_title("ArcheAge")
k=text(marsh(),50,50)
window.mainloop()