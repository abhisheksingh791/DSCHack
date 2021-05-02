# For calling and start car we use this line
print("There are 4 people leaving in the society named:- ")
print("Arbaz,  Abhishek,  Omkar,  Abhi ")
print("At first type only name but after first one type yes before the Name (for ex- 'yes Abhishek')")

a = str(input("Who is calling to the car??: "))

import pygame

pygame.init()
window = pygame.display.set_mode((1505, 694))

if a == 'Arbaz':
    track = pygame.image.load('5st.png')
    car = pygame.image.load('car2 (1).jpg')
    car = pygame.transform.scale(car, (30, 60))
    car_x = 120
    car_y = 305
    focal_dis = 25
    cam_x_offset = 0
    cam_y_offset = 0
    direction = 'up'
    drive = True
    clock = pygame.time.Clock()
    while drive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                drive = False
            print("mission complet")
        clock.tick(300)
        cam_x = car_x + cam_x_offset + 15
        cam_y = car_y + cam_y_offset + 15
        up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
        down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
        right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
        left_px = window.get_at((cam_x - focal_dis, cam_y))[0]
        print(up_px, right_px, down_px, left_px)
        # change direction (take turn)
        if direction == 'up' and up_px != 255 and right_px == 255:
            direction = 'right'
            cam_x_offset = 30
            car = pygame.transform.rotate(car, -90)
        elif direction == 'right' and right_px != 255 and down_px == 255:
            direction = 'down'
            car_x = car_x + 30
            cam_x_offset = 0
            cam_y_offset = 30
            car = pygame.transform.rotate(car, -90)
        elif direction == 'down' and down_px != 255 and left_px == 255:
            direction = 'left'
            car_y = car_y + 30
            cam_x_offset = -5
            cam_y_offset = 0
            car = pygame.transform.rotate(car, -90)
        elif direction == 'left' and left_px != 255 and down_px == 255:
            direction = 'down'
            cam_x_offset = 0
            cam_y_offset = 30
            car = pygame.transform.rotate(car, 90)
        elif direction == 'down' and down_px != 255 and right_px == 255:
            direction = 'right'
            car_y = car_y + 30
            cam_x_offset = 30
            cam_y_offset = 0
            car = pygame.transform.rotate(car, 90)
        elif direction == 'right' and right_px != 255 and up_px == 255:
            direction = 'up'
            car_x = car_x + 30
            cam_x_offset = 0
            car = pygame.transform.rotate(car, 90)
        elif direction == 'left' and left_px != 255 and up_px == 255:
            direction = "up"
            car_x = car_x - 13
            cam_x_offset = 2

            car = pygame.transform.rotate(car, -90)

        elif up_px == 88 and right_px == 0 and down_px == 34 and left_px == 0:
            b = input("Who is going to put the waste in the dustbin?: >>>> ")
            if b == "yes Abhishek":
                track = pygame.image.load('6st.png')
                car = pygame.image.load('car44.jpg')
                car = pygame.transform.scale(car, (30, 60))
                car_x = 750
                car_y = 105
                focal_dis = 25
                cam_x_offset = -10
                cam_y_offset = 0
                direction = 'down'
                drive = True
                clock = pygame.time.Clock()

        elif up_px == 0 and right_px == 127 and down_px == 57 and left_px == 255:
            b = input("Who is going to put the waste in the dustbin?: >>>> ")
            if b == "yes Omkar":
                track = pygame.image.load('7st.png')

                car = pygame.image.load('car4.jpg')

                car = pygame.transform.scale(car, (30, 60))
                # car_x = 140
                # car_y = 390
                car_x = 610
                car_y = 630
                focal_dis = 25
                cam_x_offset = 0
                cam_y_offset = 0
                direction = 'up'
                drive = True
                clock = pygame.time.Clock()

        elif up_px == 0 and right_px == 0 and down_px == 8 and left_px == 255:
            b = input("Who is going to put the waste in the dustbin?: >>>> ")
            if b == "yes Abhi":
                track = pygame.image.load('8st.png')
                car = pygame.image.load('car3.jpg')
                car = pygame.transform.scale(car, (35, 60))
                car_x = 1340
                car_y = 363
                focal_dis = 25
                cam_x_offset = 0
                cam_y_offset = 0
                direction = 'down'
                drive = True
                clock = pygame.time.Clock()




        # drive
        if direction == 'up' and up_px == 255:
            car_y = car_y - 2
        elif direction == 'right' and right_px == 255:
            car_x = car_x + 2
        elif direction == 'left' and left_px == 255:
            # yha pe x ki value change krna hai
            car_x = car_x - 2
        elif direction == 'down' and down_px == 255:
            car_y = car_y + 2
        window.blit(track, (0, 0))
        window.blit(car, (car_x, car_y))
        pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
        pygame.display.update()

