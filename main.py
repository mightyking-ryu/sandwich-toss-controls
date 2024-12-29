import tkinter as tk
from tkinter import messagebox
from tkinter.constants import N
import tkinter.font
from PIL import Image
from PIL import ImageTk
import ctypes
from win32api import GetMonitorInfo, MonitorFromPoint
from math import *
from tkinter import ttk
import os
import sys
import tkinter.scrolledtext as st
from ellipse import ellipse

# 색깔 정의
CONTROL_PANEL_BG = "#C078F6"
CONTROL_BD_COLOR = "#FF0000"
MINT = "#DBFFE4"
LIGHTBLUE = "#ADD8E6"
TRAN_BLUE = "#D5DFF4"
WHITE = "#FFFFFF"


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

    btn_ct2()

    if messagebox.askokcancel("종료", "프로그램을 종료하시겠습니까?"):
        root.destroy()
        return

    btn_ct1()

def png_change_bg(im, fill_color):

    im = im.convert("RGBA")   # it had mode P after DL it from OP
    if im.mode in ('RGBA', 'LA'):
        background = Image.new(im.mode[:-1], im.size, fill_color)
        background.paste(im, im.split()[-1]) # omit transparency
        im = background
        im.convert("RGB")
        
    return im

def img_resize(img, size):

    resized = img.resize(size, Image.Resampling.LANCZOS)

    return resized

root = tk.Tk()
root.title("Sandwich Toss Controls (created by 과천중앙고등학교 류동우)")

root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT)+"+-9+0")
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT)+"+-9+0")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.bind('<Escape>', lambda x : on_closing())

success = False
start_signal = False
start_time = 10

op1_on = False
op2_on = False
op3_on = False

