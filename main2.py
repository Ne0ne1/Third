import pygame

# инициализация
pygame.init()
x1, y1 = 1280, 720 # размеры окна
screen = pygame.display.set_mode((x1, y1))
clock = pygame.time.Clock()
running = True
dt = 0
# определяет позицию шара по x и y, возвращает список
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) 
def drewcercle():
    pygame.draw.circle(screen, "red", player_pos, razmer)
razmer = 40 # размер круга
while running:
    # делает так чтоб можно было закрыть программу
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # делает фон и рисует круг
    screen.fill('Black')
    drewcercle()
    # print(player_pos.y)
    if player_pos.y <= -(razmer): # сделал так чтобы круг выходил за рамки, полностью прятался
        player_pos.y += y1 + razmer * 2
    if player_pos.y >= y1 + razmer:
        player_pos.y -= y1 + razmer * 2
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos.y >= -41:
        # print(player_pos.y)
        player_pos.y -= 300 * dt
    if keys[pygame.K_s] and player_pos.y <= 761:
        # print(player_pos.y)
        # if player_pos.y >= 760:
        #     player_pos.y -= 760
        player_pos.y += 300 * dt
    if keys[pygame.K_a] and player_pos.x >= 40:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d] and player_pos.x <= 1240:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()