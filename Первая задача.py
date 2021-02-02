import pygame
import requests

clock = pygame.time.Clock()

api_server = "http://static-maps.yandex.ru/1.x/"

print("Введите: ")
lon = input("Долготу: ")
lat = input("Широту: ")
delta = input("Приближение: ")
l = input("Тип: ")

params = {
    "ll": ",".join([lon, lat]),
    "spn": ",".join([delta, delta]),
    "l": l
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
