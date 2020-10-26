import pygame
from pygame import mixer
pygame.init()

white = (255, 255, 255)

X = 400
Y = 400
clock = pygame.time.Clock()
clocl.tick(30)
display_surface = pygame.display.set_mode((X, Y ))
pygame.display.set_caption('Image')
image = pygame.image.load(r'theme.png')
image1 = pygame.transform.scale(image, (400, 400))
mixer.init()
mixer.music.load("welcome.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()
while True :
	display_surface.fill(white)
	display_surface.blit(image1, (0, 0))

    import pygame_image
pygame.quit()
