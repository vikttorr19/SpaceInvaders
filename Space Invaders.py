import turtle
import os
import math
import random

#Megjelenítés
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

#Alak
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

#Egér
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for sde in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Nullázza a pontot
score = 0

#Írja ki a pontot
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Játékos
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
playerspeed=15

#Ellenfelek mennyisége
number_of_enemies = 5
#Üres lista, ellenfelekből
enemies = []

#Ellenfelek hozzáadása a listához
for i in range(number_of_enemies):
    #Ellenfél készítése
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
    
enemyspeed = 2

#Lövedék
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletspeed=20
bulletstate = "ready"

#Mozgatás
def move_left():
    x=player.xcor()
    x-=playerspeed
    if x<-280:
        x=-280
    player.setx(x)
    
def move_right():
    x=player.xcor()
    x+=playerspeed
    if x>280:
        x=280
    player.setx(x)
    
def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #Lövedék haladása
        x=player.xcor()
        y=player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()
    
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
    
#Billentyűzet
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Menet
while True:
    
    for enemy in enemies:    
        #Ellenfél mozgatása
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)
    
        #Ellenfél mozgatása vissza és le
        if enemy.xcor()>280:
            #Minden ellenfelet lejjebb tesz
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            #Irány változtatás
            enemyspeed *= -1
            
        if enemy.xcor()<-280:
            #Minden ellenfelet lejjeb tesz
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            #Irány változtatás
            enemyspeed *= -1
        #Ellenőrzi, hogy érintkezik e a lövedék az ellenféllel
        if isCollision(bullet, enemy):
            #Visszahelyezése a lövedéknek
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Visszahelyezése az ellenfélnek
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Pontozás
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            if score%50==0:
                enemies.append(turtle.Turtle())
                enemies[-1].color("red")
                enemies[-1].shape("invader.gif")
                enemies[-1].penup()
                enemies[-1].speed(0)
                x = random.randint(-200, 200)
                y = random.randint(100, 250)
                enemies[-1].setposition(x, y)
                
            
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over")
            break
                    
    #Lövedék mozgatás
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    
    #Ellenőrzi, hogy eltűnt e már a lövedék
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
        
wn.mainloop()