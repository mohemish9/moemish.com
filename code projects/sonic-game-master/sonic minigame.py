GlowScript 2.6 VPython
#milestone.py
#Group Names:
#Alex Posada
#Mohamed Emish
#Chris Paniagua
#December 8, 2017

def make_bomb(starting_position, starting_vel= vector(1,0,0)):
    """Creates a bomb object with a starting position and a starting velocity"""
    bomb_body = sphere( size=1.0*vector(1,1,1), pos=vector(0,0,0), color=color.black )
    bomb_line = cylinder( pos=0.42*vector(0,.9,.0), axis=vector(.02,.2,-.02), size=vector(0.4,0.2,0.2), color=color.white)
    bomb_objects = [bomb_body, bomb_line]
    com_bomb = compound( bomb_objects, pos=starting_position )
    com_bomb.vel = starting_vel   # set the initial velocity
    return com_bomb
    
    
def make_enemy( starting_position, starting_vel):
    """Creates an enemy object with a starting position and a starting velocity"""
    enemy_body = cylinder( size=1.0*vector(1,1,1), pos=vector(0,0,0), color=color.orange)
    enemy_objects = [enemy_body]
    com_enemy = compound( enemy_objects, pos=starting_position )
    com_enemy.vel = starting_vel   # set the initial velocity
    return com_enemy

def make_Sonic( starting_position, starting_vel=vector(0,0,0) ):
    """Creats a Sonic object with starting position and starting velocity"""
    sonic_body1 = sphere(size=0.8*vector(1,1,1),  pos=vector(0,0,0),  color=color.blue)
    sonic_body2 = sphere(size=0.60*vector(1,1,1),  pos=vector(0.2,0,0),  color=vector(1,0.999,0.6))
    sonic_head = sphere(size = 0.8*vector(1,1,1), pos=vector(0,0.7,0), color=color.blue)
    sonic_headspike1 = pyramid(size = 1.4*vector(0.3, 0.3, 0.3), pos = vector(-0.25, 0.7, 0.1), color = color.blue, axis = vector(-1,0,0))
    sonic_headspike2 = pyramid(size = 1.4*vector(0.3, 0.3, 0.3), pos = vector(-0.25, 0.7, -0.1), color = color.blue, axis = vector(-1,0,0))
    sonic_headspike3 = pyramid(size = 1.4*vector(0.3, 0.3, 0.3), pos = vector(-0.1, 0.55, 0), color = color.blue, axis = vector(-1,0,0))
    sonic_headspike4 = pyramid(size = 1.4*vector(0.3, 0.3, 0.3), pos = vector(-0.15, 0.85, 0), color = color.blue, axis = vector(-1,0,0))
    sonic_earA1 = pyramid(size = 0.6*vector(0.3, 0.3, 0.3), pos = vector(0, 1.0, 0.2), color = vector(1,0.999,0.6), axis = vector(0,1,1))
    sonic_earA2 = pyramid(size = 0.6*vector(0.3, 0.3, 0.3), pos = vector(0, 1.0, -0.2), color = vector(1,0.999,0.6), axis = vector(0,1,-1))
    sonic_earB1 = pyramid(size = 0.6*vector(0.3, 0.3, 0.3), pos = vector(-0.01, 1.0, 0.2), color = color.blue, axis = vector(0,1,1))
    sonic_earB2 = pyramid(size = 0.6*vector(0.3, 0.3, 0.3), pos = vector(-0.01, 1.0, -0.2), color = color.blue, axis = vector(0,1,-1))
    sonic_shoesL = pyramid(size = 1.4*vector(0.3, 0.3, 0.3), pos = vector(0.09, -0.7, -0.25), color = color.red)
    sonic_shoesR = pyramid(size = 1.4*vector(0.3, 0.3, 0.3), pos = vector(-0.31, -0.7, 0.25), color = color.red)
    sonic_shoesWL = pyramid(size = 1.1*vector(0.3, 0.3, 0.3), pos = vector(0.09, -0.65, -0.25), color = color.white)
    sonic_shoesWR = pyramid(size = 1.1*vector(0.3, 0.3, 0.3), pos = vector(-0.31, -0.65, 0.25), color = color.white)
    sonic_legL = box(size=0.8*vector(0.6,0.1,0.2), pos=vector(-0.000001,-0.45,-0.2), axis = vector(-1,1,1), color=color.blue)
    sonic_legR = box(size=0.8*vector(0.6,0.1,0.2), pos=vector(-0.1,-0.45,0.2), axis = vector(1,1,-1), color=color.blue)
    sonic_mouth = sphere(size=0.60*vector(1,0.5,1), pos=vector(0.15,0.55,0), axis=vector(0,0,1), color=vector(1,0.999,0.6))
    sonic_nose = sphere(size=0.2*vector(1,0.5,1), pos=vector(0.5,0.55,0), axis=vector(1,0.5,0), color=color.black)
    sonic_eye1 = sphere(size=0.4*vector(1,1,1), pos=vector(0.2,0.7,-0.1), axis=vector(1,0.5,0), color=color.white)
    sonic_eye2 = sphere(size=0.4*vector(1,1,1), pos=vector(0.2,0.7,0.1), axis=vector(1,0.5,0), color=color.white)
    #sonic_eye3 = sphere(size=0.4*vector(1,0.8,1), pos=vector(0.21,0.65,0), axis=vector(1,0.5,0), color=color.white)
    sonic_eyeB1 = sphere(size=0.2*vector(1,1,0.5), pos=vector(0.31,0.7,0.15), axis=vector(1,0.5,0), color=color.black)
    sonic_eyeB2 = sphere(size=0.2*vector(1,1,0.5), pos=vector(0.31,0.7,-0.15), axis=vector(1,0.5,0), color=color.black)
    sonic_arm1 = box(size=0.8*vector(0.6,0.1,0.2), pos=vector(-0.000001,0,0.4), axis = vector(-1,-1,1), color=color.blue)
    sonic_arm2 = box(size=0.8*vector(0.6,0.1,0.2), pos=vector(-0.000001,0,-0.4), axis = vector(-1,-1,1), color=color.blue)
    sonic_backspike = pyramid(size = 1.4*vector(0.3, 0.3, 0.3), pos = vector(-0.25,0.03,0), color = color.blue, axis = vector(-1,-0.3,0))
    sonic_glove1 = sphere(size=0.35*vector(1,1,1),  pos=vector(0.1,0.2,-0.6),  color=color.white)
    sonic_glove2 = sphere(size=0.35*vector(1,1,1),  pos=vector(-0.1,-0.2,0.5),  color=color.white)
    
    sonic_objects = [sonic_body1, sonic_body2, sonic_shoesL, sonic_shoesR, sonic_headspike1,
                        sonic_headspike2, sonic_headspike3, sonic_head, sonic_headspike4,
                        sonic_earA1, sonic_earA2, sonic_earB1, sonic_earB2, sonic_legL,
                        sonic_legR, sonic_mouth, sonic_nose, sonic_eye1, sonic_eye2, sonic_eyeB1,
                        sonic_eyeB2, sonic_arm1,sonic_arm2, sonic_backspike, sonic_glove1, sonic_glove2, sonic_shoesWR, sonic_shoesWL]
    com_sonic = compound( sonic_objects, pos=starting_position )
    com_sonic.vel = starting_vel
    return com_sonic

    


