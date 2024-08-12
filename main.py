import pygame
import random
# import numpy as np

pygame.init()

# Параметры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра тир")
icon = pygame.image.load("img/5659_800.jpg")
pygame.display.set_icon(icon)

# Параметры мишени
target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = 0.2  # Начальная скорость по оси X
target_speed_y = 0.2  # Начальная скорость по оси Y

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Переменные для подсчета попаданий
hit_count = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # При попадании обновляем координаты мишени и увеличиваем счетчик попаданий
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                hit_count += 1
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                if target_x < 0: # Увеличиваем скорость по оси Y
                    target_speed_x -= 0.1
                else:
                    target_speed_x += 0.1
                if target_speed_y < 0: # Увеличиваем скорость по оси Y
                    target_speed_y -= 0.1
                else:
                    target_speed_y += 0.1


    # Перемещение мишени
    target_x += target_speed_x
    target_y += target_speed_y

    # Отскок от границ экрана
    if target_x <= 0 or target_x + target_width >= SCREEN_WIDTH:
        target_speed_x *= -1
    if target_y <= 0 or target_y + target_height >= SCREEN_HEIGHT:
        target_speed_y *= -1

    # Отрисовка
    screen.fill(color)
    screen.blit(target_img, (target_x, target_y))

    # Отображение количества попаданий
    hit_text = font.render(f"Попадания: {hit_count}, скорость по X {target_speed_x:.2f}, скорость по Y {target_speed_y:.2f}", True, (255, 255, 255))
    screen.blit(hit_text, (5, 5))

    pygame.display.update()

pygame.quit()