if a == 'Abhishek':
    track = pygame.image.load('6st.png')

    car = pygame.image.load('car44.jpg')
    car = pygame.transform.scale(car, (30, 60))
    car_x = 698
    car_y = 50
    focal_dis = 25
    cam_x_offset = -10
    cam_y_offset = 0
    direction = 'down'
    drive = True
    clock = pygame.time.Clock()
    while drive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                drive = False
            print("mission complet")
        clock.tick(300)
        cam_x = car_x + cam_x_offset + 15
        cam_y = car_y + cam_y_offset + 15
        up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
        down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
        right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
        left_px = window.get_at((cam_x - focal_dis, cam_y))[0]
        print(up_px, right_px, down_px, left_px)
        # change direction (take turn)
        if direction == 'up' and up_px != 255 and right_px == 255:
            direction = 'right'
            cam_x_offset = 30
            car = pygame.transform.rotate(car, -90)
        elif direction == 'right' and right_px != 255 and down_px == 255:
            direction = 'down'
            car_x = car_x + 30
            cam_x_offset = 0
            cam_y_offset = 30
            car = pygame.transform.rotate(car, -90)
        elif direction == 'down' and down_px != 255 and left_px == 255:
            direction = 'left'
            car_y = car_y + 30
            cam_x_offset = -5
            cam_y_offset = 0
            car = pygame.transform.rotate(car, -90)
        elif direction == 'left' and left_px != 255 and down_px == 255:
            direction = 'down'
            cam_x_offset = 0
            cam_y_offset = 30
            car = pygame.transform.rotate(car, 90)
        elif direction == 'down' and down_px != 255 and right_px == 255:
            direction = 'right'
            car_y = car_y + 30
            cam_x_offset = 30
            cam_y_offset = 0
            car = pygame.transform.rotate(car, 90)
        elif direction == 'right' and right_px != 255 and up_px == 255:
            direction = 'up'
            car_x = car_x + 30
            cam_x_offset = 0
            car = pygame.transform.rotate(car, 90)
        elif direction == 'left' and left_px != 255 and up_px == 255:
            direction = "up"
            car_x = car_x - 13
            cam_x_offset = 2

            car = pygame.transform.rotate(car, -90)

        elif up_px == 8 and right_px == 254 and down_px == 0 and left_px == 0:
            b = input("Who is going to put the waste in the dustbin?: >>>> ")
            if b == "yes Arbaz":
                track = pygame.image.load('5st.png')
                car = pygame.image.load('car2 (1).jpg')
                car = pygame.transform.scale(car, (30, 60))
                car_x = 120
                car_y = 305
                focal_dis = 25
                cam_x_offset = 0
                cam_y_offset = 0
                direction = 'up'
                drive = True
                clock = pygame.time.Clock()

        elif up_px == 88 and right_px == 0 and down_px == 34 and left_px == 0:
            b = input("Who is going to put the waste in the dustbin?: >>>> ")
            if b == "yes Omkar":
                track = pygame.image.load('7st.png')

                car = pygame.image.load('car4.jpg')

                car = pygame.transform.scale(car, (30, 60))
                # car_x = 140
                # car_y = 390
                car_x = 610
                car_y = 630
                focal_dis = 25
                cam_x_offset = 0
                cam_y_offset = 0
                direction = 'up'
                drive = True
                clock = pygame.time.Clock()

        elif up_px == 0 and right_px == 0 and down_px == 8 and left_px == 255:
            b = input("Who is going to put the waste in the dustbin?: >>>> ")
            if b == "yes Abhi":
                track = pygame.image.load('8st.png')
                car = pygame.image.load('car3.jpg')
                car = pygame.transform.scale(car, (35, 60))
                car_x = 1340
                car_y = 363
                focal_dis = 25
                cam_x_offset = 0
                cam_y_offset = 0
                direction = 'down'
                drive = True
                clock = pygame.time.Clock()

            # drive
        if direction == 'up' and up_px == 255:
            car_y = car_y - 2
        elif direction == 'right' and right_px == 255:
            car_x = car_x + 2
        elif direction == 'left' and left_px == 255:
            # yha pe x ki value change krna hai
            car_x = car_x - 2
        elif direction == 'down' and down_px == 255:
            car_y = car_y + 2
        window.blit(track, (0, 0))
        window.blit(car, (car_x, car_y))
        pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
        pygame.display.update()


