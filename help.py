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