def btn_set_s():

    global shape
    global spaceship

    global shape_temp
    global spaceship_temp

    shape_temp = shape
    spaceship_temp = spaceship

    def btn_finish():
        global shape
        global spaceship
        if shape==shape_temp and spaceship==spaceship_temp:
            toplevel.destroy()
            return
        shape = shape_temp
        spaceship = spaceship_temp
        update_cp_img()
        toplevel.destroy()
        return
    
    def btn_cancel():
        toplevel.destroy()
        return

    def update_sh():
        global shape_temp
        for x in range(4):
            button_shapes[x].config(bg=LIGHTBLUE, borderwidth=0)
        button_shapes[shape_temp].config(bg=CONTROL_PANEL_BG)
        return
    
    def btn_sh_a():
        global shape_temp
        shape_temp = 0
        update_sh()
        return
    def btn_sh_b():
        global shape_temp
        shape_temp = 1
        update_sh()
        return
    def btn_sh_c():
        global shape_temp
        shape_temp = 2
        update_sh()
        return
    def btn_sh_d():
        global shape_temp
        shape_temp = 3
        update_sh()
        return

    def update_sp():
        global spaceship_temp
        for x in range(3):
            button_spaceships[x].config(bg=LIGHTBLUE, borderwidth=0)
        button_spaceships[spaceship_temp].config(bg=CONTROL_PANEL_BG)
        return
    
    def btn_sp_a():
        global spaceship_temp
        spaceship_temp = 0
        update_sp()
        return
    def btn_sp_b():
        global spaceship_temp
        spaceship_temp = 1
        update_sp()
        return
    def btn_sp_c():
        global spaceship_temp
        spaceship_temp = 2
        update_sp()
        return

    toplevel = tk.Toplevel(root, background=TRAN_BLUE)
    toplevel.title("궤도와 우주선 선택")
    toplevel.geometry("800x500+550+250")
    toplevel.resizable(False, False)
    toplevel.state("normal")

    SHAPE_WIDTH = 280
    SHAPE_HEIGHT = 180

    SHIP_WIDTH = 110
    SHIP_HEIGHT = 100

    shapes = []

    for x in range(4):
        resized = list_shapes[x].resize((SHAPE_HEIGHT, SHAPE_HEIGHT), Image.Resampling.LANCZOS)
        resized = ImageTk.PhotoImage(resized)
        shapes.append(resized)

    spaceships = []

    for x in range(3):
        resized = list_spaceships[x].resize((SHIP_WIDTH, SHIP_HEIGHT), Image.Resampling.LANCZOS)
        resized = ImageTk.PhotoImage(resized)
        spaceships.append(resized)

    frame_1 = tk.Frame(toplevel, width=600, height=450, bg=TRAN_BLUE)
    frame_1_title = tk.Frame(frame_1, bg = TRAN_BLUE,width=600, height=40)
    label_1_title = tk.Label(frame_1_title, text="궤도", font=font_option, bg=TRAN_BLUE)
    frame_1_1 = tk.Frame(frame_1, width=600, height=450, bg=MINT)

    frame_1_a = tk.Frame(frame_1_1, width=295, height=195, bg=MINT, bd=0)
    frame_1_b = tk.Frame(frame_1_1, width=295, height=195, bg=MINT, bd=0)
    frame_1_c = tk.Frame(frame_1_1, width=295, height=195, bg=MINT, bd=0)
    frame_1_d = tk.Frame(frame_1_1, width=295, height=195, bg=MINT, bd=0)

    button_1_a = tk.Button(frame_1_a, borderwidth=0, image=shapes[0], command=btn_sh_a, highlightthickness=0, relief="sunken", bg=LIGHTBLUE, activebackground=CONTROL_PANEL_BG)
    button_1_b = tk.Button(frame_1_b, borderwidth=0, image=shapes[1], command=btn_sh_b, highlightthickness=0, relief="sunken", bg=LIGHTBLUE, activebackground=CONTROL_PANEL_BG)
    button_1_c = tk.Button(frame_1_c, borderwidth=0, image=shapes[2], command=btn_sh_c, highlightthickness=0, relief="sunken", bg=LIGHTBLUE, activebackground=CONTROL_PANEL_BG)
    button_1_d = tk.Button(frame_1_d, borderwidth=0, image=shapes[3], command=btn_sh_d, highlightthickness=0, relief="sunken", bg=LIGHTBLUE, activebackground=CONTROL_PANEL_BG)

    button_1_a.image = shapes[0]
    button_1_b.image = shapes[1]
    button_1_c.image = shapes[2]
    button_1_d.image = shapes[3]

    button_shapes = [button_1_a, button_1_b, button_1_c, button_1_d]

    frame_2 = tk.Frame(toplevel, width=200, height=450, bg=TRAN_BLUE)
    frame_2_title = tk.Frame(frame_2, bg = TRAN_BLUE,width=200, height=40)
    label_2_title = tk.Label(frame_2_title, text="우주선", font=font_option, bg=TRAN_BLUE)
    frame_2_1 = tk.Frame(frame_2, width=200, height=450, bg=MINT)

    frame_2_a = tk.Frame(frame_2_1, width=160, height=int(350/3), bg=MINT, bd=0)
    frame_2_b = tk.Frame(frame_2_1, width=160, height=int(350/3), bg=MINT, bd=0)
    frame_2_c = tk.Frame(frame_2_1, width=160, height=int(350/3), bg=MINT, bd=0)

    button_2_a = tk.Button(frame_2_a, borderwidth=0, command=btn_sp_a, image=spaceships[0], highlightthickness=0, relief="sunken", bg=LIGHTBLUE, activebackground=CONTROL_PANEL_BG)
    button_2_b = tk.Button(frame_2_b, borderwidth=0, command=btn_sp_b, image=spaceships[1], highlightthickness=0, relief="sunken", bg=LIGHTBLUE, activebackground=CONTROL_PANEL_BG)
    button_2_c = tk.Button(frame_2_c, borderwidth=0, command=btn_sp_c, image=spaceships[2], highlightthickness=0, relief="sunken", bg=LIGHTBLUE, activebackground=CONTROL_PANEL_BG)

    button_spaceships = [button_2_a, button_2_b, button_2_c]

    button_2_a.image = spaceships[0]
    button_2_b.image = spaceships[1]
    button_2_c.image = spaceships[2]

    frame_fin = tk.Frame(toplevel, bg = TRAN_BLUE,width=800, height=50)
    frame_fin.pack(side="bottom")
    frame_fin.pack_propagate(0)

    frame_1.pack(side="left")
    frame_1.pack_propagate(0)

    frame_1_title.pack(side="top")
    frame_1_title.pack_propagate(0)
    label_1_title.pack(side="left", padx=10, pady=(10, 0))
    frame_1_1.pack(padx=(10, 0), pady=10)
    frame_1_1.grid_propagate(0)

    frame_1_a.grid(row=0, column=0)
    frame_1_a.pack_propagate(0)
    button_1_a.pack(fill="both", expand=True, padx=(10, 5), pady=(10, 5))

    frame_1_b.grid(row=0, column=1)
    frame_1_b.pack_propagate(0)
    button_1_b.pack(fill="both", expand=True, padx=(5, 10), pady=(10, 5))

    frame_1_c.grid(row=1, column=0)
    frame_1_c.pack_propagate(0)
    button_1_c.pack(fill="both", expand=True, padx=(10, 5), pady=(5, 10))

    frame_1_d.grid(row=1, column=1)
    frame_1_d.pack_propagate(0)
    button_1_d.pack(fill="both", expand=True, padx=(5, 10), pady=(5, 10))


    frame_2.pack(side="right")
    frame_2.pack_propagate(0)

    frame_2_title.pack(side="top")
    frame_2_title.pack_propagate(0)
    label_2_title.pack(side="left", padx=10, pady=(10, 0))
    frame_2_1.pack(padx=10, pady=10)
    frame_2_1.pack_propagate(0)


    frame_2_a.pack(side="top", padx=10, pady=(10, 0))
    frame_2_a.pack_propagate(0)
    button_2_a.pack(fill="both", expand=True)

    frame_2_b.pack(side="top", padx=10, pady=(10, 0))
    frame_2_b.pack_propagate(0)
    button_2_b.pack(fill="both", expand=True)
    frame_2_c.pack(side="top", padx=10, pady=(10, 0))
    frame_2_c.pack_propagate(0)
    button_2_c.pack(fill="both", expand=True)

    update_sh()
    update_sp()

    frame_fin_1 = tk.Frame(frame_fin, bg = TRAN_BLUE,width=300, height=50)
    frame_fin_1.pack(side="right")
    frame_fin_1.pack_propagate(0)
    button_finish = tk.Button(frame_fin_1, text="적용", width=12, command=btn_finish)
    button_cancel = tk.Button(frame_fin_1, text="취소", width=12, command=btn_cancel)
    button_cancel.pack(side="right", padx=(0,16))
    button_finish.pack(side="right", padx=16)
    return

def btn_op1():
    global op1_on

    if op1_on:
        button_set_o_1.config(image = img_off)
        op1_on = False
    else:
        button_set_o_1.config(image = img_on)
        op1_on = True
    return

def btn_op2():
    global op2_on

    if op2_on:
        button_set_o_2.config(image = img_off)
        op2_on = False
    else:
        button_set_o_2.config(image = img_on)
        op2_on = True
    return

def btn_op3():
    global op3_on

    if op3_on:
        button_set_o_3.config(image = img_off)
        op3_on = False
    else:
        button_set_o_3.config(image = img_on)
        op3_on = True
    return

