import pygame
pygame.init()

win =pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

class characters(object):
	def __init__(self,height,width,x,y,speed):
		self.height = height
		self.width = width
		self.x = x
		self.y = y
		self.speed = speed
		
class balls(object):
	def __init__(self,height,width,x,y,speed,LorR, UorD, WorL):
		self.height = height
		self.width = width
		self.x = x
		self.y = y
		self.speed = speed
		self.LorR = LorR
		self.UorD = UorD
		self.WorL = WorL

black = (0, 0, 0)
white = (255,255,255)
red = (255, 1, 1)
blue = (1, 1, 255)

run = True
paddle1 = characters(100, 25, 10, 500/2 - 50, 10)
paddle2 = characters(100, 25, 465, 500/2 - 50, 10)
ball = balls(25, 25, 500/2, 500/2, 10, True, None, None)


while run:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w] and paddle1.y > paddle1.speed:
		paddle1.y -= paddle1.speed

	if keys[pygame.K_s]and paddle1.y < 500 - paddle1.height - paddle1.speed:
		paddle1.y += paddle1.speed

	if ball.y < paddle1.y + paddle1.height and ball.y > paddle1.y - paddle1.height/4:
		print('placeholder')
	else:
		if paddle2.y > ball.y - ball.height:
			paddle2.y -= paddle2.speed
		elif paddle2.y < ball.y - ball.height:
			paddle2.y += paddle2.speed
	if ball.x > 500:
		run = False
	if ball.x < 0:
		run = False
	if ball.LorR:
		ball.x -= 10
	else:
		ball.x += 10
	if ball.UorD == 0:
		ball.y -= 10
	elif ball.UorD == -1:
		ball.y += 10
	if ball.y > 490 and ball.x > 0 and ball.x < 500:
		ball.UorD = 0
	if ball.y < 10 and ball.x > 0 and ball.x < 500:
		ball.UorD = -1
	if ball.x < paddle1.x + paddle1.width and ball.y < paddle1.y + paddle1.height and ball.y > paddle1.y - paddle1.height/4:
		ball.UorD = 1
		if ball.y < paddle1.y + paddle1.height - 75:
			ball.UorD = 0
		elif ball.y > paddle1.y + 75:
			ball.UorD = -1
		ball.LorR = False
	elif ball.x > paddle2.x - paddle2.width and ball.y < paddle2.y + paddle2.height and ball.y > paddle2.y - paddle2.height/4:
		ball.LorR = True


	win.fill((0,0,0))
	pygame.draw.rect(win, red, (paddle1.x, paddle1.y, paddle1.width, paddle1.height))
	pygame.draw.rect(win, white, (paddle1.x + 25, paddle1.y, paddle1.width, paddle1.height - 75))
	pygame.draw.rect(win, white, (paddle1.x + 25, paddle1.y + 75, paddle1.width, paddle1.height - 75))
	pygame.draw.rect(win, red, (paddle2.x, paddle2.y, paddle2.width, paddle2.height))
	pygame.draw.rect(win, white, (ball.x, ball.y, ball.width, ball.height))
	pygame.display.update()


