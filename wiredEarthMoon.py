from vpython import *

scene.select()

Re = 6.37e6                         #Radius of Earth
Rm = 1.174e6                        #Radius of Moon
Rs = 6.95e8                         #Radius of Sun
t = 0
dt = 1000                           #time step size in sec
Se = 1.5e11                         #Earth-Sun distance
Em = 3.48e8                         #Earth-Moon distance
Ms = 1.989e30                       #Mass of Sun
Me = 5.97e24                        #Mass of Earth
Mm = 7.34767e22                     #Mass of Moon
G = 6.67e-11                        #Gravitational Constant

sun = vec(-Se,0,0)                  #Sun is not an object, but a vector outside the view
earth = sphere(pos=vec(0,0,0), radius=Re, color=color.blue,make_trail=True)
earth.m = Me
moon = sphere(pos=vec(-Em,0,0), radius=Rm, color=vec(0.7,0.7,0.7), make_trail=True)
moon.m = Mm

we = sqrt(G*Ms/Se**3)               #Angular speed of the earth
wm = sqrt(G*Me/Em**3)               #Angular speed of the moon (around the earth)
tmonth = 28*24*60*60                #Time it takes the moon to complete an orbit around the earth (in seconds)

earth.p = vec(0,Se*Me*we,0)
moon.p = moon.m*(earth.p / earth.m + vec(0,-Em*wm,0))

while t < tmonth:
    rate(100)
    re = earth.pos - sun            #calc r earth to sun
    rem = moon.pos - earth.pos      #calc r earth to moon
    res = moon.pos - sun            #calc r moon to sun

    #Calc the gravitational forces
    Fe = G * Ms * earth.m * norm(re) / mag(re)**2 + G * earth.m * moon.m * norm(rem) / mag(rem)**2
    Fm = G * Ms * moon.m * norm(res)/ mag(res)**2 - G * earth.m * moon.m * norm(rem) / mag(rem)**2

    #Update momentums
    earth.p = earth.p + Fe *dt
    moon.p = moon.p + Fm *dt

    #Update positions
    earth.pos = earth.pos + earth.p * dt / earth.m
    moon.pos = moon.pos + moon.p * dt /moon.m

    #Update time
    t = t + dt

