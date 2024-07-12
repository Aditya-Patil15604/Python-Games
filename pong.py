import pygame

pygame.init()

screen = pygame.display.set_mode((300,300))
pygame.display.set_caption("pong remade")

time = pygame.time.Clock()
playery = 100
computery = 100
ballx = 150
bally = 150
font = pygame.font.Font('freesansbold.ttf', 20)
running = True
player_direction = 0
player_speed = 5
ball_x_direction = 1
ball_y_direction = -1
ball_x_speed = 2
ball_y_speed = 3
gameover = False

def check_gameover(ballx, gameover):
    if (ballx <= 0 or ballx >= 290) and gameover == False:
        gameover = True
    return gameover

def ball_movement(ball_x_direction, ball_y_direction, ballx, bally, ball_x_speed, ball_y_speed):
    if ball_x_direction == 1 and ballx < 290:
        ballx += ball_x_speed
    elif ball_x_direction == 1 and ballx >= 290:
        ball_x_direction *= -1
    if ball_x_direction == -1 and ballx > 0:
        ballx -= ball_x_speed
    elif ball_x_direction == -1 and ballx <= 0:
        ball_x_direction *= -1
    if ball_y_direction == 1 and bally < 290:
        bally += ball_y_speed
    elif ball_y_direction == 1 and bally >= 290:
        ball_y_direction *= -1
    if ball_y_direction == -1 and bally > 0:
        bally -= ball_y_speed
    elif ball_y_direction == -1 and bally <= 0:
        ball_y_direction *= -1

    return ball_x_direction, ball_y_direction, ballx, bally

def computer_movement(bally , computery):
    computerspeed = 3
    if (computery + 20) > (bally + 5):
        computery = computery - computerspeed
    elif (computery + 20) < (bally + 5):
        computery = computery + computerspeed
    return computery

def check_collisions(ball, player, computer, ball_x_direction):
    if ball.colliderect(player):
        ball_x_direction = 1
    if ball.colliderect(computer):
        ball_x_direction = -1

    return ball_x_direction

while running:
    time.tick(60)
    screen.fill("black")
    player = pygame.draw.rect(screen,"white",(5,playery,10,40))
    computer = pygame.draw.rect(screen,"white",(285,computery,10,40))
    ball = pygame.draw.rect(screen,"white",(ballx,bally,10,10))
    gameover = check_gameover(ballx, gameover)
    if not gameover:
        computery = computer_movement(bally, computery)
        ball_x_direction, ball_y_direction, ballx, bally = ball_movement(ball_x_direction, ball_y_direction, ballx, bally, ball_x_speed, ball_y_speed)
    ball_x_direction = check_collisions(ball, player, computer, ball_x_direction)

    if gameover:
        gameoverText = font.render('Game Over',True,'white','black')
        screen.blit(gameoverText,(80, 130))
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_direction = -1
            if event.key == pygame.K_s:
                player_direction = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_direction = 0
            if event.key == pygame.K_s:
                player_direction = 0
    
    playery = playery + (player_speed * player_direction)
    pygame.display.flip()

pygame.quit()
