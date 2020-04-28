"""
*Snakess*
! Game Made By Dhruv Lohar.
! Copyright will be claimed if done.
! Do not delete or modify any content or code.
! Do not delete files under static_media folder.
! Keep calm and enjoy the snakess.
! Completed at 28 April, 2020.
! Check out more projects at https://github.com/DhruvLohar
"""

from Core import Button
from Core import check_fruit, check_mode
import pygame
import random

pygame.init()
pygame.mixer.init()
pygame.font.init()

root_width = 600
root_height = 500
root = pygame.display.set_mode((root_width, root_height))
pygame.display.set_caption("Snakie")

lime = (252, 186, 0)
white = (255, 255, 255)
burgandy = (128, 0, 32)
red = (255, 0, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)

bgimg = pygame.image.load("static_media/images/menu_bg.jpg")
bgimg = pygame.transform.scale(bgimg, (root_width, root_height)).convert_alpha()

milk = pygame.image.load("static_media/images/milk.png")
milk = pygame.transform.scale(milk, (25, 25))

apple = pygame.image.load("static_media/images/apple.png")
apple = pygame.transform.scale(apple, (25, 25))

orange = pygame.image.load("static_media/images/orange.png")
orange = pygame.transform.scale(orange, (25, 25))

strawberry = pygame.image.load("static_media/images/strawberry.png")
strawberry = pygame.transform.scale(strawberry, (25, 25))

fruits = [apple, orange, strawberry, milk]

back_btn = Button(root, [black, white], [0, 0], [50, 50], "<")

button_click = pygame.mixer.Sound('static_media/sounds/click.wav')
eat = pygame.mixer.Sound('static_media/sounds/eat.wav')

snake_block = 20
velocity = 10

clock = pygame.time.Clock()


def text_screen(text, color, pos, size):
    font = pygame.font.Font("static_media/font/Damion.ttf", size)
    text = font.render(text, True, color)
    root.blit(text, (pos[0], pos[1]))


def set_mode():
    easy_btn = Button(root, [black, white], [50, 150], [200, 50], "Easy")
    mid_btn = Button(root, [black, white], [50, 220], [200, 50], "Moderate")
    hard_btn = Button(root, [black, white], [50, 290], [200, 50], "Extreme")

    easy, med, hard = False, False, False

    exit_set = False

    while not exit_set:
        root.blit(bgimg, (0, 0))

        back_btn.draw(lime)

        easy_btn.draw(lime)
        mid_btn.draw(lime)
        hard_btn.draw(lime)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                exit_set = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_btn.is_over(pos):
                    button_click.play()
                    check_mode(15)
                    easy, med, hard = True, False, False
                elif mid_btn.is_over(pos):
                    button_click.play()
                    check_mode(20)
                    easy, med, hard = False, True, False
                elif hard_btn.is_over(pos):
                    button_click.play()
                    check_mode(30)
                    easy, med, hard = False, False, True
                elif back_btn.is_over(pos):
                    button_click.play()
                    exit_set = True

            if event.type == pygame.MOUSEMOTION:
                if easy_btn.is_over(pos):
                    easy_btn.add_shadow()
                elif mid_btn.is_over(pos):
                    mid_btn.add_shadow()
                elif hard_btn.is_over(pos):
                    hard_btn.add_shadow()
                elif back_btn.is_over(pos):
                    back_btn.add_shadow()

        if easy:
            easy_btn.add_shadow()
        elif med:
            mid_btn.add_shadow()
        elif hard:
            hard_btn.add_shadow()

        pygame.display.update()
        clock.tick(20)


