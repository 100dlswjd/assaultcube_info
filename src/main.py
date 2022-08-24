from class_gather.ac_class import AC
import time
a = AC()

while True:
    hp = a.hp()
    bullet = a.bullet()

    print("체력 : ",hp)
    print("총알 : ",bullet)
    print("-"*99)
    time.sleep(0.5)
