GlowScript 2.9 VPython

k=3 #You may choose k according to how fast or slow you want to see the planetary motion.
z=2 #You may choose higher value of z if you want slower revolution attributes of moon around the earth #Where do you want the camera focus be?
#Please don't change anything here ! And please go to the very bottom of the code
#And you get to select the camera position there.
sun=sphere(pos=vector(0,0,0),radius=50,color=color.yellow)
#sun.texture=textures.sun
mercury=sphere(pos=vector(70*sqrt(2),0,80*sqrt(2)),radius=2.5,color=color.orange,make_trail=False,trail_color=color.white)
#mercury.texture=textures.mercury
venus=sphere(pos=vector(110*sqrt(2),0,106*sqrt(2)),radius=6,color=color.red,make_trail=False,trail_color=color.white)
#venus.texture=textures.venus
earth=sphere(pos=vector(180*sqrt(2),0,160*sqrt(2)),radius=6.3,color=color.cyan,make_trail=False,trail_color=color.white)
earth.texture=textures.earth
mars=sphere(pos=vector(230*sqrt(2),0,210*sqrt(2)),radius=3.39,color=color.green,make_trail=False,trail_color=color.white)
#mars.texture=textures.mars
phobos_mars=sphere(pos=vector(245,0,245),radius=1,color=color.yellow)
diemos_mars=sphere(pos=vector(245,0,245),radius=2,color=color.orange)
moon_earth=sphere(pos=vector(140*sqrt(2),0,150*sqrt(2)),radius=2,color=color.white,make_trail=False)
jupiter=sphere(pos=vector(500*sqrt(2),0,510*sqrt(2)),radius=30,color=color.yellow,make_trail=False,trail_color=color.white)
#jupiter.texture=textures.jupiter
jup_s=sphere(pos=vector(610*sqrt(2),0,610*sqrt(2)),radius=0.8,color=color.white)
jup_moonlist=[jup_s]
for i in range (0,50):
  jup_moonlist.append(jup_s.clone())
for i in range (0,51):
  jup_moonlist[i].pos=vector(600+random()*30,0,600+random()*30)
  
saturn=sphere(pos=vector(800*sqrt(2),0,850*sqrt(2)),radius=16,color=color.orange,make_trail=False,trail_color=color.white)
#saturn.texture=textures.saturn
circ=shapes.circle(radius=50)
saturn_ring=extrusion(path=[vector(800*sqrt(2),0,850*sqrt(2)),vector(800*sqrt(2),0.1,850*sqrt(2))],shape=circ)
sat_s=sphere(pos=vector(830*sqrt(2),0,830*sqrt(2)),radius=2,color=color.white)
sat_moonlist=[sat_s]
for i in range (0,43):
  sat_moonlist.append(sat_s.clone())
for i in range (0,44):
  sat_moonlist[i].pos=vector(900+random()*100,0,900+random()*100)
uranus=sphere(pos=vector(1200*sqrt(2),0,1200*sqrt(2)),radius=10,color=color.cyan,make_trail=False,trail_color=color.white)
#uranus.texture=textures.uranus
neptune=sphere(pos=vector(1500*sqrt(2),0,1500*sqrt(2)),radius=14,color=color.white,make_trail=False,trail_color=color.white)
#neptune.texture=textures.neptune
#asteroid=sphere(pos=vector(400,0,400),radius=3,color=color.white,trail_color=color.white,make_trail=True)

