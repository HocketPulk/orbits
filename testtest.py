from vpython import *

scene = autoscale=True

Sun = sphere(pos=vec(0,0,0),radius=100,color=color.orange)
earth = sphere(pos=vec(-200,0,0),radius=10,color=color.blue,make_trail=True)

earthv=vec(0,0,6)

for i in range(100000000):
    rate(100)
    earth.pos = earth.pos + earthv
    dist = (earth.pos.x**2+earth.pos.y**2+earth.pos.z**2)**0.5
    RadialVector = (earth.pos -Sun.pos)/dist
    Fg = -10000 * RadialVector/dist**2
    earthv=earthv+Fg
    earth.pos += earthv
    if dist <= Sun.radius: break