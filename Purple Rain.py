import pygame
import random
pygame.init()

#window settings
title = "Purple Rain"
size = width, height = 640, 360

#colors in rgb
background = (230, 230, 250)
purple = (138, 43, 226)

#initialization
drops = []
distance = {}
speed = {}
clock = pygame.time.Clock()
window = pygame.display.set_mode(size)
pygame.display.set_caption(title)

#classes
class Drop:
	def __init__(self, x, y, z, speed, length, width):
		self.x = x
		self.y = y
		self.z = z
		self.speed = speed
		self.len = length
		self.width = width
		self.gravity = 0.1

	def fall(self):
		self.y += self.speed
		self.speed += self.gravity
		if self.y > height:
			self.y = random.randint(-500, -50)
			z = random.randint(0, 20)
			self.speed = speed[z]

	def show(self):
		self.color = (138, 43, 226)
		pygame.draw.line(window, self.color, (self.x, int(self.y)), (self.x, int(self.y + self.len)), self.width)



def create3D():
	length = 10
	speedDiff = 4
	for i in range(21):
		distance[i] = length
		speed[i] = speedDiff
		length += 0.5
		speedDiff += 0.3


#draws window
def setup():
	for i in range(550):
		x = random.randint(0, 700)
		y = random.randint(-500, -50)
		z = random.randint(0, 20)
		lineWidth = 1 if z < 14 else 2
		drop = Drop(x, y, z, speed[z], distance[z], lineWidth)
		drops.append(drop)


#draw game window
def redrawGameWin():
	window.fill(background)
	for i in range(550):
		drops[i].fall()
		drops[i].show()
	pygame.display.update()


#main loop
create3D()
run = True
while run:
	setup()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	redrawGameWin()
	clock.tick(70)

pygame.quit()
