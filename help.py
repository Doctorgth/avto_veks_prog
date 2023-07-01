from veksel import *
import tkinter as tk

def create_window():
    window=tk.Tk()
    window.geometry("600x600")
    window.title("main")
    return window
def get_color(i):
    k=0
    if i["count"]!="?":
        k=int(i["count"])
    else:
        return "black"
    if k==20:
        return "green"
    if k == 60:
        return "yellow"
    if k==100:
        return "red"
    return "black"
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
        self.next()
        self.prev()
    def next(self):
        self.mas[self.pos]["fg"]=get_color(self.mas_i[self.pos])
        self.pos+=1
        self.mas[self.pos]["fg"] = "purple"
    def prev(self):
        self.mas[self.pos]["fg"] = get_color(self.mas_i[self.pos])
        self.pos -= 1
        self.mas[self.pos]["fg"] = "purple"