elif a == 'Omkar':
    track = pygame.image.load('7st.png')

    car = pygame.image.load('car4.jpg')

    car = pygame.transform.scale(car, (30, 60))
    # car_x = 140
    # car_y = 390
    car_x = 610
    car_y = 630
    focal_dis = 25
    cam_x_offset = 0
    cam_y_offset = 0
    direction = 'up'
    drive = True
    clock = pygame.time.Clock()
    while drive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                drive = False
            print("mission complet")
        clock.tick(300)
        cam_x = car_x + cam_x_offset + 15
        cam_y = car_y + cam_y_offset + 15
        up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
        down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
        right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
        left_px = window.get_at((cam_x - focal_dis, cam_y))[0]
        print(up_px, right_px, down_px, left_px)
        # change direction (take turn)
        if direction == 'up' and up_px != 255 and right_px == 255:
            direction = 'right'
            cam_x_offset = 30
            car = pygame.transform.rotate(car, -90)
        elif direction == 'right' and right_px != 255 and down_px == 255:
            direction = 'down'
            car_x = car_x + 30
            cam_x_offset = 0
            cam_y_offset = 30
            car = pygame.transform.rotate(car, -90)
        elif direction == 'down' and down_px != 255 and left_px == 255:
            direction = 'left'
            car_y = car_y + 30
            cam_x_offset = -5
            cam_y_offset = 0
            car = pygame.transform.rotate(car, -90)
        elif direction == 'left' and left_px != 255 and down_px == 255:
            direction = 'down'
            cam_x_offset = 0
            cam_y_offset = 30
            car = pygame.transform.rotate(car, 90)
        elif direction == 'down' and down_px != 255 and right_px == 255:
            direction = 'right'
            car_y = car_y + 30
            cam_x_offset = 30
            cam_y_offset = 0
            car = pygame.transform.rotate(car, 90)
        elif direction == 'right' and right_px != 255 and up_px == 255:
            direction = 'up'
            car_x = car_x + 30
            cam_x_offset = 0
            car = pygame.transform.rotate(car, 90)
        elif direction == 'left' and left_px != 255 and up_px == 255:
            direction = "up"
            car_x = car_x - 13
            cam_x_offset = 2

            car = pygame.transform.rotate(car, -90)

        elif up_px == 0 and right_px == 0 and down_px == 8 and left_px == 255:
            b = input("Who is going to put the waste in the dustbin?: >>>> ")
            if b == "yes Arbaz":
                track = pygame.image.load('5st.png')
                car = pygame.image.load('car2 (1).jpg')
                car = pygame.transform.scale(car, (30, 60))
                car_x = 120
                car_y = 305
                focal_dis = 25
                cam_x_offset = 0
                cam_y_offset = 0
                direction = 'up'
                drive = True
                clock = pygame.time.Clock()


        elif up_px == 88 and right_px == 0 and down_px == 34 and left_px == 0:
            b = input("Who is going to put the waste in the dustbin?: >>>> ")
            if b == "yes Abhishek":
                track = pygame.image.load('6st.png')
                car = pygame.image.load('car44.jpg')
                car = pygame.transform.scale(car, (30, 60))
                car_x = 750
                car_y = 105
                focal_dis = 25
                cam_x_offset = -10
                cam_y_offset = 0
                direction = 'down'
                drive = True
                clock = pygame.time.Clock()

        elif up_px == 0 and right_px == 0 and down_px == 8 and left_px == 255:
            b = input("Who is going to put the waste in the dustbin?: >>>> ")
            if b == "yes Abhi":
                track = pygame.image.load('8st.png')
                car = pygame.image.load('car3.jpg')
                car = pygame.transform.scale(car, (35, 60))
                car_x = 1340
                car_y = 363
                focal_dis = 25
                cam_x_offset = 0
                cam_y_offset = 0
                direction = 'down'
                drive = True
                clock = pygame.time.Clock()


        # drive
        if direction == 'up' and up_px == 255:
            car_y = car_y - 2
        elif direction == 'right' and right_px == 255:
            car_x = car_x + 2
        elif direction == 'left' and left_px == 255:
            # yha pe x ki value change krna hai
            car_x = car_x - 2
        elif direction == 'down' and down_px == 255:
            car_y = car_y + 2
        window.blit(track, (0, 0))
        window.blit(car, (car_x, car_y))
        pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
        pygame.display.update()