#Creates the ground where all the objects will be moving on
ground = box(size=vector(15,1,200), pos=vector(0,-1,0), color=vector(.196078,.8039215686,.1960784))
#Creates the pyramid and ring that will be the end target
pyr=pyramid(size= vector(1, 3, 1), pos=vector(0, 0,-95), color=color.red, axis=vector(0,1,0))
rin=ring(size=vector(.25,5,5), pos=vector(0,4,-95), color=color.yellow,axis=vector(0,1,0))


#Creates the walls of the ground so that objects do not stray too far from the ground
wallA = box(pos=vector(0,0,-100), axis=vector(1,0,0), size=vector(15,1,.2), color=vector(0.587, 0.39, 0.023)) # amber
wallB = box(pos=vector(-7.5,0,0), axis=vector(0,0,1), size=vector(200,1,.2), color=vector(0.587, 0.39, 0.023))   # blue
wallC = box(pos=vector(0,0,100), axis=vector(1,0,0), size=vector(15,1,.2), color=vector(0.587, 0.39, 0.023)) # ambe
wallD = box(pos=vector(7.5,0,0), axis=vector(0,0,1), size=vector(200,1,.2), color=vector(0.587, 0.39, 0.023))   # blue

#Creates the Sonic character that the user will control
sonic1 = make_Sonic( starting_position = vector(0,0.3,95), starting_vel=vector(0,0,0))
sonic1.vel = vector(0,0,-5)
sonic1.rotate(angle=radians(90), 
           axis=vec(0,1,0))

#Creates the scene with the background color
scene.bind('keydown', keydown_fun)

scene.background = vector(0.8, 1, 1)
scene.width = 640
scene.height = 480


