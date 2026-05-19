import pygame
import asyncio
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eid-ul-Adha Mubarak")

clock = pygame.time.Clock()

# Colors
SKY = (10, 10, 40)
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)
GREEN = (20, 120, 40)

# Fonts
title_font = pygame.font.SysFont("georgia", 56, bold=True)
subtitle_font = pygame.font.SysFont("arial", 42, bold=True)

# Stars
stars = [
    (
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT // 2),
        random.randint(1, 3)
    )
    for _ in range(80)
]

# Animation
goat_x = -150
cloud_x = 0


def draw_goat(x, y):
    pygame.draw.ellipse(screen, (220, 220, 220), (x, y, 100, 50))
    pygame.draw.ellipse(screen, (240, 240, 240), (x - 30, y + 5, 40, 30))
    for lx in [x + 20, x + 40, x + 60, x + 80]:
        pygame.draw.rect(screen, (180, 180, 180), (lx, y + 45, 5, 20))


def draw_moon():
    pygame.draw.circle(screen, YELLOW, (650, 100), 40)
    pygame.draw.circle(screen, SKY, (665, 95), 35)


def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, (x, y, 120, 40))
    pygame.draw.ellipse(screen, WHITE, (x + 20, y - 15, 60, 50))


def draw_mosque():
    pygame.draw.rect(screen, (30, 30, 30), (250, 320, 300, 180))
    pygame.draw.circle(screen, (50, 50, 50), (400, 300), 60)


async def main():
    global goat_x, cloud_x

    running = True

    while running:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Background
        screen.fill(SKY)

        # Stars
        for x, y, r in stars:
            pygame.draw.circle(screen, WHITE, (x, y), r)

        # Moon
        draw_moon()

        # Clouds
        cloud_x -= 0.5
        if cloud_x < -150:
            cloud_x = WIDTH

        draw_cloud(cloud_x, 120)
        draw_cloud(cloud_x + 250, 170)

        # Mosque
        draw_mosque()

        # Ground
        pygame.draw.rect(screen, GREEN, (0, HEIGHT - 100, WIDTH, 100))

        # Goat
        goat_x += 2
        if goat_x > WIDTH + 100:
            goat_x = -150

        draw_goat(goat_x, HEIGHT - 150)

        # Text
        title = title_font.render("Eid-ul-Adha", True, YELLOW)
        subtitle = subtitle_font.render("Mubarak", True, WHITE)

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 420))
        screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, 490))

        pygame.display.flip()
        clock.tick(60)

        # REQUIRED FOR WEB
        await asyncio.sleep(0)

    pygame.quit()


asyncio.run(main())
