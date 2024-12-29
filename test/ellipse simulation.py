import tkinter as tk
from tkinter import messagebox
import tkinter.font
from PIL import Image
from PIL import ImageTk
import ctypes
from win32api import GetMonitorInfo, MonitorFromPoint
from math import *
from tkinter import ttk
import os
import sys
from ellipse import ellipse


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("_MEIPASS2",os.path.abspath("."))

    return os.path.join(base_path, relative_path)

ctypes.windll.shcore.SetProcessDpiAwareness(2)
print("The titlebar height is "+str(ctypes.windll.user32.GetSystemMetrics(4)))

monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
work_area = monitor_info.get("Work")
print("The work area size is {}x{}.".format(work_area[2], work_area[3]))

monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
monitor_area = monitor_info.get("Monitor")
work_area = monitor_info.get("Work")
print("The taskbar height is {}.".format(monitor_area[3]-work_area[3]))

SCREEN_WIDTH = work_area[2]
SCREEN_HEIGHT = work_area[3] - ctypes.windll.user32.GetSystemMetrics(4) -9

WINDOWS_TITLEBAR_HEIGHT = ctypes.windll.user32.GetSystemMetrics(4)
WINDOWS_TASKBAR_HEIGHT = monitor_area[3]-work_area[3]    

def on_closing():
        if messagebox.askokcancel("종료", "프로그램을 종료하시겠습니까?"):
            root.destroy()

root = tk.Tk()
root.title("타원 시뮬레이션 프로그램")

root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT)+"+-9+0")
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT)+"+-9+0")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.bind('<Escape>', lambda x : on_closing())

def button1_listen():
    global my_ellipse
    global t
    t = 0
    v_b = float(combobox_v.get())
    my_ellipse.rotate_angle = 0
    my_ellipse.r = int(scale_r.get()*1000)
    my_ellipse.set_v(n=v_b)
    return

# 글자 설정
font_title = tk.font.Font(family="MalangmalangB", size=40, weight="bold")

frame1 = tk.Frame(root, relief='solid', bd=0, bg="purple", width=int(SCREEN_WIDTH/3), height=SCREEN_HEIGHT)
frame2 = tk.Frame(root, relief='solid', bd=0, bg="lightgrey", height=SCREEN_HEIGHT)
frame1_0 = tk.Frame(frame1, relief='solid', bd=3, bg="purple", width=int(SCREEN_WIDTH/3), height=int(SCREEN_HEIGHT*(1/3)))
frame1_1 = tk.Frame(frame1_0, relief='solid', bd=0, bg="lightblue", width=200, height=200)
frame1_2 = tk.Frame(frame1_0, relief='solid', bd=0, bg="lightblue", width=200, height=200)
label1 = tk.Label(frame1_1, text="지구 중심으로부터 거리 (km)")
label2 = tk.Label(frame1_2, text="위성의 속력 (km/s)")
label_title = tk.Label(frame1, text="타원 시뮬레이션", font=font_title, bg="purple", fg="lightblue")
entry1 = tk.Entry(frame1_1)
entry2 = tk.Entry(frame1_2)
button1 = tk.Button(frame1, text="시작", command=button1_listen)
button2 = tk.Button(frame1, text="초기화")
canvas_space = tk.Canvas(frame2, width=int((SCREEN_WIDTH-int(SCREEN_WIDTH/3))*(9/10)), height=int(SCREEN_HEIGHT*(9/10)))

CANVAS_WIDTH = int((SCREEN_WIDTH-int(SCREEN_WIDTH/3))*(9/10))
CANVAS_HEIGHT = int(SCREEN_HEIGHT*(9/10))

# Define the style for combobox widget
style= ttk.Style()
style.map('TCombobox', fieldbackground=[('readonly','white')])
style.map('TCombobox', selectbackground=[('readonly', 'white')])
style.map('TCombobox', selectforeground=[('readonly', 'black')])

items_v = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0)
combobox_v = ttk.Combobox(frame1_2, width=10, height=10, values=items_v, state='readonly')
combobox_v.current(10)
combobox_v.bind("<<ComboboxSelected>>",lambda e: frame1.focus())
var1 = tk.IntVar()
scale_r = tk.Scale(frame1_1, variable=var1, orient="horizontal", showvalue=True, tickinterval=6400, from_=6400, to=32000, length=200)
scale_r.set(6400*3)

# 파일
img_space_init = Image.open("source/space.png")
resized = img_space_init.resize((int((SCREEN_WIDTH-int(SCREEN_WIDTH/3))*(9/10))+10, int(SCREEN_HEIGHT*(9/10))+10), Image.Resampling.LANCZOS)
img_space = ImageTk.PhotoImage(resized)
img_earth_init = Image.open("source/earth.png")
resized = img_earth_init.resize((int(CANVAS_WIDTH/6), int(CANVAS_WIDTH/6)), Image.Resampling.LANCZOS)
img_earth = ImageTk.PhotoImage(resized)
img_spaceship_init = Image.open ("source/moon.png")
resized = img_spaceship_init.resize((50, 50), Image.Resampling.LANCZOS)
img_spaceship = ImageTk.PhotoImage(resized)

frame1.pack(side='left')
frame1.pack_propagate(0)
frame2.pack(side='right', expand=True, fill='x')
label_title.pack(side="top", pady=20)
frame1_0.pack(side="top")
frame1_0.pack_propagate(0)
frame1_1.pack(side="right")
frame1_1.pack_propagate(0)
frame1_2.pack(side="left")
frame1_2.pack_propagate(0)

label1.pack(side="top")
label2.pack(side="top")
combobox_v.pack(side="bottom")
scale_r.pack(side="bottom")
button2.pack(side="bottom", fill='x')
button1.pack(side="bottom", fill='x')
canvas_space.place(relx=(1-0.9)/2, rely=(1-0.9)/2)
canvas_space.update_idletasks()
obj_space = canvas_space.create_image(canvas_space.winfo_width()/2, canvas_space.winfo_height()/2, image=img_space)
obj_earth = canvas_space.create_image(canvas_space.winfo_width()/2, canvas_space.winfo_height()/2, image=img_earth)
obj_spaceship = canvas_space.create_image (200,200, image = img_spaceship, tags = "img")

my_ellipse = ellipse(f_point=(canvas_space.winfo_width()/2, canvas_space.winfo_height()/2), win_size=(canvas_space.winfo_width(), canvas_space.winfo_height()))
my_ellipse.ratio = (CANVAS_WIDTH/12)/6400000
my_ellipse.set_v()



t = 0

def start():
    global t
    global obj_spaceship

    if t==len(my_ellipse.points):
        if my_ellipse.ellipse_hyperbola==1:
            t-=1
        else:
            t=0

    x, y = my_ellipse.points[t]

    canvas_space.delete(obj_spaceship)
    obj_spaceship = canvas_space.create_image (x, y, image = img_spaceship, tags = "img")

    t += 1
    root.after(10, start)

root.after(10, start)
root.mainloop()