def set_food():
    apple_btn = Button(root, [black, white], [50, 140], [200, 50], "Apple")
    orange_btn = Button(root, [black, white], [50, 200], [200, 50], "Orange")
    strawberry_btn = Button(root, [black, white], [50, 260], [200, 50], "Strawberry")
    milk_btn = Button(root, [black, white], [50, 320], [200, 50], "Milk Can")

    exit_set = False

    apple, orange, strawberry, milk = False, False, False, False

    while not exit_set:
        root.blit(bgimg, (0, 0))

        back_btn.draw(lime)
        apple_btn.draw(lime)
        orange_btn.draw(lime)
        strawberry_btn.draw(lime)
        milk_btn.draw(lime)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                exit_set = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if apple_btn.is_over(pos):
                    button_click.play()
                    check_fruit(0)
                    apple, orange, strawberry, milk = True, False, False, False
                elif orange_btn.is_over(pos):
                    button_click.play()
                    check_fruit(1)
                    apple, orange, strawberry, milk = False, True, False, False
                elif strawberry_btn.is_over(pos):
                    button_click.play()
                    check_fruit(2)
                    apple, orange, strawberry, milk = False, False, True, False
                elif milk_btn.is_over(pos):
                    button_click.play()
                    check_fruit(3)
                    apple, orange, strawberry, milk = False, False, False, True
                elif back_btn.is_over(pos):
                    button_click.play()
                    exit_set = True

            if event.type == pygame.MOUSEMOTION:
                if apple_btn.is_over(pos):
                    apple_btn.add_shadow()
                elif orange_btn.is_over(pos):
                    orange_btn.add_shadow()
                elif strawberry_btn.is_over(pos):
                    strawberry_btn.add_shadow()
                elif milk_btn.is_over(pos):
                    milk_btn.add_shadow()
                elif back_btn.is_over(pos):
                    back_btn.add_shadow()

        if apple:
            apple_btn.add_shadow()
        elif orange:
            orange_btn.add_shadow()
        elif strawberry:
            strawberry_btn.add_shadow()
        elif milk:
            milk_btn.add_shadow()

        pygame.display.update()
        clock.tick(20)


def learn_more():
    exit_more = False
    img = pygame.image.load('static_media/images/about_bg.jpg')

    while not exit_more:
        root.fill(white)
        root.blit(img, (0, 0))
        back_btn.draw(lime)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                exit_more = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.is_over(pos):
                	exit_more = True
                	button_click.play()
                	back_btn.add_shadow()

        pygame.display.update()
        clock.tick(20)


def setting_menu():
    game_mode = Button(root, [black, white], [50, 150], [200, 40], "Game Mode")
    select_food = Button(root, [black, white], [50, 220], [200, 40], "Select Fruit")
    about_btn = Button(root, [black, white], [50, 290], [200, 40], "About Us")

    exit_setting = False

    while not exit_setting:
        root.fill(black)
        root.blit(bgimg, (0, 0))

        back_btn.draw(lime)
        select_food.draw(lime)
        game_mode.draw(lime)
        about_btn.draw(lime)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                exit_setting = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if select_food.is_over(pos):
                    button_click.play()
                    set_food()
                elif game_mode.is_over(pos):
                    button_click.play()
                    set_mode()
                elif about_btn.is_over(pos):
                    button_click.play()
                    learn_more()
                elif back_btn.is_over(pos):
                    button_click.play()
                    exit_setting = True

            if event.type == pygame.MOUSEMOTION:
                if select_food.is_over(pos):
                    select_food.add_shadow()
                elif game_mode.is_over(pos):
                    game_mode.add_shadow()
                elif about_btn.is_over(pos):
                    about_btn.add_shadow()
                elif back_btn.is_over(pos):
                    back_btn.add_shadow()

        pygame.display.update()
        clock.tick(20)


def score_menu():
    reset_btn = Button(root, [black, white], [50, 400], [100, 50], "Reset")

    with open("static_media/score.txt", "r") as file:
        hi_score = file.read()

    exit_score = False

    while not exit_score:
        root.fill(black)
        root.blit(bgimg, (0, 0))

        back_btn.draw(lime)
        reset_btn.draw(lime)

        text_screen(str(hi_score), white, [54, 134], 100)
        text_screen(str(hi_score), burgandy, [50, 130], 100)
        text_screen("All Time Best", white, [53, 253], 40)
        text_screen("All Time Best", black, [50, 250], 40)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                exit_score = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.is_over(pos):
                    button_click.play()
                    exit_score = True
                if reset_btn.is_over(pos):
                    button_click.play()
                    with open("static_media/score.txt", "w") as file:
                        file.write("0")

            if event.type == pygame.MOUSEMOTION:
                if back_btn.is_over(pos):
                    back_btn.add_shadow()
                if reset_btn.is_over(pos):
                    reset_btn.add_shadow()

        pygame.display.update()
        clock.tick(20)


