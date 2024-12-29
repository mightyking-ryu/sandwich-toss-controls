import tkinter as tk
import tkinter.messagebox
from math import *
from PIL import Image
from PIL import ImageTk


# 화면 사이즈
SCREEN_WIDTH_INIT = 1280
SCREEN_HEIGHT_INIT = 720
SCREEN_WIDTH_FULL = 0
SCREEN_HEIGHT_FULL = 0
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0

# 사진 크기
EARTH_WIDTH = 0
EARTH_HEIGHT = 0

# 초기 화면 GEOMETRY
init_geo = str(SCREEN_WIDTH_INIT)+"x"+str(SCREEN_HEIGHT_INIT)+"+100+50"

# 비율 조정
frame_L_ratio = 0.38
frame_space_ratio = 0.9
earth_ratio = 0.2

# 화면 조정 클래스
class Screen_Window:

    def __init__(self, root):
        self.root = root
        self.state = True    
        self.set_screensize(self.state)
        self.set_obj_size()
        self.root.bind("<F11>", self.toggle_fullscreen)
        self.root.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.set_screensize(self.state)
        self.set_obj_size()
        refresh()
        self.root.attributes("-fullscreen", self.state)
        refresh_obj()
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.set_screensize(self.state)
        self.set_obj_size()
        refresh()
        self.root.attributes("-fullscreen", False)
        refresh_obj()
        #print(SCREEN_WIDTH_FULL, SCREEN_HEIGHT_FULL)
        return "break"

    def set_screensize(self, b):
        global SCREEN_WIDTH
        global SCREEN_HEIGHT
        if b==True:
            SCREEN_WIDTH = SCREEN_WIDTH_FULL
            SCREEN_HEIGHT = SCREEN_HEIGHT_FULL
        else:
            SCREEN_WIDTH = SCREEN_WIDTH_INIT
            SCREEN_HEIGHT = SCREEN_HEIGHT_INIT
        return

    def set_obj_size(self):
        global EARTH_WIDTH
        global EARTH_HEIGHT
        EARTH_WIDTH = int(SCREEN_WIDTH*(1-frame_L_ratio)*frame_space_ratio*earth_ratio)
        EARTH_HEIGHT = EARTH_WIDTH
        return


# 메시지 팝업 클래스
class message_popup:

    def __init__(self, message):
        self.message = message
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        if tkinter.messagebox.askokcancel("Exit", "프로그램을 종료하시겠습니까?"):
            root.destroy()

# 화면 크기 업데이트 함수
def refresh():
    frame_L.configure(width=SCREEN_WIDTH*frame_L_ratio, height=SCREEN_HEIGHT)
    frame_R.configure(width=SCREEN_WIDTH*(1-frame_L_ratio), height=SCREEN_HEIGHT)
    frame_space.configure(width=SCREEN_WIDTH*(1-frame_L_ratio)*frame_space_ratio, height=SCREEN_HEIGHT*frame_space_ratio)
    canvas_space.configure(width=SCREEN_WIDTH*(1-frame_L_ratio)*frame_space_ratio, height=SCREEN_HEIGHT*frame_space_ratio)
    return

# 이미지 업데이트 함수
def refresh_obj():
    canvas_space.update_idletasks()
    temp1 = canvas_space.coords(obj_earth)
    temp2 = canvas_space.coords(obj_space)
    resize_image()
    canvas_space.itemconfigure(obj_earth, image=img_earth)
    canvas_space.move(obj_earth, canvas_space.winfo_width()/2-temp1[0], canvas_space.winfo_height()/2-temp1[1])
    canvas_space.itemconfigure(obj_space, image=img_space)
    canvas_space.move(obj_space, canvas_space.winfo_width()/2-temp2[0], canvas_space.winfo_height()/2-temp2[1])
    return

# 이미지 크기 조정 함수
def resize_image():
    global resized
    global img_earth
    global img_space
    resized = img_earth_init.resize((EARTH_WIDTH, EARTH_HEIGHT), Image.Resampling.LANCZOS)
    img_earth = ImageTk.PhotoImage(resized)
    resized = img_space_init.resize((int(SCREEN_WIDTH*(1-frame_L_ratio)*frame_space_ratio)+1, int(SCREEN_HEIGHT*frame_space_ratio)+1), Image.Resampling.LANCZOS)
    img_space = ImageTk.PhotoImage(resized)
    return

