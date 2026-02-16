import pygame
import time

pygame.init()

menu = True

currentLevel = 0
global hitcounter
global text
text = pygame.font.SysFont('stencil', 30, 0, 1)


# -------------- menu ------------------
def menu():
    menuBg = pygame.image.load('images/menu_pong_BG.png')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((360, 540))
    pygame.display.set_caption("BasketPong -> Main Menu")
    # clickable play text
    play_text = text.render("Play (click)", 1, 'yellow')
    play_rect = play_text.get_rect(center=(180, 480))

    running = True
    while running:
        clock.tick(230)
        keys = pygame.key.get_pressed()

        screen.blit(menuBg, (0, 0))
        screen.blit(play_text, play_rect.topleft)

        if keys[pygame.K_p]:
            running = False
            gamemode()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_rect.collidepoint(event.pos):
                    running = False
                    gamemode()

        pygame.display.update()

def transition():
    bg = pygame.image.load('images/pong_BG.png')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((360, 540))
    pygame.display.set_caption("BasketPong")
    lev = pygame.font.SysFont('stencil', 36,0,1)
    dif = pygame.font.SysFont('stencil', 40,0,1 )

    running = True
    while running:
        clock.tick(230)
        keys = pygame.key.get_pressed()
        pongLogo = pygame.image.load('images/pong_logo.png')

        screen.blit(pongLogo, (0, 0))
        if currentLevel == 0:
            l1 = lev.render("Level 1", 1, 'yellow')
            screen.blit(l1, (115, 350))
            d1 = dif.render("Easy", 1, 'yellow')
            screen.blit(d1, (130,400))
        elif currentLevel == 1:
            l1 = lev.render("Level 2", 1, 'yellow')
            screen.blit(l1, (115, 350))
            d1 = dif.render("Medium", 1, 'yellow')
            screen.blit(d1, (98,400))
            br = lev.render('Be ready',1, 'yellow')
            screen.blit(br, (93, 450))
        elif currentLevel == 2:
            l1 = lev.render("Level 3", 1, 'yellow')
            screen.blit(l1, (115, 350))
            d1 = dif.render("hard", 1, 'yellow')
            screen.blit(d1, (130,400))
            br = lev.render('Be ready', 1, 'yellow')
            screen.blit(br, (93, 450))
        pygame.display.update()

        time.sleep(5)

        if currentLevel == 0:
            level1()
        elif currentLevel == 1:
            level2()
        elif currentLevel == 2:
            level3()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

def gamemode():
    menuBg = pygame.image.load('images/pong_gamemods.png')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((360, 540))
    pygame.display.set_caption("BasketPong -> Game Modes")



    running = True
    while running:
        clock.tick(230)
        keys = pygame.key.get_pressed()

        screen.blit(menuBg, (0, 0))

        if keys[pygame.K_1]:
            running = False
            levelDescription()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

def levelDescription():
    menuBg = pygame.image.load('images/pong_level_descrip.png')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((360, 540))
    pygame.display.set_caption("BasketPong -> Game Modes")

    running = True
    while running:
        clock.tick(230)
        keys = pygame.key.get_pressed()

        screen.blit(menuBg, (0, 0))

        if keys[pygame.K_s]:
            running = False
            transition()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


def win():
    winBg = pygame.image.load('images/win.png')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((360, 540))
    pygame.display.set_caption("BasketPong -> Win")

    running = True
    while running:
        clock.tick(230)
        keys = pygame.key.get_pressed()

        screen.blit(winBg , (0, 0))

        if keys[pygame.K_m]:
            running = False
            menu()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

def lose():
    loseBg = pygame.image.load('images/lose.png')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((360, 540))
    pygame.display.set_caption("BasketPong -> Lose")

    running = True
    while running:
        clock.tick(230)
        keys = pygame.key.get_pressed()

        screen.blit(loseBg, (0, 0))

        if keys[pygame.K_m]:
            running = False
            menu()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

