import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FunCount")

# Background
dashboard = pygame.image.load("assets/dashboard.png").convert_alpha()
dashboard = pygame.transform.scale(dashboard, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Welcome image (di atas tombol)
welcome_img = pygame.image.load("assets/welcome.png").convert_alpha()

# Scale opsional (jika welcome terlalu besar)
welcome_scale_width = 500
welcome_ratio = welcome_scale_width / welcome_img.get_width()
welcome_img = pygame.transform.scale(
    welcome_img,
    (welcome_scale_width, int(welcome_img.get_height() * welcome_ratio))
)

welcome_rect = welcome_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 120))

# Button start
button_original = pygame.image.load("assets/button_start.png").convert_alpha()

SMALL_SIZE = (200, 100)   # ukuran awal (kecil)
BIG_SIZE = (300, 150)     # ukuran ketika hover

button_small = pygame.transform.scale(button_original, SMALL_SIZE)
button_big = pygame.transform.scale(button_original, BIG_SIZE)

button_image = button_small
button_rect = button_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button_rect.collidepoint(mouse_pos):
                    print("START clicked!")
                    # TODO: pindah ke scene berikutnya

    # Hover animation
    if button_rect.collidepoint(mouse_pos):
        button_image = button_big
    else:
        button_image = button_small

    # Keep it centered after resizing
    button_rect = button_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))

    # DRAWING
    screen.blit(dashboard, (0, 0))
    screen.blit(welcome_img, welcome_rect)
    screen.blit(button_image, button_rect)

    pygame.display.update()
