import pygame
import sys
import time
from pictures import *
from map import mapa


# =========================================================
# Nastavení pygame
# =========================================================
pygame.init()

SCALE = 6
OLED_W = 128
OLED_H = 64
SCREEN_W = OLED_W * SCALE
SCREEN_H = OLED_H * SCALE

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Snack Rider v1.0")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 8 * SCALE // 2)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def dungeon():

    


    # ===== stav hry =====
    movie = 1
    movie2 = 1
    movie3 = 0
    smer = 1
    room = 0
    food1_x = []
    food1_y = []
    food1_x_total = []
    food1_y_total = []
    food_collected = set()
    food1_count = 0
    food = 0
    food_hero_count = 0
   

    # ===== hrdina =====
    x_hero = 8
    y_hero = 35
    x_hero_old = 0
    y_hero_old = 0
    jump = 0
    pad = 0
    up = 0
    full_lives = 1000
    livesblok = 0

    # ===== scroll mapy =====
    x_roll = 0
    y_roll = 0

    # ===== pomocné =====
    tlac = 1
    line = 0
    next_x = 0
    fix = 0

    # ===== nepřátelé a překážky =====
    blade1_x = []
    blade1_y = []
    blade1_count = 0

    monster1_x = []
    monster1_y = []
    monster1_x_old = []
    monster1_y_old = []
    monster1_count = 0
    monster1_move = []

    monster2_x = []
    monster2_y = []
    monster2_x_old = []
    monster2_y_old = []
    monster2_count = 0
    monster2_move = []
    lives = full_lives




    def draw_picture(next_x, line, picture, color_p):
        px = next_x * 8
        py = line * 7
        for line2 in range(7):
            for next2_x in range(8):
                read = picture[line2][next2_x]

                if read == '1':
                    color = color_p
                elif read == '2':
                    color = 'yellow'
                elif read == '3':
                    color = 'brown'
                elif read == '4':
                    color = 'red'
                elif read == '5':
                    color = 'orange'
                elif read == '6':
                    color = 'blue'
                elif read == '7':
                    color = 'white'
                elif read == '8':
                    color = 'green'
                else:
                    color = 'black'

                pygame.draw.rect(
                    screen,
                    color,
                    ((px + next2_x) * SCALE, (py + line2) * SCALE, SCALE, SCALE)
                )

    def reset_room():
        nonlocal monster1_x_old, monster1_y_old
        nonlocal monster1_x, monster1_y
        nonlocal monster2_x_old, monster2_y_old
        nonlocal monster2_x, monster2_y
        nonlocal blade1_x, blade1_y, livesblok
        nonlocal monster1_move, monster1_count, blade1_count
        nonlocal monster2_move, monster2_count, food1_x, food1_y, food1_count


        monster1_x_old = []
        monster1_y_old = []
        monster1_x = []
        monster1_y = []
        food1_x = []
        food1_y = []
        food1_count = 0
   

        monster2_x_old = []
        monster2_y_old = []
        monster2_x = []
        monster2_y = []

        blade1_x = []
        blade1_y = []

        monster1_move = []
        monster1_count = 0

        monster2_move = []
        monster2_count = 0
        livesblok = 0

        blade1_count = 0

    running = True

    while running:
        clock.tick(10)

        movie = -movie
        movie3 += 1
        if movie3 > 10:
            movie3 = 0

        x_hero_old = x_hero
        y_hero_old = y_hero

        move_right = False
        move_left = False
        move_jump = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            return

        if keys[pygame.K_RIGHT]:
            move_right = True
        if keys[pygame.K_LEFT]:
            move_left = True
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            move_jump = True

        # --- mazání staré pozice hráče ---
        pygame.draw.rect(
            screen,
            BLACK,
            (x_hero * SCALE, y_hero * SCALE, 8 * SCALE, 7 * SCALE)
        )

        # --- mazání starých pozic monster1 ---
        for i in range(monster1_count):
            pygame.draw.rect(
                screen,
                BLACK,
                (monster1_x[i] * SCALE, monster1_y[i] * SCALE, 8 * SCALE, 7 * SCALE)
            )

        # --- mazání starých pozic monster2 ---
        for i in range(monster2_count):
            pygame.draw.rect(
                screen,
                BLACK,
                (monster2_x[i] * SCALE, monster2_y[i] * SCALE, 8 * SCALE, 7 * SCALE)
            )

        # --- mazání starých pozic blade ---
        for i in range(blade1_count):
            pygame.draw.rect(
                screen,
                BLACK,
                (blade1_x[i] * SCALE, blade1_y[i] * SCALE, 8 * SCALE, 7 * SCALE)
            )

        # --- vstup ---
        if move_right:
            smer = 1
            x_hero += 8
            movie2 = -movie2

        if move_left:
            smer = 2
            x_hero -= 8
            movie2 = -movie2

        if move_jump:
            tlac = 1
            if jump == 0 and pad == 0:
                jump = 1

        # --- skok ---
        if 0 < jump <= 4:
            y_hero -= 7
            jump += 1
        elif jump > 4:
            y_hero += 7
            jump += 1

        if jump > 8:
            jump = 0

        
        colision = mapa[y_hero // 7 + y_roll][x_hero // 8 + x_roll : x_hero // 8 + 1 + x_roll]
        fix = mapa[y_hero // 7 + y_roll + 1][x_hero // 8 + x_roll : x_hero // 8 + 1 + x_roll]

        if (fix == " " or fix == "S" or fix == "M" or fix == "P" or fix == "L" or fix == "F") and jump == 0:
            y_hero += 7
            pad = 1
            up = 2
        else:
            pad = 0
            up = 1

        if colision not in [" ", "S", "M", "P", "L", 'F']:
            y_hero = y_hero_old
            x_hero = x_hero_old
            col = 1
        else:
            col = 0

        if colision == "L" and livesblok == 0:
            lives = full_lives
            livesblok = 1
        
        if colision == "F":
            hero_food_x = x_hero // 8 + x_roll
            hero_food_y = y_hero // 7 + y_roll

            if (hero_food_x, hero_food_y) not in food_collected:
                food_collected.add((hero_food_x, hero_food_y))
                food += 1
                food_hero_count += 1

        for i in range(food1_count):
            food_world_x = food1_x[i] + x_roll
            food_world_y = food1_y[i] + y_roll

            if (food_world_x, food_world_y) not in food_collected:
                draw_picture(food1_x[i], food1_y[i], new_food, 'brown')



           

        # --- přechod roomazovky ---
        if x_hero // 8 >= 16 and smer == 1:
            x_roll += 16
            x_hero = 0
            smer = 0
            room = 0
            reset_room()

        if x_hero // 8 <= 0 and smer == 2 and x_roll > 0:
            x_roll -= 16
            x_hero = 120
            smer = 0
            room = 0
            reset_room()

        if y_hero // 7 >= 8 and up == 2:
            y_roll += 7
            y_hero = 0
            up = 0
            room = 0
            reset_room()

        if y_hero // 7 <= 0 and up == 1 and y_roll > 0:
            y_roll -= 7
            y_hero = 56
            up = 0
            room = 0
            reset_room()

        # --- načtení roomazovky ---
        if room == 0:
            screen.fill(BLACK)

            line = 0
            next_x = 0

            for _ in range(144):
                read = mapa[line + y_roll][x_roll + next_x: x_roll + next_x + 1]

                if read == '#':
                    draw_picture(next_x, line, new_stone, 'gray')

                if read == 'L':
                    draw_picture(next_x, line, new_health, 'white')

                if read == 'V':
                    draw_picture(next_x, line, new_water, 'blue')

                if read == 'F':
                    food1_count += 1
                    food1_x.append(next_x)
                    food1_y.append(line)
                    food1_x_total.append(next_x + x_roll)
                    food1_y_total.append(line + y_roll)
              



                if read == 'H':
                    blade1_count += 1
                    blade1_x.append(next_x * 8)
                    blade1_y.append(line * 7)

                if read == 'M':
                    monster1_count += 1
                    monster1_x.append(next_x * 8)
                    monster1_y.append(line * 7)
                    monster1_x_old.append(next_x * 8)
                    monster1_y_old.append(line * 7)
                    monster1_move.append(8)

                if read == 'P':
                    monster2_count += 1
                    monster2_x.append(next_x * 8)
                    monster2_y.append(line * 7)
                    monster2_x_old.append(next_x * 8)
                    monster2_y_old.append(line * 7)
                    monster2_move.append(7)

                next_x += 1

                if next_x == 16:
                    line += 1
                    next_x = 0

                if line == 9:
                    line = 0
                    next_x = 0
                    room = 1
                    break

        # --- pohyb monster1 ---
        for i in range(monster1_count):
            monster1_x[i] += monster1_move[i]
            
            colision3 = mapa[monster1_y[i] // 7 + y_roll][monster1_x[i] // 8 + x_roll : monster1_x[i] // 8 + 1 + x_roll]
    

            if colision3 not in [" ", "S", "M", "P"]:
                monster1_y[i] = monster1_y_old[i]
                monster1_x[i] = monster1_x_old[i]
                monster1_move[i] = -monster1_move[i]

            monster1_y_old[i] = monster1_y[i]
            monster1_x_old[i] = monster1_x[i]

        # --- pohyb monster2 ---
        for i in range(monster2_count):
            monster2_y[i] += monster2_move[i]
        
            colision4 = mapa[monster2_y[i] // 7 + y_roll][monster2_x[i] // 8 + x_roll : monster2_x[i] // 8 + 1 + x_roll]

            if colision4 not in [" ", "S", "M", "P"]:
                monster2_y[i] = monster2_y_old[i]
                monster2_x[i] = monster2_x_old[i]
                monster2_move[i] = -monster2_move[i]

            monster2_y_old[i] = monster2_y[i]
            monster2_x_old[i] = monster2_x[i]

        # --- kreslení monster1 ---
        for i in range(monster1_count):
            if movie == 1:
                draw_picture(monster1_x[i] // 8, monster1_y[i] // 7, new_monster1, 'red')
            else:
                draw_picture(monster1_x[i] // 8, monster1_y[i] // 7, new_monster1_mov, 'red')

        # --- kreslení monster2 ---
        for i in range(monster2_count):
            if movie == 1:
                draw_picture(monster2_x[i] // 8, monster2_y[i] // 7, new_monster2, 'green')
            else:
                draw_picture(monster2_x[i] // 8, monster2_y[i] // 7, new_monster2_mov, 'green')

        # --- kreslení blade ---
        for i in range(blade1_count):
            if movie3 > 5:
                draw_picture(blade1_x[i] // 8, blade1_y[i] // 7, new_blade, 'yellow')
            else:
                draw_picture(blade1_x[i] // 8, blade1_y[i] // 7, new_blade_mov, 'yellow')



        # --- kolize s monstry ---
        dead_now = False

        for i in range(monster1_count):
            if monster1_x[i] == x_hero and monster1_y[i] == y_hero:
                draw_picture(x_hero // 8, y_hero // 7, new_hero_death, 'red')
                lives -= 1
                dead_now = True

        for i in range(monster2_count):
            if monster2_x[i] == x_hero and monster2_y[i] == y_hero:
                draw_picture(x_hero // 8, y_hero // 7, new_hero_death, 'red')
                lives -= 1
                dead_now = True

        if fix == "H" and movie3 > 5:
            draw_picture(x_hero // 8, y_hero // 7, new_hero_death, 'red')
            lives -= 1
            dead_now = True

        if fix == "V":
            draw_picture(x_hero // 8, y_hero // 7, new_hero_death, 'red')
            lives -= 1
            dead_now = True

        

        # --- kreslení hráče ---
        if not dead_now:
            if smer == 0:
                draw_picture(x_hero // 8, y_hero // 7, new_hero_up, 'green')
            elif smer == 1 or smer == 2:
                if movie2 == 1:
                    draw_picture(x_hero // 8, y_hero // 7, new_hero_left, 'green')
                else:
                    draw_picture(x_hero // 8, y_hero // 7, new_hero_right, 'green')
            elif smer == 3:
                draw_picture(x_hero // 8, y_hero // 7, new_hero_up, 'green')
            elif smer == 4:
                draw_picture(x_hero // 8, y_hero // 7, new_hero_down, 'green')

        # --- HUD ---
        font = pygame.font.SysFont("Arial", 35, bold=True)

       
        
        txt = font.render(str(food) + "      ", True, (180,180,180), (0,0,0))
        screen.blit(txt , (114 *SCALE, 0 )  )
        draw_picture(15, 0, new_food_ico, 'brown')

        txt = font.render(str(lives), True, (180,180,180), (0,0,0))
        screen.blit(txt, (50, 0 )  )
        draw_picture(0, 0, new_heart_ico, 'pink')


      

        # --- GAME OVER ---
        if lives <= 0:
           
            txt = font.render("GAME OVER", True, BLACK, WHITE)
            screen.blit(txt, (40 * SCALE, 25 * SCALE))
            pygame.display.flip()
            pygame.time.delay(3000)
            return dungeon()

        pygame.display.flip()


dungeon()
pygame.quit()
sys.exit()