# -------------------- first level --------------------
def level1():
    global currentLevel
    currentLevel = 1
    hitcounter = 0
    clock = pygame.time.Clock()  # creating clock for tick
    screen = pygame.display.set_mode((360, 540))  # display / screen
    pygame.display.set_caption("BasketPong -> Level 1 ")

    bg = pygame.image.load('images/pong_BG.png')  # <-------bg of the game
    ball = pygame.image.load('images/ball.png')  # ball image
    ball = pygame.transform.scale(ball, (20, 20))

    player = pygame.Surface((100, 22))  # player
    player.fill('yellow')

    bot = pygame.Surface((100, 22))  # bot
    bot.fill('yellow')

    hit = text.render(f"Hits: {hitcounter}", 1, 'yellow')

    playerPos = 130  # initial values
    botPos = 130
    xBallPos = 167
    yBallPos = 255
    yMove = 1
    xMove = -0.4

    running = True
    while running:
        clock.tick(250)
        keys = pygame.key.get_pressed()

        screen.blit(bg, (0, 0))

        if playerPos - 25 <= xBallPos <= playerPos + 115 and yBallPos >= 477:
            yMove *= -1
            hitcounter += 1

            hit = text.render(f"Hits: {hitcounter}", 1, 'yellow')

            # ball trajectory
            if xBallPos - playerPos < 7 or 93 <= xBallPos - playerPos:
                xMove *= 1.4
            elif 5 <= xBallPos - playerPos < 15 or 85 <= xBallPos - playerPos < 95:
                xMove *= 1.3
            elif 15 <= xBallPos - playerPos < 25 or 75 <= xBallPos - playerPos < 85:
                xMove *= 1.2
            elif 25 <= xBallPos - playerPos < 30 or 65 <= xBallPos - playerPos < 75:
                    xMove *= 1.0
            elif 30 <= xBallPos - playerPos < 35 or 60 <= xBallPos - playerPos < 65:
                xMove *= 0.8
            elif 35 <= xBallPos - playerPos < 40 or 61 < xBallPos - playerPos < 70:
                xMove *= 0.6

            elif 40 <= xBallPos - playerPos <= 60:
                xMove = xMove  # <----------

            if xMove > 6:
                xMove = 6
            if xMove < -6:
                xMove = -6
            if 0 < abs(xMove) < 0.2:
                xMove = 0.2 if xMove > 0 else -0.2

        if botPos - 25 <= xBallPos <= botPos + 120 and yBallPos <= 56:
            yMove *= -1
            hitcounter += 1
            hit = text.render(f"Hits: {hitcounter}", 1, 'yellow')

        # movements
        yBallPos += yMove
        xBallPos += xMove

        if xBallPos < -3:
            xMove *= -1

        if xBallPos > 350:
            xMove *= -1

        # button press
        if keys[pygame.K_LEFT] and playerPos > 0:
            playerPos -= 1.2
        if keys[pygame.K_RIGHT] and playerPos < 260:
            playerPos += 1.2

        # win or lose
        if yBallPos > 570:
            currentLevel = 0
            pygame.display.update()
            time.sleep(1)
            lose()
        elif yBallPos < -20:
            pygame.display.update()
            time.sleep(1)
            transition()

        # bot movement
        if xBallPos < botPos:
            botPos -= 0.7
        elif xBallPos > botPos:
            botPos += 0.7

        screen.blit(player, (playerPos, 495))  # <------- player pos

        screen.blit(bot, (botPos, 35))  # <------- bot pos
        screen.blit(ball, (xBallPos, yBallPos))  # <------- ball pos

        hit = text.render(f"Hits: {hitcounter}", 1, 'yellow')
        screen.blit(hit, (10, 10))  # <------- hit counter

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


# --------------------- Second level ------------------------
def level2():
    global currentLevel
    currentLevel = 2
    hitcounter = 0
    clock = pygame.time.Clock()  # creating clock for tick
    screen = pygame.display.set_mode((360, 540))  # display / screen
    pygame.display.set_caption("BasketPong -> Level 2 ")

    bg = pygame.image.load('images/pong_BG.png')  # <-------bg of the game
    ball = pygame.image.load('images/ball.png')  # ball image
    ball = pygame.transform.scale(ball, (20, 20))

    player = pygame.Surface((100, 22))  # player
    player.fill('yellow')

    bot = pygame.Surface((100, 22))  # bot
    bot.fill('yellow')

    hit = text.render(f"Hits: {hitcounter}", 1, 'yellow')

    playerPos = 130  # initial values
    botPos = 130
    xBallPos = 167
    yBallPos = 255
    yMove = 1
    xMove = 0.5

    running = True
    while running:
        clock.tick(270)
        keys = pygame.key.get_pressed()

        screen.blit(bg, (0, 0))


        if playerPos - 25 <= xBallPos <= playerPos + 115 and yBallPos >= 477:
            yMove *= -1
            hitcounter += 1
            hit = text.render(f"Hits: {hitcounter}", 1, 'yellow')

            # ball trajectory
            if xBallPos - playerPos < 7 or 93 <= xBallPos - playerPos:
                xMove *= 1.4
            elif 5 <= xBallPos - playerPos < 15 or 85 <= xBallPos - playerPos < 95:
                xMove *= 1.3
            elif 15 <= xBallPos - playerPos < 25 or 75 <= xBallPos - playerPos < 85:
                xMove *= 1.2
            elif 25 <= xBallPos - playerPos < 30 or 65 <= xBallPos - playerPos < 75:
                xMove *= 1.0
            elif 30 <= xBallPos - playerPos < 35 or 60 <= xBallPos - playerPos < 65:
                xMove *= 0.8
            elif 35 <= xBallPos - playerPos < 40 or 61 < xBallPos - playerPos < 70:
                xMove *= 0.6
            elif 40 <= xBallPos - playerPos <= 60:
                xMove = xMove  # <----------
            # clamp horizontal speed
            if xMove > 6:
                xMove = 6
            if xMove < -6:
                xMove = -6
            if 0 < abs(xMove) < 0.2:
                xMove = 0.2 if xMove > 0 else -0.2


        if botPos - 25 <= xBallPos <= botPos + 120 and yBallPos <= 56:
            yMove *= -1
            hitcounter += 1
            hit = text.render(f"Hits: {hitcounter}", 1, 'yellow')

        # movements
        yBallPos += yMove
        xBallPos += xMove

        if xBallPos < -3:
            xMove *= -1

        if xBallPos > 350:
            xMove *= -1

        # button press
        if keys[pygame.K_LEFT] and playerPos > 0:
            playerPos -= 1.2
        if keys[pygame.K_RIGHT] and playerPos < 260:
            playerPos += 1.2

        # win or lose
        if yBallPos > 570:
            currentLevel = 0
            pygame.display.update()
            time.sleep(1)
            lose()
        elif yBallPos < -20:
            pygame.display.update()
            time.sleep(1)
            transition()

        # bot movement
        if xBallPos < botPos:
            botPos -= 1
        elif xBallPos > botPos:
            botPos += 1

        screen.blit(player, (playerPos, 495))  # <------- player pos

        screen.blit(bot, (botPos, 35))  # <------- bot pos
        screen.blit(ball, (xBallPos, yBallPos))  # <------- ball pos

        hit = text.render(f"Hits: {hitcounter}", 1, 'yellow')
        screen.blit(hit, (10, 10))  # <------- hit counter

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


