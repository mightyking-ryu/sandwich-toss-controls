from math import *

class ellipse:

    ellipse_hyperbola = 0

    G = 6.673*(10**(-11)) #중력상수
    M = 5.972*(10**24) #지구 질량

    r = 6400000*3 #지구 중심으로부터의 거리

    k = 1
    v0 = 1.082*(10**2)*40
    v = v0*k

    a = 0 
    b = 0
    c = 0

    e = 0 #이심률

    T = 0 #주기

    r_sandwich = 0 #샌드위치 r

    f_point = (0, 0) #초점 좌표

    ratio = 0.00001 #축소 비율

    counterclockwise = True #회전 방향 : True-시계반대방향, False-시계방향

    rotate_angle = 0 #회전 각도

    rotate_angle_init = 0

    init_angle = 0 #초기 각도

    rotate_speed = 50 #각속도 비율 (실제 속도는 얼마나 자주 반복되는지에 따라 달라진다 -> 상대적인 값)

    win_size = 0, 0 #좌표계 사이즈

    collide = [False, 0]

    w_12 = 0

    w = []

    points = []

    list_r = []

    def __init__(self, f_point=None, m=None, r=None, k=None, ratio=None, counterclockwise=None, rotate_angle=None, win_size=None, init_angle=None, r_k = None):
        if f_point is not None:
            self.f_point = f_point
        if m is not None:
            self.m = m
        if r is not None:
            self.r = r
        if k is not None:
            self.k= k
        if ratio is not None:
            self.ratio = ratio
        if counterclockwise is not None:
            self.counterclockwise = counterclockwise
        if rotate_angle is not None:
            self.rotate_angle_init = rotate_angle
            self.rotate_angle = rotate_angle
        if win_size is not None:
            self.win_size = win_size
        if init_angle is not None:
            self.init_angle= init_angle
        if r_k is not None:
            self.rotate_speed = r_k*self.rotate_speed
        return

    def config(self, v=None, r=None, e=None, counterclockwise=None):
        if v is not None:
            self.v = v
        if r is not None:
            self.r = r
        if e is not None:
            self.e = e
        if counterclockwise is not None:
            self.counterclockwise = counterclockwise
    
    def set_v(self, v_=None, t=None):
        if v_ is not None:
            self.v0 = v_
        if t is None:
            self.v = self.v0*self.k
        else:
            self.v = (self.G*self.M*(2/self.r - ((4*(pi**2))/((t**2)*self.G*self.M))**(1/3)))**(1/2)
            try:
                v = int(self.v)
            except TypeError:
                print("Fail!")
                return False
            else:
                print("PASS!")
        self.set_a()
        return True

    def set_a(self, e=None):
        self.rotate_angle = self.rotate_angle_init
        if e is None:
            self.a = abs(1/(2/self.r - (self.v**2)/(self.G*self.M)))
            self.c = self.a - self.r
            if self.a**2 - (self.c)**2 > 0:
                if self.c<0:
                    self.rotate_angle = self.rotate_angle_init + pi
            else:
                self.c = self.a + self.r
            self.set_e()
        else:
            self.e = e
            self.a = self.r/(1-e)
            self.c = e*self.a
            self.b = (self.a**2 - self.c**2)**(1/2)
            self.ellipse_hyperbola = 0
            #print("hyperbola : " + str(self.ellipse_hyperbola))
            self.v = (self.G*self.M*(2/self.r-1/self.a))**(1/2)
            self.set_T()
        return

    def set_e(self):
        if self.a**2 - self.c**2 < 0:
            self.b = (self.c**2 - self.a**2)**(1/2)
            self.e = (1+(self.b**2)/(self.a**2))**(1/2)
            self.ellipse_hyperbola = 1
            self.rotate_angle = self.rotate_angle_init + pi
            #print("hyperbola : " + str(self.ellipse_hyperbola))
            self.cal_points_hyperbola()
        else:
            self.b = (self.a**2 - self.c**2)**(1/2)
            self.e = (1-(self.b**2)/(self.a**2))**(1/2)
            self.ellipse_hyperbola = 0
            #print("hyperbola : " + str(self.ellipse_hyperbola))
            self.set_T()
        return

    def set_T(self):
        self.T = 2*pi*(((self.a**3)/(self.G*self.M))**(1/2))
        print("T : "+str(self.T))
        self.cal_points_ellipse()
        return

    def set_r(self, r):
        self.r = r
        return

    def cal_points_ellipse(self):

        self.w = []
        self.points = []
        self.collide = [False, 0]


        M = 0
        k = 2*pi
        if self.c < 0:
            M = pi
            k = 3*pi

        while M <= k:
            E = M
            while True:
                dE = (E - self.e*sin(E) - M)/(1 - self.e*cos(E))
                E -= dE
                if abs(dE)<1e-6:
                    break

            self.w.append(self.get_w_ellipse(E))
            M += 2*pi/self.T*self.rotate_speed

        i = 0
        check = False

        while i<len(self.w):
            x, y = self.get_coordinates(self.w[i])

            if check==False and self.w[i]>=pi/2 and self.counterclockwise==True:
                self.w_12 = i
                self.r_sandwich = int((((x-self.f_point[0])**2 + (y-self.f_point[1])**2)**(1/2))/self.ratio)
                check = True
            elif check==False and self.w[i]>=-pi/2 and self.w[i]<0 and self.counterclockwise==False:
                self.w_12 = i
                self.r_sandwich = int((((x-self.f_point[0])**2 + (y-self.f_point[1])**2)**(1/2))/self.ratio)
                check = True
            
            self.points.append((x, y))
            i+=1
    
        return

    def get_w_ellipse(self, x):
        return 2*atan(((1+self.e)/(1-self.e))**(1/2)*tan(x/2))

    def cal_points_hyperbola(self):

        self.w = []
        self.points = []

        M = 0
        k = self.win_size[0]/100*self.k*pi

        while M <= k:
            E = -M
            while True:
                dE = (self.e*sinh(E) -E - M)/(self.e*cosh(E)-1)
                E -= dE
                if abs(dE)<1e-6:
                    break
            x , y = self.get_coordinates(self.get_w_hyperbola(E))
            if x > self.win_size[0]+100 or x < -100 or y < -100 or y > self.win_size[1]+100:
                break
            self.w.append(self.get_w_hyperbola(E))
            M += (self.G*self.M/(self.a**3))**(1/2)*self.rotate_speed

        i = 0

        while i<len(self.w):
            x, y = self.get_coordinates(self.w[i])
            self.points.append((x, y))
            i+=1
    
        return

    def get_w_hyperbola(self, x):
        return 2*atanh(((self.e+1)/(self.e-1))**(1/2)*tan(x/2))

    def get_r_ellipse(self, x):
        r = self.a*(1-self.e**2)/(1+self.e*cos(x))
        return r

    def get_r_hyperbola(self, x):
        r = -self.a*(self.e**2-1)/(1+self.e*cos(x))
        return r

    def get_coordinates(self, p):

        if self.counterclockwise is True:
            k = p + self.init_angle
        else:
            k = -p + self.init_angle

        if self.a>=0:
            r = self.get_r_ellipse(k)
        else:
            r = self.get_r_hyperbola(k)

        self.list_r.append(r)

        if r <= 6400000:
            self.collide = [True, len(self.points)+1]

        x1 = self.ratio*r*cos(k)
        y1 = self.ratio*r*sin(k)

        x = self.f_point[0] + cos(self.rotate_angle)*x1 - sin(self.rotate_angle)*y1
        y = self.f_point[1] + sin(self.rotate_angle)*x1 + cos(self.rotate_angle)*y1

        x, y = self.convert_coordinate((x, y))

        return x, y

    def convert_coordinate(self, coordinate):
        return coordinate[0], self.win_size[1]-coordinate[1]