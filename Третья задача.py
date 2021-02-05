import os

import pygame
import requests

clock = pygame.time.Clock()
map_request = "https://static-maps.yandex.ru/1.x/"
map_file = "map.png"
print("Введите: ")
lon = float(input("Долготу: "))
lat = float(input("Широту: "))
delta = float(input("Приближение: "))
l = input("Тип: ")
# lon, lat, delta = input(), input(), input()
# ?ll=42.588353%2C-58.006297&spn=1.0,1.5&l=sat
a = ''
def new_image():
    global map_file, a
    params = {
        "ll": ",".join([str(lon), str(lat)]),
        "spn": ",".join([str(delta), str(delta)]),
        "l": l
    }
    resp = requests.get(map_request, params=params)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        if a != resp.content:
            a = resp.content
        file.write(resp.content)
    file.close()


new_image()
pygame.init()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                if delta <= 10:
                    delta -= 10
                else:
                    delta -= delta / 2
                if delta < 0.001:
                    delta = 0.001
                new_image()
            elif event.key == pygame.K_PAGEDOWN:
                if delta <= 10:
                    delta += delta
                else:
                    delta += 10
                if delta > 90:
                    delta = 90.0
                new_image()


            elif event.key == pygame.K_RIGHT:
                lon += delta * 2
                if lon > 180:
                    lon -= delta * 2
                new_image()
            elif event.key == pygame.K_LEFT:
                lon -= delta * 2
                if lon < -180:
                    lon += delta * 2
                new_image()
            elif event.key == pygame.K_UP:
                lat += delta * 2
                if lat > 90:
                    lat -= delta * 2
                new_image()
            elif event.key == pygame.K_DOWN:
                lat -= delta * 2
                if lat < -90:
                    lat += delta * 2
                new_image()
    clock.tick(1)
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))

    pygame.display.flip()
os.remove(map_file)
pygame.quit()
