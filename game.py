import random
import PIL.Image
import pygame
import sys
import threading
import string
from horse import Horse

from PIL import ImageFont, ImageDraw


class Window:
    def __init__(self, width, height, title):

        #create three new horses from the horse class called horse1, horse2 and horse3
        self.horse1 = Horse("Cavalo Roxo", 0, "horse1.png")
        self.horse2 = Horse("Cavalo Verde", 0, "horse2.png")
        self.horse3 = Horse("Cavalo Amarelo", 0, "horse3.png")



        self.winscreen = PIL.Image.open("winner.png")
        self.width = width
        self.height = height
        self.title = title
        self.gameDisplay = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.list = []
        self.running = True
        self.gameExit = False
        self.gameOver = False
        self.counter = 0


    def game_loop(self):
        while self.running:


            self.clock.tick(self.fps)


            thread1 = threading.Thread(target=self.image_move, args=(self.horse1.image_game, 0, 0,self.horse1.name))
            thread2 = threading.Thread(target=self.image_move, args=(self.horse2.image_game, 0, 200,self.horse2.name))
            thread3 = threading.Thread(target=self.image_move, args=(self.horse3.image_game, 0, 400,self.horse3.name))
            thread4 = threading.Thread(target=self.show_winners)

            thread1.start()
            thread2.start()
            thread3.start()
            thread4.start()

            thread1.join()
            thread2.join()
            thread3.join()
            thread4.join()


    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.gameExit = True
                if event.key == pygame.K_SPACE:
                    self.gameOver = True

    def show_winners(self):
        running = 1
        while running == 1:
            pass
            if len(self.list) >= 3:
                print(self.list)
                print("O vencedor é: " + self.list[0])

                #set the image in the background as the horse in position 0
                self.placements()
                for i in range(0, len(self.list)):
                    print("Colocações: " + self.list[i]+ " - " + str(i+1))

                running = 0
            pass


    def placements(self):
        winner_horse = self.list[0]
        second_place = self.list[1]
        third_place = self.list[2]
        print(winner_horse + " " + second_place + " " + third_place)
        if winner_horse == self.horse1.name:
            winner_horse = self.horse1.image_winscreen
        elif winner_horse == self.horse2.name:
            winner_horse = self.horse2.image_winscreen
        elif winner_horse == self.horse3.name:
            winner_horse = self.horse3.image_winscreen
        if second_place == self.horse1.name:
            second_place = self.horse1.image_winscreen
        elif second_place == self.horse2.name:
            second_place = self.horse2.image_winscreen
        elif second_place == self.horse3.name:
            second_place = self.horse3.image_winscreen
        if third_place == self.horse1.name:
            third_place = self.horse1.image_winscreen
        elif third_place == self.horse2.name:
            third_place = self.horse2.image_winscreen
        elif third_place == self.horse3.name:
            third_place = self.horse3.image_winscreen

        self.winscreen.paste(winner_horse, (290, 220), winner_horse)
        self.winscreen.paste(second_place, (510, 250), second_place)
        self.winscreen.paste(third_place, (50, 270), third_place)

        font = ImageFont.truetype("arial.ttf", 48)
        text = self.list[0]
        text_img = PIL.Image.new('RGBA', (370, 200), (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_img)
        draw.text((0, 0), text, (0, 0, 0), font=font)
        self.winscreen.paste(text_img, (200, 85), text_img)

        rand_number = random.randint(1, 1000)
        rand_letter = (random.choice(string.ascii_letters)).upper()
        rand_letter2 = random.choice(string.ascii_letters).upper()

        font = ImageFont.truetype("arial.ttf", 32)
        text = rand_letter+rand_letter2+str(rand_number)
        text_img = PIL.Image.new('RGBA', (370, 200), (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_img)
        draw.text((0, 0), text, (0, 0, 0), font=font)
        self.winscreen.paste(text_img, (0, 0), text_img)
        self.winscreen.save("winscreen.png")



    def game_exit(self):
        pygame.quit()
        sys.exit()

    def image_move(self,img,startx,starty,horsename):
        running = 0
        img_x = startx
        img_y = starty
        while self.running:
            self.gameDisplay.blit(img, (img_x, img_y))
            pygame.display.update()
            #1 é o ideal
            img_x += 1
            img_y += 0

            pygame.time.delay(5)

            self.gameDisplay.fill((0, 0, 0))

            if img_x > self.width or img_y > self.height:
                print("-------------------------------"+horsename+ " Terminou a corrida"+"-------------------------------")

                self.list.append(horsename)

                while running == 0:
                   pass
        pass
