import pygame
import requests
import os

clock = pygame.time.Clock()
c = 0
map_request = "https://static-maps.yandex.ru/1.x/"
lon = '40'
lat = '40'
delta = '10'
l = 'sat'
# lon, lat, delta = input(), input(), input()
# ?ll=42.588353%2C-58.006297&spn=1.0,1.5&l=sat
map_file = "map.png"
def update():
    print(lon, lat)
    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": l
    }
    resp = requests.get(map_request, params=params)
    with open(map_file, "wb") as file:
        file.write(resp.content)
update()

pygame.init()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lon = str(int(lon) - int(delta) * 2)
                update()
            elif event.key == pygame.K_RIGHT:
                lon = str(int(lon) + int(delta) * 2)
                update()
            elif event.key == pygame.K_DOWN:
                lat = str(int(lat) - int(delta) * 2)
                update()
            elif event.key == pygame.K_UP:
                lat = str(int(lat) + int(delta) * 2)
                update()
    clock.tick(1)
    screen = pygame.display.set_mode((400, 400))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
os.remove(map_file)
pygame.quit()