dt=0.01 #Elemental time step
t=0 #Initial value
while(True):
  rate(100)  #Frame rate, 100 Frames every second, otherwise it would have got too fast and crazy !
  sun.pos.x=20*cos(k*2*pi*t/300)
  sun.pos.z=20*sin(k*2*pi*t/300)
  mercury.pos.x=58*sqrt(2)*cos(k*2*pi*t/87.97)
  mercury.pos.z=65*sqrt(2)*sin(k*2*pi*t/87.97)
  venus.pos.x=110*sqrt(2)*cos(k*2*pi*t/224.7)
  venus.pos.z=106*sqrt(2)*sin(k*2*pi*t/224.7)
  earth.pos.x=180*sqrt(2)*cos(k*2*pi*t/365.3)
  earth.pos.z=160*sqrt(2)*sin(k*2*pi*t/365.3)
  mars.pos.x=230*sqrt(2)*cos(k*2*pi*t/680)
  mars.pos.z=210*sqrt(2)*sin(k*2*pi*t/680)
  moon_earth.pos.x=earth.pos.x+40*cos(k*2*pi*t/30*z)
  moon_earth.pos.z=earth.pos.z+40*sin(k*2*pi*t/30*z)
  phobos_mars.pos.x=mars.pos.x+20*cos(k*2*pi*t/100*z)
  phobos_mars.pos.z=mars.pos.z+20*sin(k*2*pi*t/100*z)
  diemos_mars.pos.x=mars.pos.x+40*cos(k*2*pi*t/50*z)
  diemos_mars.pos.z=mars.pos.z+40*sin(k*2*pi*t/50*z)
  jupiter.pos.x=500*sqrt(2)*cos(k*2*pi*t/4332.8)
  jupiter.pos.z=510*sqrt(2)*sin(k*2*pi*t/4332.8)
  jupiter.pos.y=0
  j=50
  d=100
  for i in range(0,51):
    jup_moonlist[i].pos.x=jupiter.pos.x+jup_moonlist[i].pos.x*cos(2*pi*k*t/d)
    jup_moonlist[i].pos.z=jupiter.pos.z+jup_moonlist[i].pos.z*sin(2*pi*k*t/d)
    jup_moonlist[0].pos.y=0
    d+=3
    h=0 
    dh=0.5
    for a in range (0,5):
      for b in range (1,11):
        jup_moonlist[a*10+b].pos.y=h
        h+=dh
        
   
  
  saturn.pos.x=800*sqrt(2)*cos(k*2*pi*t/10755.7)
  saturn.pos.z=850*sqrt(2)*sin(k*2*pi*t/10755.7)
  saturn_ring.pos.x=saturn.pos.x 
  saturn_ring.pos.z=saturn.pos.z
  j=70
  d=100
  for i in range(0,44):
    sat_moonlist[i].pos.x=saturn.pos.x+sat_moonlist[i].pos.x*cos(2*pi*k*t/d)
    sat_moonlist[i].pos.z=saturn.pos.z+sat_moonlist[i].pos.z*sin(2*pi*k*t/d)
    sat_moonlist[0].pos.y=0
    d+=3
    h=0 
    dh=0.5
    for a in range (0,43):
      sat_moonlist[a].pos.y=h
      h+=dh
        
    j+=3
  #saturn_ring.path.append(vector(saturn.pos.x,0.1,saturn.pos.z))
  uranus.pos.x=1200*sqrt(2)*cos(k*2*pi*t/30687.1)
  uranus.pos.z=1240*sqrt(2)*sin(k*2*pi*t/30687.1)
  neptune.pos.x=1500*sqrt(2)*cos(k*2*pi*t/60190)
  neptune.pos.z=1600*sqrt(2)*sin(k*2*pi*t/60190)
  #asteroid.pos.x=300*cos(k*2*pi*t)
  #asteroid.pos.z=300*sin(k*2*pi*t)
  
  
  
  mercury.rotate(axis=vector(0,1,0),angle=k*2*pi*t/58.6)
  venus.rotate(axis=vector(0,1,0),angle=k*2*pi*t/243)
  earth.rotate(axis=vector(0,1,0),angle=k*2*pi*t/10000)
  mars.rotate(axis=vector(0,1,0),angle=k*2*pi*t/1.03)
  
  t+=dt
  # if(t<=3000):
  #   scene.camera.follow(mercury)  #Set the camera such that you would like to see the camera follow that particular body.
  # elif(t>3000 and t<=6000):
  #   scene.camera.follow(venus)
  # elif(t>6000 and t<=9000):
  #   scene.camera.follow(earth)
  # else(t>9000):
  #   scene.camera.follow(mars)