elif a == 'Abhi':
    track = pygame.image.load('8st.png')
    car = pygame.image.load('car4.jpg')
    car = pygame.transform.scale(car, (35, 60))
    car_x = 1340
    car_y = 363
    focal_dis = 25
    cam_x_offset = 0
    cam_y_offset = 0
    direction = 'down'
    drive = True
    clock = pygame.time.Clock()
    while drive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                drive = False
            print("mission complet")
        clock.tick(300)
        cam_x = car_x + cam_x_offset + 15
        cam_y = car_y + cam_y_offset + 15
        up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
        down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
        right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
        left_px = window.get_at((cam_x - focal_dis, cam_y))[0]
        print(up_px, right_px, down_px, left_px)
        # change direction (take turn)
        if direction == 'up' and up_px != 255 and right_px == 255:
            direction = 'right'
            cam_x_offset = 30
            car = pygame.transform.rotate(car, -90)
        elif direction == 'right' and right_px != 255 and down_px == 255:
            direction = 'down'
            car_x = car_x + 30
            cam_x_offset = 0
            cam_y_offset = 30
            car = pygame.transform.rotate(car, -90)
        elif direction == 'down' and down_px != 255 and left_px == 255:
            direction = 'left'
            car_y = car_y + 30
            cam_x_offset = -5
            cam_y_offset = 0
            car = pygame.transform.rotate(car, -90)
        elif direction == 'left' and left_px != 255 and down_px == 255:
            direction = 'down'
            cam_x_offset = 0
            cam_y_offset = 30
            car = pygame.transform.rotate(car, 90)
        elif direction == 'down' and down_px != 255 and right_px == 255:
            direction = 'right'
            car_y = car_y + 30
            cam_x_offset = 30
            cam_y_offset = 0
            car = pygame.transform.rotate(car, 90)
        elif direction == 'right' and right_px != 255 and up_px == 255:
            direction = 'up'
            car_x = car_x + 30
            cam_x_offset = 0
            car = pygame.transform.rotate(car, 90)
        elif direction == 'left' and left_px != 255 and up_px == 255:
            direction = "up"
            car_x = car_x - 13
            cam_x_offset = 2

            car = pygame.transform.rotate(car, -90)

        elif up_px == 21 and right_px == 0 and down_px == 0 and left_px == 200:
            b = input("Who is going to put the waste in the dustbin?: >>>> ")
            if b == "yes Arbaz":
                track = pygame.image.load('5st.png')
                car = pygame.image.load('car2 (1).jpg')
                car = pygame.transform.scale(car, (30, 60))
                car_x = 120
                car_y = 305
                focal_dis = 25
                cam_x_offset = 0
                cam_y_offset = 0
                direction = 'up'
                drive = True
                clock = pygame.time.Clock()

        elif up_px == 0 and right_px == 127 and down_px == 9 and left_px == 255:
            b = input("Who is going to put the waste in the dustbin?: >>>> ")
            if b == "yes Omkar":
                track = pygame.image.load('7st.png')

                car = pygame.image.load('car4.jpg')

                car = pygame.transform.scale(car, (30, 60))
                # car_x = 140
                # car_y = 390
                car_x = 610
                car_y = 630
                focal_dis = 25
                cam_x_offset = 0
                cam_y_offset = 0
                direction = 'up'
                drive = True
                clock = pygame.time.Clock()

        elif up_px == 88 and right_px == 0 and down_px == 34 and left_px == 0:
            b = input("Who is going to put the waste in the dustbin?: >>>> ")
            if b == "yes Abhishek":
                track = pygame.image.load('6st.png')
                car = pygame.image.load('car44.jpg')
                car = pygame.transform.scale(car, (30, 60))
                car_x = 750
                car_y = 105
                focal_dis = 25
                cam_x_offset = -10
                cam_y_offset = 0
                direction = 'down'
                drive = True
                clock = pygame.time.Clock()

            # drive
        if direction == 'up' and up_px == 255:
            car_y = car_y - 2
        elif direction == 'right' and right_px == 255:
            car_x = car_x + 2
        elif direction == 'left' and left_px == 255:
            # yha pe x ki value change krna hai
            car_x = car_x - 2
        elif direction == 'down' and down_px == 255:
            car_y = car_y + 2
        window.blit(track, (0, 0))
        window.blit(car, (car_x, car_y))
        pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
        pygame.display.update()
