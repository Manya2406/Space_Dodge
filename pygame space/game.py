import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,468))
pygame.display.set_caption("sprinter")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font\Pixeltype.ttf", 30)

scr = '0'

sky_surface = pygame.image.load("2824536_1.png").convert()
text_surface_1 = test_font.render('Score:', False, 'Black' )
text_rect_1 = text_surface_1.get_rect(topleft = (20,10))
text_surface_2 = test_font.render(scr, False, 'Black' )
text_rect_2 = text_surface_2.get_rect(topleft = (90,10))

snail_surface = pygame.image.load("asteroid.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (700,380))

player_surf = pygame.image.load("player.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,320))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
 #       if event.type == pygame.MOUSEMOTION:
#            print(event.pos)
    screen.blit(sky_surface, (0,0))   
    pygame.draw.rect(screen, "lightblue", pygame.Rect(0,0,800,25))
    pygame.draw.line(screen, 'Black', (0,25), (800,25),2)
    screen.blit(text_surface_1, text_rect_1) 
    snail_rect.x  -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
        scr = str(int(scr)+1)
    screen.blit(snail_surface, snail_rect)
    text_surface_2 = test_font.render(scr, False, 'Black' )
    screen.blit(text_surface_2, text_rect_2) 
    screen.blit(player_surf, player_rect)
    
#    mouse_pos = pygame.mouse.get_pos()
    
 #   if player_rect.collidepoint(mouse_pos):
  #      print(pygame.mouse.get_pressed())
    
    
    
    
    pygame.display.update()
    clock.tick(60)
