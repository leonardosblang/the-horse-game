import random
import PIL.Image
import pygame
import sys
import threading
import string
from PIL import *

#create a window class for the game and the game loop and then run the game
from PIL import ImageFont, ImageDraw
from PIL.Image import Image




rand_number= random.randint(1,1000)
rand_letter = (random.choice(string.ascii_letters)).upper()
rand_letter2 = random.choice(string.ascii_letters).upper()

class Window:
    def __init__(self, width, height, title):
        #set an image for the background

        self.horse1img = PIL.Image.open("horse1.png")
        self.horse2img = PIL.Image.open("horse2.png")
        self.horse3img = PIL.Image.open("horse3.png")
        self.width, self.height = self.horse1img.size
        self.horse1img = self.horse1img.resize((int(self.width/5), int(self.height/5)))
        self.horse2img = self.horse2img.resize((int(self.width/5), int(self.height/5)))
        self.horse3img = self.horse3img.resize((int(self.width / 5), int(self.height / 5)))
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
        self.horse1name = "Cavalo Roxo"
        self.horse2name = "Cavalo Verde"
        self.horse3name = "Cavalo Amarelo"

    def game_loop(self):
        while self.running:


            self.clock.tick(self.fps)

            horse1 = pygame.image.load('horse1.png')
            horse2 = pygame.image.load('horse2.png')
            horse3 = pygame.image.load('horse3.png')



            horse1 = pygame.transform.scale(horse1, (horse1.get_width() // 4, horse1.get_height() // 4))
            horse2 = pygame.transform.scale(horse2, (horse2.get_width() // 4, horse2.get_height() // 4))
            horse3 = pygame.transform.scale(horse3, (horse3.get_width() // 4, horse3.get_height() // 4))


            thread1 = threading.Thread(target=self.image_move, args=(horse1, 0, 0,self.horse1name))
            thread2 = threading.Thread(target=self.image_move, args=(horse2, 0, 200,self.horse2name))
            thread3 = threading.Thread(target=self.image_move, args=(horse3, 0, 400,self.horse3name))
            thread4 = threading.Thread(target=self.show_winners)

            thread1.start()
            thread2.start()
            thread3.start()
            thread4.start()

            thread1.join()
            thread2.join()
            thread3.join()
            thread4.join()

            print("AAAAA")






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

    def update(self):
        pass

    def draw(self):


        pass
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
        if winner_horse == self.horse1name:
            winner_horse = self.horse1img
        elif winner_horse == self.horse2name:
            winner_horse = self.horse2img
        elif winner_horse == self.horse3name:
            winner_horse = self.horse3img
        if second_place == self.horse1name:
            second_place = self.horse1img
        elif second_place == self.horse2name:
            second_place = self.horse2img
        elif second_place == self.horse3name:
            second_place = self.horse3img
        if third_place == self.horse1name:
            third_place = self.horse1img
        elif third_place == self.horse2name:
            third_place = self.horse2img
        elif third_place == self.horse3name:
            third_place = self.horse3img

        self.winscreen.paste(winner_horse, (290, 220), winner_horse)
        self.winscreen.paste(second_place, (510, 250), second_place)
        self.winscreen.paste(third_place, (50, 270), third_place)

        #write the name of the winner_horse at the top of the screen using pillow without mask error
        font = ImageFont.truetype("arial.ttf", 48)
        text = self.list[0]
        text_img = PIL.Image.new('RGBA', (370, 200), (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_img)
        draw.text((0, 0), text, (0, 0, 0), font=font)
        self.winscreen.paste(text_img, (200, 85), text_img)

        #write the two random letters and the random number at the top left of the screen
        font = ImageFont.truetype("arial.ttf", 32)
        text = rand_letter+rand_letter2+str(rand_number)
        text_img = PIL.Image.new('RGBA', (370, 200), (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_img)
        draw.text((0, 0), text, (0, 0, 0), font=font)
        self.winscreen.paste(text_img, (0, 0), text_img)

        self.winscreen.save("winscreen.png")






    def game_over(self):
        pass

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



window = Window(800, 600, "The Horse Game - " + rand_letter+rand_letter2 + str(rand_number))
window.game_loop()
window.game_exit()
