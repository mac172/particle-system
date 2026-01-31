
import pygame
import random
import math

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (20, 20, 30)
FPS = 60

# Simple colors
COLORS = [(255, 80, 80), (255, 160, 20), (255, 220, 100)]

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(4, 8)
        self.color = random.choice(COLORS)
        
        # 1. THE PHYSICS OF SPAWNING
        # We pick a random direction (0 to 360 degrees) and a speed
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 9)
        
        # Convert Angle/Speed to X/Y steps (Trigonometry)
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed

    def move(self):
        # 2. BASIC MOTION
        # Just add velocity to position. No gravity yet.
        self.x += self.dx
        self.y += self.dy

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    particles = []
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
        
        # Input: Hold to spawn
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            for _ in range(5):
                particles.append(Particle(mx, my))

        screen.fill(BG_COLOR)
        
        for p in particles:
            p.move()
            p.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()