# --------------------- THIRD LEVEL ------------------------
def level3():
    clock = pygame.time.Clock()  # creating clock for tick
    screen = pygame.display.set_mode((360, 540))  # display / screen
    hitcounter = 0
    pygame.display.set_caption("BasketPong -> Level 3 ")

    bg = pygame.image.load('images/pong_BG.png')  # <-------bg of the game
    ball = pygame.image.load('images/ball.png')  # ball image
    ball = pygame.transform.scale(ball, (20, 20))

    player = pygame.Surface((100, 22))  # player
    player.fill('yellow')

    bot = pygame.Surface((100, 22))  # bot
    bot.fill('yellow')

    hit = text.render(f"Hits: {hitcounter}", 1, 'yellow')   

    playerPos = 130  # initial values
    botPos = 130
    xBallPos = 167
    yBallPos = 255
    yMove = 1
    xMove = 0.6

    running = True
    while running:
        global currentLevel

        clock.tick(300)
        keys = pygame.key.get_pressed()

        screen.blit(bg, (0, 0))


        if playerPos - 25 <= xBallPos <= playerPos + 115 and yBallPos >= 477:
            yMove *= -1
            hitcounter += 1
            hit = text.render(f"Hits: {hitcounter}", 1, 'yellow')

            # ball trajectory 
            if xBallPos - playerPos < 7 or 93 <= xBallPos - playerPos:
                xMove *= 1.4
            elif 5 <= xBallPos - playerPos < 15 or 85 <= xBallPos - playerPos < 95:
                xMove *= 1.3
            elif 15 <= xBallPos - playerPos < 25 or 75 <= xBallPos - playerPos < 85:
                xMove *= 1.2
            elif 25 <= xBallPos - playerPos < 30 or 65 <= xBallPos - playerPos < 75:
                xMove *= 1.0
            elif 30 <= xBallPos - playerPos < 35 or 60 <= xBallPos - playerPos < 65:
                xMove *= 0.8
            elif 35 <= xBallPos - playerPos < 40 or 61 < xBallPos - playerPos < 70:
                xMove *= 0.6
            elif 40 <= xBallPos - playerPos <= 60:
                xMove = xMove  # <----------
            # clamp horizontal speed
            if xMove > 6:
                xMove = 6
            if xMove < -6:
                xMove = -6
            if 0 < abs(xMove) < 0.2:
                xMove = 0.2 if xMove > 0 else -0.2


        if botPos - 25 <= xBallPos <= botPos + 120 and yBallPos <= 56:
            yMove *= -1
            hitcounter += 1
            hit = text.render(f"Hits: {hitcounter}", 1, 'yellow')

        # movements
        yBallPos += yMove
        xBallPos += xMove

        if xBallPos < -3:
            xMove *= -1

        if xBallPos > 350:
            xMove *= -1

        # button press
        if keys[pygame.K_LEFT] and playerPos > 0:
            playerPos -= 1.2
        if keys[pygame.K_RIGHT] and playerPos < 260:
            playerPos += 1.2

        # win or lose
        if yBallPos > 570:
            currentLevel = 0
            pygame.display.update()
            time.sleep(1)
            lose()
        elif yBallPos < -20:
            currentLevel = 0
            pygame.display.update()
            time.sleep(1)
            win()

        # bot movement
        if xBallPos < botPos:
            botPos -= 1.43
        elif xBallPos > botPos:
            botPos += 1.43

        screen.blit(player, (playerPos, 495))  # <------- player pos

        screen.blit(bot, (botPos, 35))  # <------- bot pos
        screen.blit(ball, (xBallPos, yBallPos))  # <------- ball pos
        # refresh hit text each frame
        hit = text.render(f"Hits: {hitcounter}", 1, 'yellow')
        screen.blit(hit, (10, 10))  # <------- hit counter

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


menu()
