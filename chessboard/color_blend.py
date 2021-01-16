# -*- coding: utf-8 -*-
"""
@Time    : 13/12/2020 10:08
@Author  : Colm Keyes
@Email   : keyesco@tcd.ie
@File    : color_blend.py
"""

import pygame
import time

class color_blend:

    def __init__(self, start_color, end_color, iterations=10):
        self.start_color = pygame.Color(start_color.r, start_color.g, start_color.b)
        self.current_color = pygame.Color(start_color.r, start_color.g, start_color.b)
        self.end_color = end_color
        self.i=0
        self.iterations = float(iterations)
        self.color_diff_overall = []

    @staticmethod
    def blend_colors(current_color, initial_color, final_color, amount):
        r_diff = (final_color.r - initial_color.r) * amount
        g_diff = (final_color.g - initial_color.g) * amount
        b_diff = (final_color.b - initial_color.b) * amount

        # Create and return new color
        return pygame.Color((int)(round(current_color.r + r_diff)),
                            (int)(round(current_color.g + g_diff)),
                            (int)(round(current_color.b + b_diff)))


    def get_next_color(self):

        if self.i ==0:
            self.color_diff_overall = abs(self.start_color[0] - self.end_color[0])

        # Calculate percentage done (0  <= pcnt_done <= 1)
        if self.end_color[0] < self.current_color[0]:
            pcnt_done = min(1.0, self.end_color[0]/(self.current_color[0] - (self.color_diff_overall / self.iterations)))
        elif self.end_color[0] > self.current_color[0]:
           pcnt_done = min(1.0, self.current_color[0] / (self.end_color[0] - (self.color_diff_overall / self.iterations)))

        # Store new color
        if pcnt_done < 1.0:
            self.current_color = color_blend.blend_colors(self.current_color ,self.start_color, self.end_color, pcnt_done/self.iterations) #, pcnt_done/2)

        elif pcnt_done >= 1.0:
            self.current_color = self.end_color

        self.i += 1
        time.sleep(0.1)
        return self.current_color


    def is_finished(self):
        return self.current_color == self.end_color
