import pygame
import random
import math

class Magnet_Power_Up():
    def __init__(self, master, xy):
        self.master = master
        self.sprite = self.master.sprites.power_up['XP_Magnet']

        self.x = xy[0]
        self.y = xy[1]

        self.phase = 1
        self.worble = [random.randint(0,9),0.1]

        self.phase_ticks = 15
        self.life = 1

        self.vector = (random.random()*2-1, random.random()*2-1)

    def logic(self):
        self.target = (self.master.PLAYER.x, self.master.PLAYER.y)
        target_vector = (0, 0)

        x_dif = self.target[0] - self.x
        y_dif = self.target[1] - self.y

        total_dif = abs(x_dif) + abs(y_dif)
        distance = math.sqrt(abs(x_dif)**2 + abs(y_dif)**2)

        if distance <= self.master.PLAYER.absorb_range:
            self.speed = 6
            self.phase = 2
        else:
            if self.phase == 1:
                self.speed = 0
                self.worble[0] += self.worble[1]
                self.y += self.worble[1]
                if self.worble[0] > 10:
                    self.worble[1] = -0.1
                elif self.worble[0] < 1:
                    self.worble[1] = 0.1

        x_proportion = x_dif / total_dif
        y_proportion = y_dif / total_dif
        target_vector = (x_proportion, y_proportion)

        if total_dif < 3:
            self.master.PLAYER.exp_magnet()
            self.life = 0

        self.x += target_vector[0] * self.speed
        self.y += target_vector[1] * self.speed

    def draw(self, DISPLAY):
        DISPLAY.blit(self.sprite, (self.x, self.y))
        
class Shield_Power_Up():
    def __init__(self, master, xy):
        self.master = master
        self.sprite = self.master.sprites.power_up['Shield']
        self.x = xy[0]
        self.y = xy[1]
        self.life = 1

    def logic(self):
        if self.collision_with_player():
            self.master.PLAYER.activate_shield()
            self.life = 0

    def collision_with_player(self):
        player_rect = pygame.Rect(self.master.PLAYER.x, self.master.PLAYER.y, 20, 20)
        powerup_rect = pygame.Rect(self.x, self.y, 20, 20)
        return player_rect.colliderect(powerup_rect)

    def draw(self, DISPLAY):
        DISPLAY.blit(self.sprite, (self.x, self.y))

class FireRate_Power_Up():
    def __init__(self, master, xy):
        self.master = master
        self.sprite = self.master.sprites.power_up['FireRate']
        self.x = xy[0]
        self.y = xy[1]
        self.life = 1

    def logic(self):
        if self.collision_with_player():
            self.master.PLAYER.activate_fire_rate()
            self.life = 0

    def collision_with_player(self):
        player_rect = pygame.Rect(self.master.PLAYER.x, self.master.PLAYER.y, 20, 20)
        powerup_rect = pygame.Rect(self.x, self.y, 20, 20)
        return player_rect.colliderect(powerup_rect)

    def draw(self, DISPLAY):
        DISPLAY.blit(self.sprite, (self.x, self.y))
        
class MultiFire_Power_Up():
    def __init__(self, master, xy):
        self.master = master
        self.sprite = self.master.sprites.power_up['MultiFire']
        self.x = xy[0]
        self.y = xy[1]
        self.life = 1

    def logic(self):
        if self.collision_with_player():
            self.master.PLAYER.activate_multi_fire()
            self.life = 0

    def collision_with_player(self):
        player_rect = pygame.Rect(self.master.PLAYER.x, self.master.PLAYER.y, 20, 20)
        powerup_rect = pygame.Rect(self.x, self.y, 20, 20)
        return player_rect.colliderect(powerup_rect)

    def draw(self, DISPLAY):
        DISPLAY.blit(self.sprite, (self.x, self.y))