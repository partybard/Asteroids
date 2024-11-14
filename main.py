import pygame
import sys
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# Groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids =  pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)


asteroid_field = AsteroidField()

def main():
	# Initialize Pygame
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	#Create a clock
	clock = pygame.time.Clock()
	dt = 0
	# Create Player
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	print(f"""
	Starting asteroids!
	Screen width: {SCREEN_WIDTH}
	Screen height: {SCREEN_HEIGHT}
	""")
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		# Draw the screen
		screen.fill((0, 0, 0))
		#Draw the player
		for obj in updatable:
			obj.update(dt)
		for obj in drawable:
			obj.draw(screen)
		# Update the clock
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		for asteroid in asteroids:
			if player.collision(asteroid):
				print("Game over!")
				sys.exit()
			for shot in shots:
				if shot.collision(asteroid):
					asteroid.split()
					shot.kill()
					
				



if __name__ == "__main__":
		main()
