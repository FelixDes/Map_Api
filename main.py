import pygame
import requests

clock = pygame.time.Clock()

api_server = "http://static-maps.yandex.ru/1.x/"

lon = "35.511387"
lat = "48.709887"
delta = "0.004"

params = {
    "ll": ",".join([lon, lat]),
    "spn": ",".join([delta, delta]),
    "l": "map"
}
resp = requests.get(api_server, params=params)
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(resp.content)

pygame.init()

while pygame.event.wait().type != pygame.QUIT:
    clock.tick(1)
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
pygame.quit()