def btn_prepare():

    global t_play
    global start_signal
    global t_sp_1
    global t_sp_2
    global t_s
    global rotate_count
    global start_sandwich

    t_play = False
    start_signal = False

    global success
    global img_spaceship

    na = items_n_1[combobox_n_1.current()]
    ns = items_n_2[combobox_n_2.current()]

    rotate_count = ns

    r = int(scale_r.get())*1000

    e = shape_e[shape]

    img_spaceship = img_sp[spaceship]

    combo_v_1 = combobox_v_1.current()

    rotate_direction = combobox_v_2.current()

    separation = items_v_3_1[combobox_v_3.current()]

    if rotate_direction==0:
        ellipse_sp_1.config(counterclockwise=True)
        ellipse_sp_2.config(counterclockwise=True)
        ellipse_s.config(counterclockwise=True)
    elif rotate_direction==1 or rotate_direction==-1:
        ellipse_sp_1.config(counterclockwise=False)
        ellipse_sp_2.config(counterclockwise=False)
        ellipse_s.config(counterclockwise=False)

    ellipse_sp_1.set_r(r=r)
    ellipse_sp_2.set_r(r=r)
    

    ellipse_sp_1.set_a(e=e)
    ellipse_sp_2.set_a(e=e)

    ellipse_s.set_r(r=ellipse_sp_1.r_sandwich)

    Ta = ellipse_sp_1.T

    Ts = (na*Ta - separation*Ta)/ns

    print("Ts : "+str(Ts))

    v_success = 0

    if ellipse_s.set_v(t=Ts) is False:
        if combo_v_1 is 0:
            messagebox.showinfo("알림", "성공하는 루트가 없습니다")
            success = False
            return
    else: 
        v_success = ellipse_s.v
        if combo_v_1==0:
            success = True

    print(v_success)

    if op3_on==True and ellipse_s.collide[0]==True and combo_v_1==0:
        messagebox.showinfo("지구와 충돌", "성공하는 루트가 없습니다")
        success = False
        return

    v = 0
    if combo_v_1==1 or combo_v_1==-1:
        try:
            v = int(combobox_v_1.get())
        except ValueError:
            messagebox.showwarning("잘못된 입력", "숫자를 입력해주세요")
            success = False
            return
        else:
            if v < 0:
                messagebox.showwarning("잘못된 입력", "0또는 양수를 입력해주세요")
                success = False
                return

            if v<0.005:
                v = 0.0043
            elif v>10**5:
                messagebox.showwarning("오버 플로우", "더 작은 수를 입력해주세요")
                success = False
                return
            if v_success-1<v and v<v_success+1:
                v = v_success
                success = True
            ellipse_s.set_v(v_=v)


    t_sp_1 = int(len(ellipse_sp_1.w)*separation)
    t_sp_2 = 0
    t_s = 0
    start_sandwich = False
    
    return

def btn_ct1():
    global start_signal
    if start_signal is False:
        start_signal = True
        root.after(start_time, start)
    global t_play
    t_play = True
    return

def btn_ct2():
    global t_play
    t_play = False
    return

def btn_ct3():
    return

def btn_ct4():
    return

def btn_ct5():
    on_closing()
    return

def combobox_v():
    if combobox_v_1.current()==0:
        frame_cp.focus()
        combobox_v_1.config(state="readonly")
    else:
        combobox_v_1.config(state="normal")
        combobox_v_1.set('')
    return

def scale_set_label():
    temp = str(scale_r.get())
    label_set_r_2.config(text=temp+"\n(km)")
    return

def insert_text(str):
    text_area.configure(state="normal")
    text_area.insert(tk.INSERT, str)
    text_area.configure(state="disabled")
    return

def update_cp_img():
    button_set_s_1.config(image=img_shapes_CP[shape])
    button_set_s_2.config(image=img_spaceships_CP[spaceship])
    print(spaceship)
    button_set_s_1.update()
    button_set_s_2.update()
    update_scale()
    return

def update_scale():
    l = scale_limit[shape]
    interval = l[0]
    limit = l[1]
    scale_r.config(tickinterval=interval, from_=limit)
    scale_r.set(10000)
    scale_r.update()
    return

CP_WIDTH = int(SCREEN_WIDTH/3)
CP_HEIGHT = int((SCREEN_HEIGHT - int(SCREEN_HEIGHT*(1/16)))*(1/3))
PAD = int(15/1020*SCREEN_HEIGHT)

CANVAS_WIDTH = int((SCREEN_WIDTH-int(SCREEN_WIDTH/3))*(9/10))
CANVAS_HEIGHT = int(SCREEN_HEIGHT*(9/10))

# 폰트 설정
font_title = tk.font.Font(size=25, weight="bold")
font_option = tk.font.Font(size=12, weight="bold")
font_vs = tk.font.Font(size=20, weight="bold")

# 이미지 파일
img_space_init = Image.open("source/space.png")
resized = img_space_init.resize((int((SCREEN_WIDTH-int(SCREEN_WIDTH/3))*(9/10))+10, int(SCREEN_HEIGHT*(9/10))+10), Image.Resampling.LANCZOS)
img_space = ImageTk.PhotoImage(resized)

img_earth_init = Image.open("source/earth.png")
resized = img_earth_init.resize((int(CANVAS_WIDTH/6), int(CANVAS_WIDTH/6)), Image.Resampling.LANCZOS)
img_earth = ImageTk.PhotoImage(resized)

img_spaceship_init = Image.open ("source/satellite.png")
resized = img_spaceship_init.resize((50, 50), Image.Resampling.LANCZOS)
img_spaceship = ImageTk.PhotoImage(resized)

img_on_init = Image.open("source/on.png")
img_on_init = png_change_bg(img_on_init, LIGHTBLUE)
resized = img_on_init.resize((60, 30), Image.Resampling.LANCZOS)
img_on = ImageTk.PhotoImage(resized)

img_off_init = Image.open("source/off.png")
img_off_init = png_change_bg(img_off_init, LIGHTBLUE)
resized = img_off_init.resize((60, 30), Image.Resampling.LANCZOS)
img_off = ImageTk.PhotoImage(resized)

img_prepare_init = Image.open("source/prepare_toss.png")
img_prepare_init = png_change_bg(img_prepare_init, CONTROL_PANEL_BG)
resized = img_prepare_init.resize((CP_WIDTH-int(CP_WIDTH*(3/5)), int((CP_HEIGHT-2*PAD)*(1/4))), Image.Resampling.LANCZOS)
img_prepare = ImageTk.PhotoImage(resized)

