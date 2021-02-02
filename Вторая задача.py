import pygame
import requests
import os

clock = pygame.time.Clock()
c = 0
map_request = "https://static-maps.yandex.ru/1.x/"
lon = '42.588353'
lat = '58.006297'
delta = '1.0'
l = 'sat'
# lon, lat, delta = input(), input(), input()
# ?ll=42.588353%2C-58.006297&spn=1.0,1.5&l=sat
params = {
    "ll": ",".join([lon, lat]),
    "spn": ",".join([delta, delta]),
    "l": l
}
resp = requests.get(map_request, params=params)
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(resp.content)

pygame.init()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(1)
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
os.remove(map_file)
pygame.quit()