#Creats a list of rings that Sonic can pick up to go faster
rList=[]
for x in range(5):
    rinX = ring(pos=vector(random(-3, 3),0,x*19), axis=vector(0, 0, 1), size=vector(0.2,1,1), color=vector(1, 0.75, 0))
    rinX.vel = vector.random()
    rinX.vel.y = 0.0
    rList.append(rinX)
for x in range(5):
    rinX = ring(pos=vector(random(-3, 3),0,x*-18), axis=vector(0, 0, 1), size=vector(0.2,1,1), color=vector(1, 0.75, 0))
    rinX.vel = vector.random()
    rinX.vel.y = 0.0
    rList.append(rinX)


#Creates a list of bombs
bombs=[]
for x in range(10):
    bomb = make_bomb( starting_position=vector(0,0,70-((x/5)*75)), starting_vel=vector(x+1,0,0 ))
    bombs.append(bomb)
    


#Creates a list of enemies
enemies = []
for x in range(5):
    enemy = make_enemy( starting_position=vector(random(-3,3)+3,0,40-(x*-20)-50), starting_vel=vector(x+1,0,5-x))
    enemies.append(enemy)




# other constants
RATE = 30                # the number of times the while loop runs each second
dt = 1.0/(1.0*RATE)      # the time step each time through the while loop
scene.autoscale = False  # avoids changing the view automatically
Test=True
#Get start time
t1 = clock()
counter = 0
print("Welcome to Sonic! Try and reach the end by using the left and right arrow keys!")
print("Avoid hitting bombs or you will be reset! Collect coins to speed up!")
print("Avoid enemies or you will lose coins and be pushed back!")
while Test==True:    # this is the "event loop": each loop is one step in time, dt
    
    """main function that will run as the program operates"""
    rate(RATE) # maximum number of times per second the while loop runs 
    
    #Position of Sonic is updated here
    sonic1.pos = sonic1.pos + sonic1.vel*dt
    #Centers the camera on the Sonic Character
    scene.center = sonic1.pos
    
    #Updates each ring position and checks if Sonic collides with one of them; Also updates the ring counter
    for rin1 in rList:
        rin1.pos = rin1.pos + rin1.vel*dt
        corral_collide(rin1)
        counter += speedUp(sonic1, rin1)
    
    #if Sonic or the ring collide with a wall, they will bounce back in a linear collision
    corral_collide(sonic1)
    
    
    
    #Checks if Sonic has reached the end target
    #Checks the time and displays the time it took to finish the stage and displays the number of rings collected
    if finish_collide(sonic1):
        t2 = clock()
        sonic1.pos.y= rin.pos.y
        sonic1.pos.z = rin.pos.z
        sonic1.pos.x = rin.pos.x
        Test=False
        print("Congratulations! You finished the game!")
        print("Total Time: " + str(t2-t1) + " seconds!")
        print("You collected " + str(counter) + " rings!")
        
    #Updates each bomb position and checks if they collide with the wall
    for bomb in bombs:
        bomb.pos = bomb.pos + bomb.vel * dt
        corral_collide(bomb)
        
    #Updates each enemy's position and checks if they collide with the wall
    #Checks if the enemies collide with any bomb and udnergoes a spherical collision
    for enemy in enemies:
        enemy.pos = enemy.pos + enemy.vel * dt
        corral_collide(enemy)
        enemy_bombs_collision (enemy, bombs)
    
    #Checks if the enemies collide with each other and they undergo a spherical collision
    for l in range(len(enemies)):
        for k in range(len(enemies)):
            if l != k:
                enemies_collision(enemies[l], enemies[k])
    
    
    #Checks if Sonic collides with the bomb or the enemies
    sonic_bomb_collision(sonic1, bombs)
    
    counter -= sonic_enemy_collision(sonic1, enemies)
    if counter < 0:
        counter = 0
    

def speedUp(sonic, rin1):
    """Checks if Sonic has touched the ring; Returns 1 if ring is collected and 0 if not"""
    if mag( sonic.pos - rin1.pos ) < 1.0:
        sonic.vel = sonic.vel*1.25
        rin1.visible = False
        rin1.pos.y=-100
        print("Ring collected!")
        return 1
    return 0



def finish_collide(sonic):
    """Checks if Sonic and the end target have collided. The hitbox for the end target is a bit
        bigger than the actual end target to make it easier for the player to win"""
    if mag( sonic.pos - pyr.pos ) < 5.0:
        return True 
        