img_control_1_init = Image.open("source/btn_play.png")
img_control_1_init = png_change_bg(img_control_1_init, CONTROL_PANEL_BG)
resized = img_control_1_init.resize((int((CP_HEIGHT-2*PAD)*(1/3)), int((CP_HEIGHT-2*PAD)*(1/3))), Image.Resampling.LANCZOS)
img_control_1 = ImageTk.PhotoImage(resized)

img_control_2_init = Image.open("source/btn_pause.png")
img_control_2_init = png_change_bg(img_control_2_init, CONTROL_PANEL_BG)
resized = img_control_2_init.resize((int((CP_HEIGHT-2*PAD)*(1/3)), int((CP_HEIGHT-2*PAD)*(1/3))), Image.Resampling.LANCZOS)
img_control_2 = ImageTk.PhotoImage(resized)

img_control_3_init = Image.open("source/btn_stop.png")
img_control_3_init = png_change_bg(img_control_3_init, CONTROL_PANEL_BG)
resized = img_control_3_init.resize((int((CP_HEIGHT-2*PAD)*(1/3)), int((CP_HEIGHT-2*PAD)*(1/3))), Image.Resampling.LANCZOS)
img_control_3 = ImageTk.PhotoImage(resized)

img_control_4_init = Image.open("source/btn_re.png")
img_control_4_init = png_change_bg(img_control_4_init, CONTROL_PANEL_BG)
resized = img_control_4_init.resize((int((CP_HEIGHT-2*PAD)*(1/3)), int((CP_HEIGHT-2*PAD)*(1/3))), Image.Resampling.LANCZOS)
img_control_4 = ImageTk.PhotoImage(resized)

img_control_5_init = Image.open("source/btn_power.png")
img_control_5_init = png_change_bg(img_control_5_init, CONTROL_PANEL_BG)
resized = img_control_5_init.resize((int((CP_HEIGHT-2*PAD)*(1/3)), int((CP_HEIGHT-2*PAD)*(1/3))), Image.Resampling.LANCZOS)
img_control_5 = ImageTk.PhotoImage(resized)

img_shape_1_init = Image.open("source/e_0.png")   #0
img_shape_2_init = Image.open("source/e_1.png")   #1
img_shape_3_init = Image.open("source/e_2.png")   #2
img_shape_4_init = Image.open("source/e_3.png")   #3

list_shapes = [img_shape_1_init, img_shape_2_init, img_shape_3_init, img_shape_4_init]

img_spaceship_falcon_init = Image.open("source/falcon.png")   #0
img_spaceship_wing_init = Image.open("source/wing.png")       #1
img_spaceship_star_init = Image.open("source/star.png")       #2

list_spaceships = [img_spaceship_falcon_init, img_spaceship_wing_init, img_spaceship_star_init]

img_sandwich_init = Image.open("source/sandwich.png")


# 프레임 설정
frame_cp = tk.Frame(root, relief='solid', bd=0, bg=CONTROL_PANEL_BG, width=int(SCREEN_WIDTH/3), height=SCREEN_HEIGHT)
frame_gp = tk.Frame(root, relief='solid', bd=0, bg="lightgrey", height=SCREEN_HEIGHT)

frame_cp_title = tk.Frame(frame_cp, relief='solid', bd=0, bg=CONTROL_PANEL_BG, width=CP_WIDTH, height=int(SCREEN_HEIGHT*(1/16)))

frame_cp_1 = tk.Frame(frame_cp, relief='solid', bd=0, bg=CONTROL_PANEL_BG, width=CP_WIDTH, height=CP_HEIGHT)
frame_cp_2 = tk.Frame(frame_cp, relief='solid', bd=0, bg=CONTROL_PANEL_BG, width=CP_WIDTH, height=CP_HEIGHT)
frame_cp_3 = tk.Frame(frame_cp, relief='solid', bd=0, bg=CONTROL_PANEL_BG, width=CP_WIDTH, height=CP_HEIGHT)

# CP 1
frame_cp_1_1 = tk.Frame(frame_cp_1, relief='solid', bd=0, bg=CONTROL_PANEL_BG, width=CP_WIDTH-int(CP_WIDTH*(1/3)), height=CP_HEIGHT)
frame_set_r = tk.Frame(frame_cp_1, relief='solid', bd=0, bg=LIGHTBLUE, width=int(CP_WIDTH*(1/3)), height=CP_HEIGHT)
frame_set_r_1 = tk.Frame(frame_set_r, relief='solid', bd=0, bg=LIGHTBLUE)

frame_set_s = tk.Frame(frame_cp_1_1, relief='solid', bd=0, bg=LIGHTBLUE, width=CP_WIDTH-int(CP_WIDTH*(1/3)), height=int((CP_HEIGHT-3*PAD)/2))
frame_set_s_1 = tk.Frame(frame_set_s, relief='solid', bd=0, bg=MINT, width=int((CP_WIDTH-int(CP_WIDTH*(1/3)))*(3/7))-int(PAD*(3/2)), height=int((CP_HEIGHT-3*PAD)/2))
frame_set_s_2 = tk.Frame(frame_set_s, relief='solid', bd=0, bg=MINT, width=int((CP_WIDTH-int(CP_WIDTH*(1/3)))*(3/7))-int(PAD*(3/2)), height=int((CP_HEIGHT-3*PAD)/2))
frame_set_s_3 = tk.Frame(frame_set_s, relief='solid', bd=0, bg=LIGHTBLUE, width=int((CP_WIDTH-int(CP_WIDTH*(1/3)))*(1/7)), height=int((CP_HEIGHT-3*PAD)/2))

frame_set_n = tk.Frame(frame_cp_1_1, relief='solid', bd=0, bg=LIGHTBLUE, width=CP_WIDTH-int(CP_WIDTH*(1/3)), height=int((CP_HEIGHT-3*PAD)/2))
frame_set_n_1 = tk.Frame(frame_set_n, relief='solid', bd=0, bg=LIGHTBLUE, width=int((CP_WIDTH-int(CP_WIDTH*(1/3)))/2), height=int((CP_HEIGHT-3*PAD)/2))
frame_set_n_2 = tk.Frame(frame_set_n, relief='solid', bd=0, bg=MINT, width=int((CP_WIDTH-int(CP_WIDTH*(1/3)))/2), height=int((CP_HEIGHT-3*PAD)/2))

