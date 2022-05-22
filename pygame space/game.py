import pygame
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render('Score:'+ str(int(current_time/1000)), True,(64,64,64))
    score_rect = score_surf.get_rect(topleft = (20,10))
    screen.blit(score_surf, score_rect)
    

pygame.init()
screen = pygame.display.set_mode((800,468))
pygame.display.set_caption("sprinter")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font\Pixeltype.ttf", 30)
game_active = True
start_time = 0


sky_surface = pygame.image.load("2824536_1.png").convert()
text_surf_open = test_font.render("Game Over",False, 'White')
text_rect_open = text_surf_open.get_rect(center = (390,50))
text_surf_open_1 = test_font.render("Press ESCAPE KEY to Restart",False, 'White')
text_rect_open_1 = text_surf_open_1.get_rect(center = (390,100))


snail_surface = pygame.image.load("asteroid.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (700,400)) 

player_surf = pygame.image.load("player.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,320))
player_gravity = -10


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -10
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_gravity = -10
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_active = True
                snail_rect.left = 800
                start_time = pygame.time.get_ticks()
                
    if game_active:            
        screen.blit(sky_surface, (0,0))   
        pygame.draw.rect(screen, "lightblue", pygame.Rect(0,0,800,25))
        pygame.draw.line(screen, 'Black', (0,25), (800,25),2)
        snail_rect.x  -= 5
        if snail_rect.right <= 0:
            snail_rect.left = 800
          #  scr = str(int(scr)+1)
        screen.blit(snail_surface, snail_rect)
#        text_surface_2 = test_font.render(scr, False, 'Black' )
   #     screen.blit(text_surface_2, text_rect_2) 
        display_score()
        
        
        player_gravity += 0.5
        player_rect.y += player_gravity
        if player_rect.bottom >= 468: player_rect.bottom = 468
        screen.blit(player_surf, player_rect)
        if player_rect.bottom <= 0: 
            player_rect.bottom = 300
        
        if snail_rect.colliderect(player_rect):
            game_active = False
    
    else:
        screen.blit(sky_surface, (0,0)) 
        screen.blit(text_surf_open, text_rect_open)
        screen.blit(text_surf_open_1, text_rect_open_1) 
        
        
        
    
 #   keys = pygame.key.get_pressed()
  #  if keys[pygame.K_SPACE]:
        
    
#    mouse_pos = pygame.mouse.get_pos()
    
 #   if player_rect.collidepoint(mouse_pos):
  #      print(pygame.mouse.get_pressed())
    
    
    
    
    pygame.display.update()
    clock.tick(60)
