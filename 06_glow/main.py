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
LIFETIME_DECAY = 4

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
        
        self.lifetime = 255

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
        
        self.lifetime -= LIFETIME_DECAY

    def draw(self, surface):
        if self.lifetime > 0:
            target_surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
            color_with_alpha = (*self.color, int(self.lifetime))
            pygame.draw.circle(target_surface, color_with_alpha, (self.radius, self.radius), self.radius)
            
            # <--- NEW: THE GLOW MAGIC
            # BLEND_ADD adds the color values together.
            # Red + Red = Bright Red. Bright Red + Bright Red = White.
            surface.blit(target_surface, 
                         (int(self.x - self.radius), int(self.y - self.radius)), 
                         special_flags=pygame.BLEND_ADD)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Stage 6: Final Glow")
    clock = pygame.time.Clock()
    
    particles = []
    running = True

    print("👉 STAGE 6: Glow added. Overlapping particles now burn bright!")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            for _ in range(5):
                particles.append(Particle(mx, my))

        screen.fill(BG_COLOR)
        
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