def enemies_collision(enemy1, enemy2):
    """
        Performs a spherical collision on two enemies if they are within a certain distance of each other
    """
    DISTANCE = 1.0   
    s1 = enemy1
    s2 = enemy2
    diff = s1.pos - s2.pos
    if mag( diff ) < DISTANCE:
        dtan = rotate( diff, radians(90), vector(0,1,0) )
        v1 = s1.vel
        v2 = s2.vel
        s1.pos -= v1*dt
        s2.pos -= v2*dt
        v1_rad = proj(v1, diff)
        v1_tan = proj(v1, dtan)
        v2_rad = proj(v2, -diff)
        v2_tan = proj(v2, dtan)
        s1.vel =  v2_rad + v1_tan
        s2.vel =  v1_rad + v2_tan


def enemy_bombs_collision (enemy, bombs):
    """
        Performs a spherical collision on an enemy and a bomb if they are within a certain distance of each other.
        The bomb, however, will keep moving linearly
    """
    for bomb in bombs:
        DISTANCE = 1.0
        s1 = enemy
        s2 = bomb
        diff = s1.pos - s2.pos
        if mag( diff ) < DISTANCE:
            dtan = rotate( diff, radians(90), vector(0,1,0) )
            v1 = s1.vel
            v2 = s2.vel
            s1.pos -= v1*dt
            s2.pos -= v2*dt
            v1_rad = proj(v1, diff); v1_tan = proj(v1, dtan)
            v2_rad = proj(v2, -diff); v2_tan = proj(v2, dtan)
            s1.vel =  v2_rad + v1_tan
            
            
def sonic_enemy_collision(sonic1, enemies):
    """Checks if sonic collided with an enemy and according to our rules,
        he will get pushed back regardless if the enemy hit him from behind;
        returns the number of rings that will be subtracted from the ring counter"""
    numRins = 0
    for enemy in enemies:
        DISTANCE = 1.0
        s1 = sonic1
        s2 = enemy
        diff = s1.pos - s2.pos
        if mag( diff ) < DISTANCE:
            dtan = rotate( diff, radians(90), vector(0,1,0) )
            v1 = s1.vel
            v2 = s2.vel
            s1.pos -= v1*dt
            s2.pos -= v2*dt
            v1_rad = proj(v1, diff); v1_tan = proj(v1, dtan)
            v2_rad = proj(v2, -diff); v2_tan = proj(v2, dtan)
            s1.vel =  v2_rad + v1_tan
            s1.vel.y = 0
            s1.vel.z=-4
            s1.pos.z+=2
            numRins += 1
    return numRins
def sonic_bomb_collision (sonic1, bombs):
    """Checks if sonic collided with a bomb and according to our rules,
        Sonic gets reset to the very beginning of the stage"""
    for bomb in bombs:
        DISTANCE = 1.0
        s1 = sonic1
        s2 = bomb
        diff = s1.pos - s2.pos
        if mag( diff ) < DISTANCE:
            s1.pos = vector(0,0.3,95)
            s1.vel=vector(0,0,-5)
    
    
    
        
def keydown_fun(event):
    """ function called with each key pressed """
    
    key = chr(event.which)
    ri = randint( 0, 10 )
    
    amt = 0.42
    if key in 'A%J': 
        sonic1.vel = sonic1.vel + vector(-amt,0,0)
    if key in "D'L": 
        sonic1.vel = sonic1.vel + vector(amt,0,0)



def choice( L ):
     """implements Python's choice using the random() function"""
     LEN = len(L)   # get the length
     randomindex = int( LEN*random() )  # get a random index
     return L[randomindex]     # return that element
    
def randint( low, hi ):
    if hi < low:  low, hi = hi, low
    LEN = int(hi)-int(low)+1
    randvalue = LEN*random()
    return int(randvalue)


def corral_collide( ball ):
    """ Checks if the object is colliding with a wall and performs a linear collision
    """
    # if the ball hits wallA
    if ball.pos.z < wallA.pos.z: # hit - check for z
        ball.pos.z = wallA.pos.z  # bring back into bounds
        ball.vel.z *= -1.0        # reverse the z velocity
        
    # if the ball hits wallB
    if ball.pos.x < wallB.pos.x: # hit - check for x
        ball.pos.x = wallB.pos.x  # bring back into bounds
        ball.vel.x *= -1.0        # reverse the x velocity
        
    if ball.pos.z > wallC.pos.z: # hit - check for z
        ball.pos.z = wallC.pos.z  # bring back into bounds
        ball.vel.z *= -1.0        # reverse the z velocity
        
    if ball.pos.x > wallD.pos.x: # hit - check for x
        ball.pos.x = wallD.pos.x  # bring back into bounds
        ball.vel.x *= -1.0