# 이미지 회전 함수
def rotate (degrees):
    img_2 = img.rotate (degrees)
    global tkimg
    tkimg = ImageTk.PhotoImage (img_2)
    return

# root 설정
root = tk.Tk()
root.title("ellipse")
root.geometry(init_geo)
root.resizable(False, False)
root.attributes("-fullscreen", True)
root.update_idletasks() 
SCREEN_WIDTH_FULL = root.winfo_width()
SCREEN_HEIGHT_FULL = root.winfo_height()

# 클래스
screen = Screen_Window(root)
message = message_popup(root)

# 파일
img_space_init = Image.open("source/space.png")
img_earth_init = Image.open("source/earth.png")

resized = img_earth_init.resize((EARTH_WIDTH, EARTH_HEIGHT), Image.Resampling.LANCZOS)
img_earth = ImageTk.PhotoImage(resized)
resized = img_space_init.resize((int(SCREEN_WIDTH*(1-frame_L_ratio)*frame_space_ratio)+1, int(SCREEN_HEIGHT*frame_space_ratio)+1), Image.Resampling.LANCZOS)
img_space = ImageTk.PhotoImage(resized)

img = Image.open ("source/marry.png")
resized = img.resize((70, 70), Image.Resampling.LANCZOS)
img = resized


frame_L = tk.Frame(root, relief="flat", width=SCREEN_WIDTH*frame_L_ratio, height=SCREEN_HEIGHT, bd=1, bg="blue")
frame_R = tk.Frame(root, relief="flat", width=SCREEN_WIDTH*(1-frame_L_ratio), height=SCREEN_HEIGHT, bg="light grey")
frame_space = tk.Frame(frame_R, relief="flat", width=SCREEN_WIDTH*(1-frame_L_ratio)*frame_space_ratio, height=SCREEN_HEIGHT*frame_space_ratio, bg="red")
button1 = tk.Button(frame_L, text="시작", width=8)
canvas_space = tk.Canvas(frame_space, width=SCREEN_WIDTH*(1-frame_L_ratio)*frame_space_ratio, height=SCREEN_HEIGHT*frame_space_ratio, bg="blue", highlightthickness=0, relief="ridge")

frame_L.pack(side="left", fill="both")
frame_R.pack(side="right", fill="both")
frame_space.place(relx=(1-frame_space_ratio)/2, rely=(1-frame_space_ratio)/2)
frame_L.pack_propagate(0)
frame_R.pack_propagate(0)
frame_space.pack_propagate(0)
button1.pack(side="top",fill="x")
canvas_space.place(relx=0, rely=0)
canvas_space.pack_propagate(0)
canvas_space.update_idletasks()
obj_space = canvas_space.create_image(canvas_space.winfo_width()/2, canvas_space.winfo_height()/2, image=img_space)
obj_earth = canvas_space.create_image(canvas_space.winfo_width()/2, canvas_space.winfo_height()/2, image=img_earth)


tkimg = ImageTk.PhotoImage (img)
obj_spaceship = canvas_space.create_image (200,200, image = tkimg, tags = "img")


x = 0
y = 0
r = 200
t = 0

k = 0

a = 4
e = 1/3




def get_r(x):
    r = a*(1-e**2)/(1+e*cos(x))
    return r

def r_v(p):
    return 1/(get_r(p)**2)

f_x = canvas_space.winfo_width()/2
f_y = canvas_space.winfo_height()/2

px_init = f_x
py_init = f_y - 70*get_r(0)*cos(0)
px = f_x
py = f_y
p=0
while p<=360:
    p2 = p/180*pi
    px = f_x - 70*get_r(p2)*sin(p2)
    py = f_y - 70*get_r(p2)*cos(p2)
    if int(p)%3==0:
        canvas_space.create_line(px_init, py_init, px, py, width=5, fill="red")
    px_init = px
    py_init = py
    p += r_v(p2)


def start():
    global x
    global y
    global t
    global k
    global obj_spaceship
    x = f_x - 70*get_r(t)*sin(t)
    y = f_y - 70*get_r(t)*cos(t)

    temp = int(t/pi*180)

    if temp>k:
        rotate(temp)
        k = temp

    canvas_space.delete(obj_spaceship)
    obj_spaceship = canvas_space.create_image (x, y, image = tkimg, tags = "img")

    t += r_v(t)*0.1

    root.after(10, start)

root.after(10, start)


root.mainloop()