frame_set_r.config(highlightbackground=CONTROL_BD_COLOR, highlightcolor=CONTROL_BD_COLOR, highlightthickness=3)
frame_set_s.config(highlightbackground=CONTROL_BD_COLOR, highlightcolor=CONTROL_BD_COLOR, highlightthickness=3)
frame_set_n.config(highlightbackground=CONTROL_BD_COLOR, highlightcolor=CONTROL_BD_COLOR, highlightthickness=3)

label_set_r_1 = tk.Label(frame_set_r, text="지\n구\n중\n심\n으\n로\n부\n터\n\n거\n리", font=font_option, bg=MINT, fg="black")
label_set_r_2 = tk.Label(frame_set_r_1, text="10000\n(km)", font=font_option, bg=LIGHTBLUE, fg="black")

label_set_n_1 = tk.Label(frame_set_n_1, text="Na = ", font=font_title, bg=LIGHTBLUE, fg="black")
label_set_n_2 = tk.Label(frame_set_n_2, text="Ns = ", font=font_title, bg=MINT, fg="black")

shape_e = (0, 0.1, 0.2, 0.4)

shape = 0
spaceship = 0

shape_temp = 0
spaceship_temp = 0

button_set_s = tk.Button(frame_set_s_3, text="수\n정", background=MINT, font=font_option, command=btn_set_s, width=100, height=int((CP_HEIGHT-3*PAD)/2)-2*PAD)

label_set_s_1 = tk.Label(frame_set_s_1, text="궤\n도", font=font_option, bg=MINT, fg="black")
button_set_s_1 = tk.Button(frame_set_s_1, borderwidth=0, highlightthickness=0, relief="sunken", command=btn_set_s, bg=CONTROL_PANEL_BG, activebackground=CONTROL_PANEL_BG)

label_set_s_2 = tk.Label(frame_set_s_2, text="우\n주\n선", font=font_option, bg=MINT, fg="black")
button_set_s_2 = tk.Button(frame_set_s_2, borderwidth=0, highlightthickness=0, relief="sunken", command=btn_set_s, bg=CONTROL_PANEL_BG, activebackground=CONTROL_PANEL_BG)

# CP 2
frame_cp_2_1 = tk.Frame(frame_cp_2, relief='solid', bd=0, bg=CONTROL_PANEL_BG, width=CP_WIDTH-int(CP_WIDTH*(3/5)), height=CP_HEIGHT)
frame_cp_2_2 = tk.Frame(frame_cp_2, relief='solid', bd=0, bg=CONTROL_PANEL_BG, width=int(CP_WIDTH*(3/5)), height=CP_HEIGHT)
frame_set_o = tk.Frame(frame_cp_2_2, relief='solid', bd=0, bg=LIGHTBLUE, width=int(CP_WIDTH*(3/5)), height=int((CP_HEIGHT-2*PAD)*(3/4)))
frame_set_f = tk.Frame(frame_cp_2_2, relief='solid', bd=0, bg=LIGHTBLUE, width=int(CP_WIDTH*(3/5)), height=int((CP_HEIGHT-2*PAD)*(1/4)))

frame_set_v = tk.Frame(frame_cp_2_1, relief='solid', bd=0, bg=LIGHTBLUE, width=CP_WIDTH-int(CP_WIDTH*(3/5)), height=int((CP_HEIGHT-2*PAD)*(3/4)))
frame_set_v_1 = tk.Frame(frame_set_v, relief='solid', bd=0, bg=MINT, width=CP_WIDTH-int(CP_WIDTH*(3/5)), height=int((CP_HEIGHT-2*PAD)*(3/4)*(1/2)))
frame_set_v_2 = tk.Frame(frame_set_v, relief='solid', bd=0, bg=LIGHTBLUE, width=CP_WIDTH-int(CP_WIDTH*(3/5)), height=int((CP_HEIGHT-2*PAD)*(3/4)*(1/4)))
frame_set_v_3 = tk.Frame(frame_set_v, relief='solid', bd=0, bg=MINT, width=CP_WIDTH-int(CP_WIDTH*(3/5)), height=int((CP_HEIGHT-2*PAD)*(3/4)*(1/4)))

frame_set_cal = tk.Frame(frame_cp_2_1, relief='solid', bd=0, bg=CONTROL_PANEL_BG, width=CP_WIDTH-int(CP_WIDTH*(3/5)), height=int((CP_HEIGHT-2*PAD)*(1/4)))
frame_set_o.config(highlightbackground=CONTROL_BD_COLOR, highlightcolor=CONTROL_BD_COLOR, highlightthickness=3)
frame_set_f.config(highlightbackground=CONTROL_BD_COLOR, highlightcolor=CONTROL_BD_COLOR, highlightthickness=3)
frame_set_v.config(highlightbackground=CONTROL_BD_COLOR, highlightcolor=CONTROL_BD_COLOR, highlightthickness=3)

frame_set_o_1 = tk.Frame(frame_set_o, relief='solid', bd=0, bg=LIGHTBLUE, width=int(CP_WIDTH*(3/5))-6, height=int((int((CP_HEIGHT-2*PAD)*(3/4)))/3))
frame_set_o_2 = tk.Frame(frame_set_o, relief='solid', bd=0, bg=LIGHTBLUE, width=int(CP_WIDTH*(3/5))-6, height=int((int((CP_HEIGHT-2*PAD)*(3/4)))/3))
frame_set_o_3 = tk.Frame(frame_set_o, relief='solid', bd=0, bg=LIGHTBLUE, width=int(CP_WIDTH*(3/5))-6, height=int((int((CP_HEIGHT-2*PAD)*(3/4)))/3))

