import pygame
import requests

clock = pygame.time.Clock()
c = 0
map_request = "https://static-maps.yandex.ru/1.x/?ll=42.588353%2C-58.006297&spn=1.0,1.5&l=sat"
resp = requests.get(map_request)
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
