import pygame as p
import time as tm
import math as m
ang=int(input("Enter angle:"))
pw=int(input("Enter liftoff power(1-300):"))
g=int(input("Enter g:"))
F=int(input("Enter air friction(0-10):"))
th=int(input("Enter thrust(0,10):"))
F/=40
hv=m.cos((m.pi)*ang/180)*pw
vv=m.sin((m.pi)*ang/180)*pw
hype=(vv*vv+hv*hv)**0.5
Hth=hv*th/hype
Vth=vv*th/hype
win=p.display.set_mode((1500,750))
Ball=p.image.load('Ball2.jpg')
ball=[]
Build=p.image.load('building.jpg')
build=[]
n=0
for i in range(0,600):
    ball.append(p.transform.scale(Ball,(100*(1-i*0.0015),100*(1-i*0.0015))))
    build.append(p.transform.scale(Build,(300*(1-i*0.0015),500*(1-i*0.0015))))
x=50
y=640
T=1/60
global coor,z
coor=[]
z=1
def update():
    win.fill((255,255,255))
    win.blit(build[n],(z*1000,750-(450*z)))
    for i in range(0,len(coor)-1):
     p.draw.line(win,(0,0,0),(z*coor[i][0],750-((750-coor[i][1])*z)),(z*coor[i+1][0],750-((750-coor[i+1][1])*z)),8)
    win.blit(ball[n],(z*x,750-((750-y)*z)))
    p.display.update()
update()
run=True
tm.sleep(4)
while(run):
     coor.append([x+50,y+50])
     y-=T*(vv-((g+(F*vv)-Vth)*T/2))
     vv-=(g+(F*vv)-Vth)*T
     x+=T*(hv-((F*hv-Hth)*T/2))
     hv-=(F*hv-Hth)*T
     hype=(vv*vv+hv*hv)**0.5
     Hth=hv*th/hype
     Vth=vv*th/hype
     update()
     tm.sleep(T)
     if (((750-y)*z)<(90*z)):
       run=False
     if (750-((750-y)*z)<(150*z))or(x*z>(1350)):
         z-=0.0015
         n+=1
     for event in p.event.get():
        if event.type==p.QUIT:
            run=False
            p.quit()