label_set_o_1 = tk.Label(frame_set_o_1, text="우주선의 궤도 표시    ", font=font_option, bg=LIGHTBLUE, fg="black")
label_set_o_2 = tk.Label(frame_set_o_2, text="샌드위치 궤도 표시    ", font=font_option, bg=LIGHTBLUE, fg="black")
label_set_o_3 = tk.Label(frame_set_o_3, text="지구와의 충돌 고려    ", font=font_option, bg=LIGHTBLUE, fg="black")

label_set_f = tk.Label(frame_set_f, text="애니메이션 속도   : ", font=font_option, bg=LIGHTBLUE, fg="black")

label_set_v_1 = tk.Label(frame_set_v_1, text="Vs = ", font=font_vs, bg=MINT, fg="black")

label_set_v_2 = tk.Label(frame_set_v_2, text="회전방향 : ", font=font_option, bg=LIGHTBLUE, fg="black")

label_set_v_3 = tk.Label(frame_set_v_3, text="Separation : ", font=font_option, bg=MINT, fg="black")

button_set_o_1 = tk.Button(frame_set_o_1, image=img_off, borderwidth=0, highlightthickness=0, relief="sunken", command=btn_op1, bg=LIGHTBLUE, activebackground=LIGHTBLUE)
button_set_o_2 = tk.Button(frame_set_o_2, image=img_off, borderwidth=0, highlightthickness=0, relief="sunken", command=btn_op2, bg=LIGHTBLUE, activebackground=LIGHTBLUE)
button_set_o_3 = tk.Button(frame_set_o_3, image=img_off, borderwidth=0, highlightthickness=0, relief="sunken", command=btn_op3, bg=LIGHTBLUE, activebackground=LIGHTBLUE)

button_set_cal = tk.Button(frame_set_cal, image=img_prepare, borderwidth=0, highlightthickness=0, command=btn_prepare, bg=CONTROL_PANEL_BG, activebackground=CONTROL_PANEL_BG)

# CP 3
frame_show_info = tk.Frame(frame_cp_3, relief='solid', bd=0, bg=LIGHTBLUE, width=CP_WIDTH-2*PAD, height=int((CP_HEIGHT-2*PAD)*(2/3)))
frame_cp_3_1 = tk.Frame(frame_cp_3, relief='solid', bd=0, bg=CONTROL_PANEL_BG, width=CP_WIDTH-2*PAD, height=int((CP_HEIGHT-2*PAD)*(1/3)))
frame_show_info.config(highlightbackground=CONTROL_BD_COLOR, highlightcolor=CONTROL_BD_COLOR, highlightthickness=3)

text_area = st.ScrolledText(frame_show_info, width = 30, height = 8, font = font_option, background=TRAN_BLUE)

button_control_1 = tk.Button(frame_cp_3_1, width=int((CP_HEIGHT-2*PAD)*(1/3)), height=int((CP_HEIGHT-2*PAD)*(1/3)), image=img_control_1, borderwidth=0, highlightthickness=0, command=btn_ct1, bg=CONTROL_PANEL_BG, activebackground=CONTROL_PANEL_BG)
button_control_2 = tk.Button(frame_cp_3_1, width=int((CP_HEIGHT-2*PAD)*(1/3)), height=int((CP_HEIGHT-2*PAD)*(1/3)), image=img_control_2, borderwidth=0, highlightthickness=0, command=btn_ct2, bg=CONTROL_PANEL_BG, activebackground=CONTROL_PANEL_BG)
button_control_3 = tk.Button(frame_cp_3_1, width=int((CP_HEIGHT-2*PAD)*(1/3)), height=int((CP_HEIGHT-2*PAD)*(1/3)), image=img_control_3, borderwidth=0, highlightthickness=0, command=btn_ct3, bg=CONTROL_PANEL_BG, activebackground=CONTROL_PANEL_BG)
button_control_4 = tk.Button(frame_cp_3_1, width=int((CP_HEIGHT-2*PAD)*(1/3)), height=int((CP_HEIGHT-2*PAD)*(1/3)), image=img_control_4, borderwidth=0, highlightthickness=0, command=btn_ct4, bg=CONTROL_PANEL_BG, activebackground=CONTROL_PANEL_BG)
button_control_5 = tk.Button(frame_cp_3_1, width=int((CP_HEIGHT-2*PAD)*(1/3)), height=int((CP_HEIGHT-2*PAD)*(1/3)), image=img_control_5, borderwidth=0, highlightthickness=0, command=btn_ct5, bg=CONTROL_PANEL_BG, activebackground=CONTROL_PANEL_BG)

label_title = tk.Label(frame_cp_title, text="Sandwich Toss Controls", font=font_title, bg=CONTROL_PANEL_BG, fg="black")

canvas_space = tk.Canvas(frame_gp, width=int((SCREEN_WIDTH-CP_WIDTH)*(9/10)), height=int(SCREEN_HEIGHT*(9/10)))


# Scale
scale_limit = [(4500, 28000), (3000, 25000), (3000, 22000), (1500, 16000)]
var1 = tk.IntVar()
scale_r = tk.Scale(frame_set_r, variable=var1, command= lambda e: scale_set_label(), orient="vertical", showvalue=False, tickinterval=4500, from_=28000, to=10000, length=CP_HEIGHT-2*PAD-6, bg=TRAN_BLUE, bd=1, resolution=100)
scale_r.set(10000)


# Combobox 스타일
style= ttk.Style()
style.map('TCombobox', fieldbackground=[('readonly','white')])
style.map('TCombobox', selectbackground=[('readonly', 'white')])
style.map('TCombobox', selectforeground=[('readonly', 'black')])

items_f = ("매우 느리게", "느리게", "보통", "빠르게", "매우 빠르게")
combobox_f = ttk.Combobox(frame_set_f, width=10, height=10, values=items_f, state='readonly')
combobox_f.current(2)
combobox_f.bind("<<ComboboxSelected>>", lambda e: frame_cp.focus())

