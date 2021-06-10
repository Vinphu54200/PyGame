import pygame
pygame.init()
screen = pygame.display.set_mode((600,300))
pygame.display.set_caption('Dinosaur')
WHITE=(255,255,255)
RED=(255,0,0)
BLACK=(0,0,0)
background_x=0
background_y=0
dinosaur_x=0
dinosaur_y=230
tree_x=550
tree_y=235
x_velocity=9.5
y_velocity= 7
score = 0
highscore = 0
font = pygame.font.SysFont('san',20)
font1 = pygame.font.SysFont('san',40)
background=pygame.image.load(r'E:\Study\Python\dinosaur\background.jpg')
dinosaur=pygame.image.load(r'E:\Study\Python\dinosaur\dinosaur.png')
tree=pygame.image.load(r'E:\Study\Python\dinosaur\tree.png')
sound1=pygame.mixer.Sound(r'E:\Study\Python\dinosaur\tick.wav')
sound2=pygame.mixer.Sound(r'E:\Study\Python\dinosaur\te.wav')
clock = pygame.time.Clock()
running = True
jump =False
pausing = False
while running:
    clock.tick(60)
    screen.fill(WHITE)
    background1_rect=screen.blit(background,(background_x,background_y))
    background2_rect=screen.blit(background,(background_x+600,background_y))
    score_txt=font.render("Score: "+str(score),True,BLACK)
    screen.blit(score_txt,(5,5))
    highscore_txt=font.render("High Score: "+str(highscore),True,RED)
    screen.blit(highscore_txt,(5,20))
    background_x -= x_velocity
    if background_x+600<=0:
        background_x =0
    tree_x -= x_velocity
    if tree_x <= -20:
        tree_x = 550
        score+=1
    if 230 >=dinosaur_y>= 80:
        if jump ==True:
            dinosaur_y-=y_velocity
    else:
        jump =False
    if dinosaur_y<230:
        if jump == False:
            dinosaur_y+=y_velocity
    dinosaur_rect=screen.blit(dinosaur,(dinosaur_x,dinosaur_y))
    tree_rect=screen.blit(tree,(tree_x,tree_y))
    if dinosaur_rect.colliderect(tree_rect):
        pausing = True
        gameover_txt=font1.render("GAME OVER",True,RED)
        gamescore_txt=font.render("Your score: "+str(score),True,RED)
        screen.blit(gameover_txt,(200,150))
        screen.blit(gamescore_txt,(250,180))
        x_velocity=0
        y_velocity=0
        if score >= highscore:
            highscore = score
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if dinosaur_y == 230:
                    pygame.mixer.Sound.play(sound1)
                    jump = True
                if pausing:
                    background_x=0
                    background_y=0
                    dinosaur_x=0
                    dinosaur_y=230
                    tree_x=550
                    tree_y=235
                    x_velocity=9.5
                    y_velocity=7
                    score = 0
                    pausing = False
    pygame.display.flip()
pygame.quit()