def main_menu():
    pygame.mixer.music.load("static_media/sounds/main_bg.mp3")
    pygame.mixer.music.play(-1)

    play_btn = Button(root, [black, white], [325, 50], [250, 40], "Start Game")
    score_btn = Button(root, [black, white], [325, 120], [250, 40], "Score Board")
    settings_btn = Button(root, [black, white], [325, 190], [250, 40], "Settings")
    exit_btn = Button(root, [black, white], [325, 260], [250, 40], "Exit")

    img = pygame.image.load('static_media/images/main_menu.jpg')
    img = pygame.transform.scale(img, (root_width, root_height))

    exit_game = False

    while not exit_game:
        root.blit(img, (0, 0))

        play_btn.draw(lime)
        score_btn.draw(lime)
        settings_btn.draw(lime)
        exit_btn.draw(lime)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                if play_btn.is_over(pos):
                    play_btn.add_shadow()
                elif score_btn.is_over(pos):
                    score_btn.add_shadow()
                elif settings_btn.is_over(pos):
                    settings_btn.add_shadow()
                elif exit_btn.is_over(pos):
                    exit_btn.add_shadow()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.is_over(pos):
                    button_click.play()
                    game_loop()
                elif score_btn.is_over(pos):
                    button_click.play()
                    score_menu()
                elif settings_btn.is_over(pos):
                    button_click.play()
                    setting_menu()
                elif exit_btn.is_over(pos):
                    button_click.play()
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(20)


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.circle(root, white, [(x[0] + 3), (x[1] + 3)], 10)
        pygame.draw.circle(root, burgandy, [x[0], x[1]], 10)


def game_loop():

    game_over = False
    game_close = False

    cur_score = 0
    with open("static_media/score.txt", "r") as file:
        hiscore = file.read()

    x1 = root_width / 2
    y1 = root_height / 2

    x1_change = 0
    y1_change = 0

    food_x = round(random.randrange(0, root_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, root_height - 50) / 10.0) * 10.0

    game_img = pygame.image.load('static_media/images/game_bg.jpg').convert()

    snake_list = []
    length_of_snake = 1

    while not game_over:
        while game_close:
            root.fill(black)
            img = pygame.image.load('static_media/images/game_over_bg.jpg')
            root.blit(img, (0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        main_menu()
                        game_close = False
                        game_over = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if __name__ == '__main__':
                    if event.key == pygame.K_LEFT:
                        x1_change = -velocity
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = velocity
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        x1_change = 0
                        y1_change = -velocity
                    elif event.key == pygame.K_DOWN:
                        x1_change = 0
                        y1_change = velocity

        if x1 >= root_width or x1 < 0 or y1 >= root_height or y1 < 0:
            pygame.mixer.music.load("static_media/sounds/GameOver.mp3")
            pygame.mixer.music.play()
            game_close = True

        x1 += x1_change
        y1 += y1_change

        root.fill(black)
        root.blit(game_img, (0, 0))
        with open("static_media/select_fruit.txt", "r") as f:
            food = f.read()
        root.blit(fruits[int(food)], (food_x, food_y))

        snake_head = [int(x1), int(y1)]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:  # If snake hits itself
                pygame.mixer.music.load("static_media/sounds/GameOver.mp3")
                pygame.mixer.music.play()
                game_close = True

        our_snake(snake_block, snake_list)
        text_screen(str(cur_score), white, [8, 0], 60)
        text_screen(str(cur_score), burgandy, [5, 0], 60)

        if food_x < x1 < (food_x + 30) and food_y < y1 < (food_y + 30):
            eat.play()
            food_x = round(random.randrange(0, root_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, root_height - 60) / 10.0) * 10.0
            cur_score += 10
            length_of_snake += 2
            if cur_score > int(hiscore):
                with open("static_media/score.txt", "w") as file:
                    file.write(str(cur_score))

        pygame.display.update()
        with open('static_media/game_mode.txt', 'r') as f:
            FPS = f.read()
        clock.tick(int(FPS))

    pygame.quit()
    quit()


if __name__ == '__main__':
    main_menu()
