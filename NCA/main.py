import pygame, sys, random
import asyncio  # Import asyncio for asynchronous operations
import player, sprite_sys, enemies

pygame.init()

DEBUG_MODE = False
MOUSE_POS = (0, 0)

# Setup the screen
SCREEN_SIZE = [800, 600]
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Never Cheese Again")

# Setup the joysticks
pygame.joystick.init()
joy_count = pygame.joystick.get_count()
JOYSTICK = []
for i in range(joy_count):
    JOYSTICK.append(pygame.joystick.Joystick(i))
    JOYSTICK[i].init()

AXIS_A = (0, 0)
AXIS_B = (0, 0)

# Setup clock
CLOCK = pygame.time.Clock()
FPS = 60

# Game Instances
class GAME():
    def __init__(self):
        self.DEBUG_MODE = DEBUG_MODE
        self.paused = False
        self.score = 0

        self.level_dim = SCREEN_SIZE
        self.sprites = sprite_sys.Sprites()
        self.ENEMIES = []
        self.BULLETS = []
        self.PLAYER = player.Player(self)
        self.OBSTACLES = []

        self.enemy_rects = []
        self.bullet_rects = []
        self.bullet_dict = {}
        self.obstacle_rects = []

        self.PARTICLES = []

        self.game_state = "START_SCREEN"

    def render_start_screen(self):
        SCREEN.fill((21, 57, 148))
        font = pygame.font.SysFont("Arial", 50)
        font_small = pygame.font.SysFont("Arial", 30)
        
        # Instructions
        instructions1 = font_small.render("Use Left Stick to Move", True, (255, 255, 255))
        instructions2 = font_small.render("Use Right Stick to Shoot", True, (255, 255, 255))
        instructions3 = font_small.render("Press 'A' to Start", True, (255, 255, 255))
        
        # Render instructions
        SCREEN.blit(instructions1, (SCREEN.get_width() // 2 - instructions1.get_width() // 2, SCREEN.get_height() // 2 - 100))
        SCREEN.blit(instructions2, (SCREEN.get_width() // 2 - instructions2.get_width() // 2, SCREEN.get_height() // 2 - 50))
        SCREEN.blit(instructions3, (SCREEN.get_width() // 2 - instructions3.get_width() // 2, SCREEN.get_height() // 2))
        pygame.display.flip()
        
    def pause(self):
        self.paused = not self.paused

    def pause_logic(self):
        pass

    def pause_render(self):
        SCREEN.blit(self.sprites.pause, (200, 200))

    def update_collisions(self):
        self.enemy_rects = []
        for enemy in self.ENEMIES:
            if enemy.alive:
                rect = pygame.Rect(enemy.x + enemy.hit_box[0], enemy.y + enemy.hit_box[1], enemy.hit_box[2], enemy.hit_box[3])
                self.enemy_rects.append(rect)
                if rect.colliderect(pygame.Rect(self.PLAYER.x, self.PLAYER.y, 20, 20)) and not self.PLAYER.invulnerable:
                    self.PLAYER.take_damage()
                    enemy.alive = False

        self.bullet_rects = []
        self.bullet_dict = {}
        for bullet in self.BULLETS:
            rect = pygame.Rect(bullet.x + bullet.hit_box[0], bullet.y + bullet.hit_box[1], bullet.hit_box[2], bullet.hit_box[3])
            self.bullet_rects.append(rect)
            bullet_index = len(self.bullet_rects) - 1
            self.bullet_dict[bullet_index] = bullet

        self.obstacle_rects = []
        for blocks in self.OBSTACLES:
            rect = blocks.my_rect
            self.obstacle_rects.append(rect)

    def render_level(self):
        pass

    def update_score(self, points):
        self.score += points
        
    def game_over(self):
        self.game_state = "GAME_OVER"

    def restart_game(self):
        self.__init__()

def rendering():
    SCREEN.fill((255, 255, 255))
    font = pygame.font.SysFont("Arial", 30)
    score_text = font.render(f"Score: {game.score}", True, (0, 0, 0))
    lives_text = font.render(f"Lives: {game.PLAYER.lives}", True, (0, 0, 0))
    xp_text = font.render(f"Digestion: {game.PLAYER.exp}", True, (0, 0, 0))
    power_up_text = font.render(f"Power-Up: {game.PLAYER.active_power_up}", True, (0, 0, 0))
    progress = game.PLAYER.exp / 100
    progress_bar_length = 200
    pygame.draw.rect(SCREEN, (0, 255, 0), (10, 90, progress_bar_length * progress, 20))
    pygame.draw.rect(SCREEN, (0, 0, 0), (10, 90, progress_bar_length, 20), 2)
    SCREEN.blit(score_text, (10, 10))
    SCREEN.blit(lives_text, (10, 50))
    SCREEN.blit(xp_text, (10, 130))
    SCREEN.blit(power_up_text, (SCREEN.get_width() - power_up_text.get_width() - 10, 10))
    for stuff in game.OBSTACLES:
        stuff.draw(SCREEN)
    for particle in game.PARTICLES:
        particle.draw(SCREEN)
    for bullet in game.BULLETS:
        bullet.draw(SCREEN)
    for enemy in game.ENEMIES:
        enemy.draw(SCREEN)
    game.PLAYER.draw(SCREEN)
    if game.paused:
        game.pause_render()
    pygame.display.update()

def render_game_over():
    SCREEN.fill((0, 0, 0))
    font = pygame.font.SysFont("Arial", 50)
    text1 = font.render("Game Over! Play Again?", True, (255, 255, 255))
    text2 = font.render("Yes (A/Y) or No (B/N)", True, (255, 255, 255))
    SCREEN.blit(text1, (SCREEN.get_width() // 2 - text1.get_width() // 2, SCREEN.get_height() // 2 - text1.get_height()))
    SCREEN.blit(text2, (SCREEN.get_width() // 2 - text2.get_width() // 2, SCREEN.get_height() // 2))
    pygame.display.flip()

def session_kill():
    pygame.quit()
    sys.exit()

def logic():
    game.PLAYER.logic()  # Handles player-specific logic

    game.update_collisions()  # Update collisions

    for stuff in game.OBSTACLES:
        stuff.logic()

    for bullet in game.BULLETS:
        bullet.logic()

    i = len(game.BULLETS) - 1
    while i >= 0:
        if game.BULLETS[i].life < 1:
            del game.BULLETS[i]
        i -= 1

    for enemy in game.ENEMIES:
        enemy.logic()
    game.ENEMIES = [enemy for enemy in game.ENEMIES if enemy.alive]  # Keep only alive enemies
    i = len(game.ENEMIES) - 1
    while i >= 0:
        if game.ENEMIES[i].del_self:
            del game.ENEMIES[i]
        i -= 1

    for particles in game.PARTICLES:
        particles.logic()
    i = len(game.PARTICLES) - 1
    while i >= 0:
        if game.PARTICLES[i].life < 1:
            del game.PARTICLES[i]
        i -= 1

    new_spawn = random.randint(0, 120)
    if new_spawn == 1:
        game.ENEMIES.append(enemies.cheese(game, (random.randint(0, SCREEN_SIZE[0]), random.randint(0, SCREEN_SIZE[1])), random.randint(0, 1)))

async def user_input():
    global AXIS_A, AXIS_B, MOUSE_POS
    MOUSE_POS = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            session_kill()
        elif event.type == pygame.JOYBUTTONDOWN:
            if game.game_state == "START_SCREEN":
                if event.button == 0:
                    game.game_state = "PLAYING"
            elif game.game_state == "PLAYING":
                if event.button == 7:
                    game.pause()
                    print("Pause")
            elif game.game_state == "GAME_OVER":
                if event.button == 0:
                    game.restart_game()
                elif event.button == 1:
                    session_kill()
        elif event.type == pygame.JOYBUTTONUP:
            pass
        elif event.type == pygame.KEYDOWN:
            if game.game_state == "GAME_OVER":
                if event.key == pygame.K_y:
                    game.restart_game()
                elif event.key == pygame.K_n:
                    session_kill()

    for joystick in JOYSTICK:
        if joystick.get_init():
            num_axes = joystick.get_numaxes()
            if num_axes >= 4:
                axis_0 = joystick.get_axis(0)
                axis_1 = joystick.get_axis(1)
                axis_2 = joystick.get_axis(2)
                axis_3 = joystick.get_axis(3)
                AXIS_A = (axis_0, axis_1)
                AXIS_B = (axis_2, axis_3)

    if not game.paused and game.game_state == "PLAYING":
        game.PLAYER.user_inputs(AXIS_A, AXIS_B)

async def main():
    global game
    game = GAME()
    game.ENEMIES.append(enemies.cheese(game, (400, 200)))
    while True:
        await user_input()
        if game.game_state == "START_SCREEN":
            game.render_start_screen()
        elif game.game_state == "PLAYING":
            logic()
            rendering()
        elif game.game_state == "GAME_OVER":
            render_game_over()
        pygame.display.update()
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())