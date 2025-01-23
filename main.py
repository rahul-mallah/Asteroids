# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from live import Live

def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    lives = pygame.sprite.Group()
    Shot.containers = (bullets, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)

    
    AsteroidField.containers = updatable
    Live.containers = (lives, updatable, drawable)

    asteroid_field = AsteroidField() 
    player  = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    positionX = SCREEN_WIDTH/30
    positionY = SCREEN_HEIGHT/16
    
    lives = []
    for i in range(0, 3):
        lives.append(Live(positionX, positionY))
        positionX += 50

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for item in updatable:
            item.update(dt)
        
        for obj in asteroids:
            if obj.collided(player):
                if len(lives) > 0:
                    obj.kill()
                    live = lives.pop()
                    live.kill()
                else:
                    print("Game over!")
                    return
            for bullet in bullets:
                if bullet.collided(obj):
                    obj.split()
                    bullet.kill()
                    break
        
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
