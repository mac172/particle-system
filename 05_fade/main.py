import pygame
import random
import math

# --- CONFIGURATION ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (20, 20, 30)
FPS = 60
GRAVITY = 0.25
FRICTION = 0.99
BOUNCE_FACTOR = 0.7
LIFETIME_DECAY = 4  # <--- NEW

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
        
        self.lifetime = 255  # <--- NEW: Starts at full opacity

    def move(self):
        self.dy += GRAVITY
        self.dx *= FRICTION
        self.dy *= FRICTION
        
        self.x += self.dx
        self.y += self.dy
        
        if self.y + self.radius >= SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.radius
            self.dy *= -BOUNCE_FACTOR
            self.dx *= 0.9
        
        # <--- NEW: DECAY
        self.lifetime -= LIFETIME_DECAY

    def draw(self, surface):
        # <--- NEW: TRANSPARENCY DRAWING
        if self.lifetime > 0:
            # We need a temporary surface to support Alpha (transparency)
            target_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
            
            # Combine color with current lifetime (Alpha)
            color_with_alpha = (*self.color, int(self.lifetime))
            
            pygame.draw.circle(target_surface, color_with_alpha, (self.radius, self.radius), self.radius)
            surface.blit(target_surface, (int(self.x - self.radius), int(self.y - self.radius)))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Stage 5: Fading & Cleanup")
    clock = pygame.time.Clock()
    
    particles = []
    running = True

    print("👉 STAGE 5: Fading added. Watch the 'Particles' count stay stable!")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            for _ in range(5):
                particles.append(Particle(mx, my))

        screen.fill(BG_COLOR)
        
        # <--- NEW: ITERATE BACKWARDS TO REMOVE DEAD PARTICLES
        # We use particles[:] to make a copy so we can modify the original list safely
        for p in particles[:]:
            p.move()
            if p.lifetime <= 0:
                particles.remove(p)
            else:
                p.draw(screen)

        font = pygame.font.SysFont("Arial", 14)
        text = font.render(f"Particles: {len(particles)}", True, (150, 150, 150))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()