from vpython import *


##### Constants
G = 6.647428*10**-11
RE = 6.371*10**6 #Earth radius
t = 0
ME = 5.972*10**24 #Earth mass
RM = 1.737*10**6 #Moon radius
MM = 7.348*10**22 #Moon mass
CMO = 363.104*10**6 #closest distance

Director = -G*ME*MM

'''scene = autoscale=True'''


earth = sphere(pos=vec(0,0,0), radius=RE, color=color.blue, make_trail=True)
earth.m = ME
earthv = vector(0,0,0)
earth.p = earth.pos + earthv

moon = sphere(pos=vec(-CMO,0,0), radius=RM, color=color.white, make_trail=True)
moon.m = MM
moonv = vec(0,0,8.034*10**28)

for i in range(10):
    rate(1)
    moon.pos=moon.pos+moonv
    dist = (moon.pos.x**2 + moon.pos.y**2 + moon.pos.z**2)**0.5
    RadialVector = (moon.pos - earth.pos)/dist
    Fg = -Director*RadialVector/dist**2
    moonv = moonv + Fg
    moon.pos += moonv
    if dist <= earth.radius: break
