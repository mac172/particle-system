import pygame
import random
import math

# --- CONFIGURATION ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (20, 20, 30)
FPS = 60
GRAVITY = 0.25  # <--- NEW CONSTANT

COLORS = [
    (255, 80, 80),   
    (255, 160, 20),   
    (255, 220, 100),  
    (255, 255, 255)  
]

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(4, 8)
        self.color = random.choice(COLORS)
        
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 9)
        
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed

    def move(self):
        # <--- NEW: GRAVITY LOGIC
        # Gravity affects vertical speed (dy), not position directly.
        self.dy += GRAVITY 
        
        self.x += self.dx
        self.y += self.dy

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Stage 2: Gravity")
    clock = pygame.time.Clock()
    
    particles = []
    running = True

    print("👉 STAGE 2: Gravity added. Particles now arc downwards.")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            for _ in range(5):
                particles.append(Particle(mx, my))

        screen.fill(BG_COLOR)
        
        for p in particles:
            p.move()
            p.draw(screen)

        font = pygame.font.SysFont("Arial", 14)
        text = font.render(f"Particles: {len(particles)}", True, (150, 150, 150))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()