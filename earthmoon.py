from vpython import *


##### Constants
G = 6.647428*10**-11
RE = 6.371*10**6 #Earth radius
ME = 5.972*10**24 #Earth mass
RM = 1.737*10**6 #Moon radius
MM = 7.348*10**22 #Moon mass
REM = 384.4*10**6 #Avg distance

Director = -G*ME*MM

scene = autoscale=True


earth = sphere(pos=vec(0,0,0), radius=RE, color=color.blue, make_trail=True)
earth.m = ME
earthv = vector(0,0,0)
earth.p = earth.pos + earthv

moon = sphere(pos=vec(-REM,0,0), radius=RM, color=color.white, make_trail=True)
moon.m = MM
moonv = vec(0,0,(28.9/360))
'''
for i in range(1000):
    rate(1)
    moon.pos += moonv
    dist = (moon.pos.x**2 + moon.pos.y**2 + moon.pos.z**2)**0.5
    RadialVector = (moon.pos - earth.pos)/dist
    Fg = Director*RadialVector/dist**2
    moonv = moonv + Fg
    if dist <= earth.radius: break
'''