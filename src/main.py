from class_gather.ac_class import AC
import time
game = AC()


while True:
    x = game.x_pos()
    y = game.y_pos()
    z = game.z_pos()
    game.bullet_update()
    game.hp_date()
    print(f"x 좌표 {x}\ny 좌표 {y}\nz 좌표 {z}")
    print("-"*99)

    time.sleep(0.5)
    