items_n_1 = (1, 2, 3, 4, 5, 6)
combobox_n_1 = ttk.Combobox(frame_set_n_1, width=10, height=10, values=items_n_1, state='readonly')
combobox_n_1.current(0)
combobox_n_1.bind("<<ComboboxSelected>>", lambda e: frame_cp.focus())

items_n_2 = (1, 2, 3, 4, 5, 6)
combobox_n_2 = ttk.Combobox(frame_set_n_2, width=10, height=10, values=items_n_2, state='readonly')
combobox_n_2.current(0)
combobox_n_2.bind("<<ComboboxSelected>>", lambda e: frame_cp.focus())

items_v_1 = ("Auto 성공 루트", "직접 입력 (km/h)")
combobox_v_1 = ttk.Combobox(frame_set_v_1, width=100, height=10, values=items_v_1, state='readonly')
combobox_v_1.current(0)
combobox_v_1.bind("<<ComboboxSelected>>", lambda e: combobox_v())

items_v_2 = ("시계반대방향", "시계방향")
combobox_v_2 = ttk.Combobox(frame_set_v_2, width=15, height=10, values=items_v_2, state='readonly')
combobox_v_2.current(0)
combobox_v_2.bind("<<ComboboxSelected>>", lambda e: frame_cp.focus())

items_v_3 = ("0.1 (주기)", "0.2(주기)", "0.3 (주기)", "0.4 (주기)", "0.5 (주기)", "0.6 (주기)", "0.7 (주기)", "0.8 (주기)")
items_v_3_1 = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8)
combobox_v_3 = ttk.Combobox(frame_set_v_3, width=10, height=10, values=items_v_3, state='readonly')
combobox_v_3.current(2)
combobox_v_3.bind("<<ComboboxSelected>>", lambda e: frame_cp.focus())

frame_cp.pack(side='left')
frame_cp.pack_propagate(0)
frame_gp.pack(side='right', expand=True, fill='x')

frame_cp_title.pack(side="top")
frame_cp_title.pack_propagate(0)

label_title.pack(pady=(PAD,0))

frame_cp_1.pack(side="top")
frame_cp_1.pack_propagate(0)

frame_cp_2.pack(side="top")
frame_cp_2.pack_propagate(0)

frame_cp_3.pack(side="top")
frame_cp_3.pack_propagate(0)

frame_cp_1_1.pack(side="left", padx=(PAD, int(PAD/2)), pady=PAD)
frame_cp_1_1.pack_propagate(0)

frame_set_r.pack(side="right", padx=(int(PAD/2), PAD), pady=PAD)
frame_set_r.pack_propagate(0)

frame_set_s.pack(side="top")
frame_set_s.pack_propagate(0)

frame_set_s_1.pack(side="left", pady=PAD, padx=(PAD, int(PAD/2)))
frame_set_s_1.pack_propagate(0)

label_set_s_1.pack(side="left", fill="y")
button_set_s_1.pack(fill="both", expand=True)

frame_set_s_2.pack(side="left", pady=PAD, padx=(int(PAD/2), PAD))
frame_set_s_2.pack_propagate(0)

label_set_s_2.pack(side="left", fill="y")
button_set_s_2.pack(fill="both", expand=True)

button_set_s_1.update()
CP_IMG_WIDTH = button_set_s_1.winfo_width()
CP_IMG_HEIGHT = button_set_s_1.winfo_height()
CP_IMG_K = CP_IMG_HEIGHT-5

if CP_IMG_WIDTH<CP_IMG_K:
    CP_IMG_K = CP_IMG_WIDTH-5

img_shapes_CP = []
img_spaceships_CP = []

for x in range(4):
    resized = list_shapes[x].resize((CP_IMG_K, CP_IMG_K), Image.Resampling.LANCZOS)
    resized = ImageTk.PhotoImage(resized)
    img_shapes_CP.append(resized)

for x in range(3):
    resized = list_spaceships[x].resize((CP_IMG_WIDTH-5, CP_IMG_HEIGHT-5), Image.Resampling.LANCZOS)
    resized = ImageTk.PhotoImage(resized)
    img_spaceships_CP.append(resized)

update_cp_img()

frame_set_s_3.pack(side="left")
frame_set_s_3.pack_propagate(0)

button_set_s.pack(fill="both", expand=True, pady=PAD, padx=(0, PAD))

frame_set_n.pack(side="bottom")
frame_set_n.pack_propagate(0)

frame_set_n_1.pack(side="left")
frame_set_n_1.pack_propagate(0)

label_set_n_1.pack(side="left", padx=(PAD, 0))
combobox_n_1.pack(side="left", padx=(0, PAD))

label_set_n_2.pack(side="left", padx=(PAD, 0))
combobox_n_2.pack(side="left", padx=(0, PAD))

frame_set_n_2.pack(side="right")
frame_set_n_2.pack_propagate(0)

label_set_r_1.pack(side="left", padx=2)
scale_r.pack(side="left")
frame_set_r_1.pack(side="right", fill="both", expand=True)
frame_set_r_1.pack_propagate(0)
label_set_r_2.place(rely=0.4)

frame_cp_2_1.pack(side="left", padx=(PAD, int(PAD/2)), pady=(0, PAD))
frame_cp_2_1.pack_propagate(0)

frame_cp_2_2.pack(side="right", padx=(int(PAD/2), PAD), pady=(0, PAD))
frame_cp_2_2.pack_propagate(0)

frame_set_o.pack(side="top")
frame_set_o.pack_propagate(0)

frame_set_o_1.pack(side="top")
frame_set_o_1.pack_propagate(0)

frame_set_o_2.pack(side="top")
frame_set_o_2.pack_propagate(0)

frame_set_o_3.pack(side="top")
frame_set_o_3.pack_propagate(0)

label_set_o_1.pack(side="left", padx=PAD)
button_set_o_1.pack(side="left", padx=(PAD, 0))

label_set_o_2.pack(side="left", padx=PAD)
button_set_o_2.pack(side="left", padx=(PAD, 0))

label_set_o_3.pack(side="left", padx=PAD)
button_set_o_3.pack(side="left", padx=(PAD, 0))

