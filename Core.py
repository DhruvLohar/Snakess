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

import pygame
from pygame import freetype


def check_fruit(num):
    with open("static_media/select_fruit.txt", "w+") as f:
        f.truncate(0)
        f.write(str(num))


def check_mode(num):
    with open("static_media/game_mode.txt", "w+") as f:
        f.truncate(0)
        f.write(str(num))


class Button:
    def __init__(self, root, color, pos, para, text=""):
        self.root = root
        self.text_color = color[0]
        self.shadow_color = color[1]
        self.x_cord = pos[0]
        self.y_cord = pos[1]
        self.width = para[0]
        self.height = para[1]
        self.text = text

    def draw(self, outline=None):
        if outline:
            pygame.draw.rect(self.root, outline, (self.x_cord - 2, self.y_cord - 2, self.width + 4, self.height + 4), 0)

        if self.text != "":
            font = pygame.font.Font("static_media/font/Damion.ttf", 42)
            text = font.render(self.text, True, self.text_color)

            self.root.blit(text, (self.x_cord, self.y_cord))

    def is_over(self, pos):
        if self.x_cord < pos[0] < self.x_cord + self.width:
            if self.y_cord < pos[1] < self.y_cord + self.height:
                return True

        return False

    def add_shadow(self):
        font = pygame.font.Font("static_media/font/Damion.ttf", 42)
        text = font.render(self.text, True, self.text_color)
        shadow_text = font.render(self.text, True, self.shadow_color)

        shadow_x = self.x_cord + 3
        shadow_y = self.y_cord + 3

        self.root.blit(text, (self.x_cord, self.y_cord))
        self.root.blit(shadow_text, (shadow_x, shadow_y))
