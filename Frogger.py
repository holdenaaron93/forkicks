#pygame dev 1
#start game set up
#set up display


import pygame

#Size of Screen
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Aaron's Super Awesome Game"
#RGB Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans',75)

truck_speed = 10
car_speed = 15
racecar_speed = 15




class Game:
    TICK_RATE = 60
    
    def __init__(self,title,width,height):
        self.title = title
        self.width = width
        self.height = height
        #Creates Window 
        self.game_screen = pygame.display.set_mode((width,height))
        self.game_screen.fill(WHITE)
        pygame.display.set_caption(self.title)
        self.background = pygame.image.load('background.jpg')
        self.background = pygame.transform.scale(self.background,(self.width,self.height))
        
         

    def run_game_loop(self,level):
        is_game_over = False
        did_win = False
        y_direction = 0
        x_direction = 0
        #Game Loop
        #Updates all gameply such as movement, checks, and graphics
        #Runs until is_game_over = True

        #set up characters
        frogger = PlayerCharacter('frogger.jpg', self.width/2,self.height,50,50)
        car = EnemyCharacter('car_1.png',-50,400,50,50)
        racecar = EnemyCharacter('car_2.png',self.width+70,200,50,50)
        truck = EnemyCharacter('truck.png',-50,535,80,50)

        
        while not is_game_over:
            #a loop to check all events (mouse clicks/movement, keys etc.)
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    is_game_over = True
                    #dectect when any key is pressed down
                elif event.type == pygame.KEYDOWN:
                    #detect if key is down arrow/uparrow and change direction
                    if event.key == pygame.K_UP:
                        y_direction = 1
                    elif event.key == pygame.K_DOWN:
                        y_direction = -1
                    if event.key == pygame.K_RIGHT:
                        x_direction = 1
                    elif event.key == pygame.K_LEFT:
                        x_direction = -1
                    #detect if a key is up
                elif event.type == pygame.KEYUP:
                    #if the up key is the down/up arrow change direction
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_direction = 0
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        x_direction = 0


              
            self.game_screen.fill(WHITE)
            self.game_screen.blit(self.background,(0,0))
            
            #direction to calc up or down
            #self.height to create boundries
            frogger.move(x_direction,y_direction,self.width,self.height)
            frogger.draw(self.game_screen)
            
            car.move(self.width,car_speed)
            car.draw(self.game_screen)

            
            print(racecar.x_pos)
            print(level)
            if level > 1:
                racecar.move(self.width,racecar_speed)
                racecar.draw(self.game_screen)
            if level > 2:
                truck.move(self.width,truck_speed)
                truck.draw(self.game_screen)
            
            


            # End game if collision is detected or Frogger crosses road
            if frogger.detect_collision(car):
                is_game_over = True
                did_win = False
                text = font.render('SQUIISH!', True, RED)
                self.game_screen.blit(text,(350,250))
                pygame.display.update()
                clock.tick(1)
                break
            if frogger.detect_collision(racecar):
                is_game_over = True
                did_win = False
                text = font.render('SQUIIISH!', True, RED)
                self.game_screen.blit(text,(350,250))
                pygame.display.update()
                clock.tick(1)
                break
            if frogger.detect_collision(truck):
                is_game_over = True
                did_win = False
                text = font.render('SQUIISH!', True, RED)
                self.game_screen.blit(text,(350,250))
                pygame.display.update()
                clock.tick(1)
                break
            if frogger.y_pos <=45:
                is_game_over = True
                did_win = True
                text = font.render('You win!', True, BLACK)
                self.game_screen.blit(text,(350,250))
                pygame.display.update()
                clock.tick(1)
                break
            
            
            #updates all game graphics
            
            pygame.display.update()
            clock.tick(self.TICK_RATE)

        if did_win:
            level += 1
            self.run_game_loop(level)
        else:
            return

class GameObject:
##Treasure
##player
##enemy
    def __init__(self,image_path, x,y,width,height):
        object_image = pygame.image.load(image_path)
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height
        object_image = pygame.image.load(image_path)
        #scale image
        self.image = pygame.transform.scale(object_image,(width,height))
        if self.x_pos < 350:
            self.direction = 1
        if self.x_pos > 350:
            self.direction = -1


    def draw(self,background):
        background.blit(self.image, (self.x_pos,self.y_pos))

    


class PlayerCharacter(GameObject):
    #how many tiles the character moves per second
    SPEED = 10

    def __intit__(self, image_path, x, y, width, height):
        super().__init__(self,image_path, x,y,width,height)

    #move function will move character up if direction is > 0
    #Sets bounds for image location
    def move(self,x_direction, y_direction,max_width, max_height):
        if y_direction  > 0:
            self.y_pos -= self.SPEED
        elif y_direction < 0:
            self.y_pos += self.SPEED
        if x_direction > 0:
            self.x_pos += self.SPEED
        elif x_direction < 0:
            self.x_pos -= self.SPEED
            
        #Set screen bounds on Frogger
            #y bounds
        if self.y_pos > max_height - 70:
            self.y_pos = max_height - 70
        if self.y_pos < 20:
            self.y_pos = 20
            #x bounds
        if self.x_pos > max_width - 70:
            self.x_pos = max_width - 70
        if self.x_pos < 20:
            self.x_pos = 20

    #returns True when there is a detection            
    def detect_collision(self, other_body):
        #approching from bottom
        if self.y_pos >= other_body.y_pos + other_body.height:
            return False
        #approaching from top
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        #approaching form right
        if self.x_pos + self.width < other_body.x_pos:
            return False
        #approaching from left
        elif self.x_pos > other_body.x_pos + other_body.width:
            return False

        return True
    

class EnemyCharacter(GameObject):

    def __intit__(self, image_path, x, y, width, height):
        super().__init__(self,image_path, x,y,width,height)

        
    
    def move(self, width,SPEED):

        if self.direction > 0:
            self.SPEED = abs(SPEED)
            if self.x_pos > width:
                self.x_pos = -50
        elif self.direction < 0:
            self.SPEED = -abs(SPEED)
            if self.x_pos + self.width < 0:
                self.x_pos = width +50
            #adds 5 units to locatoin for every loop passed
        self.x_pos += self.SPEED


##    def move(self,width):
##        if self.x_pos  <= 0:
##            while self.x_pos <= width:
##                self.SPEED = abs(self.SPEED)
##        elif self.x_pos >= width:
##            while self.x_pos > - 50:
##                self.SPEED = -abs(self.SPEED)
##        self.x_pos += self.SPEED
            
        
        
        
        
        
pygame.init()
new_game=Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop(1)
pygame.quit()
quit()
