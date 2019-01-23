import pygame
import sys
import random
import time
import winsound

class Snake():
 def __init__(self):
  self.position=[100,40]
  self.body=[[100,40],[80,40],[60,40],[40,40]]
  self.direction="RIGHT"
  
 def changeDirTo(self,dir):
  if dir=="RIGHT" and not self.direction=="LEFT":
   self.direction="RIGHT"
  if dir=="LEFT" and not self.direction=="RIGHT": 
   self.direction="LEFT"
  if dir=="UP" and not self.direction=="DOWN":
   self.direction="UP"
  if dir=="DOWN" and not self.direction=="UP":
   self.direction="DOWN"
   
   
 def move(self,foodPos):
  if self.direction=="RIGHT":
   self.position[0] += 20
  if self.direction=="LEFT":
   self.position[0] -= 20
  if self.direction=="UP":
   self.position[1] -= 20
  if self.direction=="DOWN":
   self.position[1] += 20
  self.body.insert(0,list(self.position) )
  if self.position==foodPos:
   return 1
  else: 
   self.body.pop()
   return 0
 def checkCollision(self):
  if self.position[0] > 690 or self.position[0] <0:
   return 1
  elif self.position[1] > 490 or self.position[1] <0:
   return 1 
  for bodypart in self.body[1:]:
   if self.position == bodypart:
    return 1
  return 0
 def getHeadPos(self):
  return self.position
 def getBody(self):
  return self.body
class FoodSpawer():
 def __init__(self):
  self.position=[random.randrange(1,35)*20,random.randrange(1,24)*20]
  self.isFoodonScreen=True
 def spawnFood(self):
  if self.isFoodonScreen==False:
   self.position=[random.randrange(1,35)*20,random.randrange(1,24)*20]
   self.isFoodonScreen=True
  return self.position
 def setFoodonScreen(self,b):
  self.isFoodonScreen=b
 def grass(self):
   return self.grass_image
  
window=pygame.display.set_mode((700,500))
pygame.display.set_caption("snake game")
fps=pygame.time.Clock()
score=0
snake=Snake()
foodSpawner=FoodSpawer()
frequency = 2500 
duration =  100
background_image = pygame.image.load("G:\python programs\snake game\\background.jpeg").convert()
snake_image=pygame.image.load("G:\python programs\snake game\\food.jpeg").convert()
#grass_image=pygame.image.load("G:\\python programs\\snake game\\rat.jpeg").convert()
#snake_head=pygame.image.load("C:\Users\Manav Raj\Downloads\\img2.jpg").convert()
def gameOver():
 pygame.quit()
 sys.exit()
 
while True:
 for event in pygame.event.get():
  if event.type==pygame.QUIT:
   gameOver()
  elif event.type==pygame.KEYDOWN:
   if event.key==pygame.K_RIGHT:
    snake.changeDirTo('RIGHT')
   if event.key==pygame.K_LEFT:
    snake.changeDirTo('LEFT')
   if event.key==pygame.K_UP:
    snake.changeDirTo('UP')
   if event.key==pygame.K_DOWN:
    snake.changeDirTo('DOWN')
 foodPos=foodSpawner.spawnFood()
 window.blit(background_image, [0, 0])
 if(snake.move(foodPos)==1):
  winsound.Beep(frequency, duration)
  score+=1
  foodSpawner.setFoodonScreen(False)

 #indow.fill(pygame.Color(0,0,0))
 
 for pos in snake.getBody():
  pygame.draw.rect(window,pygame.Color(255,0,0),pygame.Rect(pos[0],pos[1],20,20))
 window.blit(snake_image,[foodPos[0],foodPos[1]])
 #pygame.draw.rect(window,pygame.Color(255,0,0),pygame.Rect(foodPos[0],foodPos[1],20,20))
 if(snake.checkCollision()==1):
  gameOver()
 pygame.display.set_caption("snake game | score :" + str(score))
 pygame.display.flip()
 fps.tick(15)
 
   