frame_set_f.pack(side="bottom")
frame_set_f.pack_propagate(0)

label_set_f.pack(side="left", padx=PAD)
combobox_f.pack(side="left", padx=(int(PAD/3), 0))

frame_set_v.pack(side="top")
frame_set_v.pack_propagate(0)

frame_set_v_1.pack(side="top")
frame_set_v_1.pack_propagate(0)

label_set_v_1.pack(side="left", padx=(PAD, 0))
combobox_v_1.pack(side="left", padx=(0, PAD))

frame_set_v_2.pack(side="top")
frame_set_v_2.pack_propagate(0)

label_set_v_2.pack(side="left", padx=(PAD, 0))
combobox_v_2.pack(side="left", padx=(0, PAD))

frame_set_v_3.pack(side="bottom")
frame_set_v_3.pack_propagate(0)

label_set_v_3.pack(side="left", padx=(PAD, 0))
combobox_v_3.pack(side="left", padx=(0, PAD))

frame_set_cal.pack(side="bottom")
frame_set_cal.pack_propagate(0)

button_set_cal.pack(expand=True, fill="both")

frame_show_info.pack(side="top", padx=PAD)
frame_show_info.pack_propagate(0)

text_area.pack(fill="both", expand=True, padx=PAD, pady=PAD)
text_area.configure(state="disabled")

frame_cp_3_1.pack(side="bottom", padx=PAD, pady=PAD)
frame_cp_3_1.pack_propagate(0)

BTN_PAD = int((CP_WIDTH - 2*PAD - 5*int((CP_HEIGHT-2*PAD)*(1/3)))/4)

button_control_1.pack(side="left")
button_control_2.pack(side="left", padx=(BTN_PAD, 0))
button_control_3.pack(side="left", padx=BTN_PAD)
button_control_4.pack(side="left")
button_control_5.pack(side="right")

canvas_space.place(relx=(1-0.9)/2, rely=(1-0.9)/2)
canvas_space.update_idletasks()

obj_space = canvas_space.create_image(canvas_space.winfo_width()/2, canvas_space.winfo_height()/2, image=img_space)
obj_earth = canvas_space.create_image(canvas_space.winfo_width()/2, canvas_space.winfo_height()/2, image=img_earth)


SP_WIDTH = int(80*(CANVAS_WIDTH/1152))
SP_HEIGHT = int(45*(CANVAS_WIDTH/1152))

SD_K = int(30*(CANVAS_WIDTH/1152))

img_sp = []

for x in range(3):
    resized = list_spaceships[x].resize((SP_WIDTH, SP_HEIGHT), Image.Resampling.LANCZOS)
    resized = ImageTk.PhotoImage(resized)
    img_sp.append(resized)

img_spaceship = img_sp[spaceship]

resized = img_sandwich_init.resize((SD_K, SD_K), Image.Resampling.LANCZOS)
img_sandwich = ImageTk.PhotoImage(resized)

#우주선
obj_sd = canvas_space.create_image (200,200, image = img_sandwich)
obj_sp_1 = canvas_space.create_image (200,200, image = img_spaceship)
obj_sp_2 = canvas_space.create_image (200,200, image = img_spaceship)
canvas_space.delete(obj_sd)

ellipse_sp_1 = ellipse(f_point=(canvas_space.winfo_width()/2, canvas_space.winfo_height()/2), win_size=(canvas_space.winfo_width(), canvas_space.winfo_height()))
ellipse_sp_1.ratio = (CANVAS_WIDTH/12)/6400000

ellipse_sp_2 = ellipse(f_point=(canvas_space.winfo_width()/2, canvas_space.winfo_height()/2), win_size=(canvas_space.winfo_width(), canvas_space.winfo_height()))
ellipse_sp_2.ratio = (CANVAS_WIDTH/12)/6400000

ellipse_s = ellipse(f_point=(canvas_space.winfo_width()/2, canvas_space.winfo_height()/2), win_size=(canvas_space.winfo_width(), canvas_space.winfo_height()), rotate_angle=pi/2)
ellipse_s.ratio = (CANVAS_WIDTH/12)/6400000

t_play = True # True : t+=1, False : t+=0

t_sp_1 = 0
t_sp_2 = 0
t_s = 0

start_sandwich = False

rotate_count = 0

def start():
    if start_signal is False:
        return
    global t_s
    global t_sp_1
    global t_sp_2
    global obj_sp_1
    global obj_sp_2
    global obj_sd
    global t_play
    global rotate_count
    global start_sandwich

    if start_sandwich is False:
        if t_sp_2 == ellipse_sp_2.w_12:
            start_sandwich = True

    if t_s==len(ellipse_s.points):
        if ellipse_s.ellipse_hyperbola==1:
            t_s-=1
        else:
            if rotate_count is not 0:
                rotate_count -= 1
                if rotate_count is not 0:
                    t_s=0
            else:
                t_s-=1

    if t_sp_1==len(ellipse_sp_1.points):
        if rotate_count is not 0:
            t_sp_1=0
        else:
            t_sp_1-=1
    if t_sp_2==len(ellipse_sp_2.points):
        if rotate_count is not 0:
            t_sp_2=0
        else:
            t_sp_2-=1

    x, y = ellipse_s.points[t_s]

    x1, y1 = ellipse_sp_1.points[t_sp_1]
    x2, y2 = ellipse_sp_2.points[t_sp_2]

    canvas_space.delete(obj_sp_1)
    canvas_space.delete(obj_sp_2)
    canvas_space.delete(obj_sd)

    obj_sp_1 = canvas_space.create_image (x1, y1, image = img_spaceship)
    obj_sp_2 = canvas_space.create_image (x2, y2, image = img_spaceship)
    if start_sandwich is True:
        obj_sd = canvas_space.create_image (x, y, image = img_sandwich)

    if t_play is True:
        if start_sandwich is True:
            t_s += 1
        t_sp_1+=1
        t_sp_2+=1
    root.after(start_time, start)

root.after(start_time, start)
root.mainloop()