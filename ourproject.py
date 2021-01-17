import pygame

pygame.init()       
Windowx=1000                    # These are global variables for the window size(1000 X 1000)
Windowy=1000
pygame.display.set_caption("Ourproject")   

clock = pygame.time.Clock()
screen = pygame.display.set_mode((Windowx,Windowy))

Colours={"Red":(255,0,0),"Blue":(0,0,255),"Green":(0,255,0),"Grey":(128,128,128),"Black":(0,0,0),"Light Grey":(211,211,211),"White":(255,255,255),"Yellow":(255,255,0)}
# Dictionary for colours

class Character(): # This is the character class that makes a character 
    frame_count=0  #Class variable called frame_count
    alive=True   
    damage_taken=0
    Faceleft=False    
    Faceright=False    
    def __init__(self,y,health,speed,attackanimationleft,attackanimationright): 
        self.x=None
        self.y=y  
        self.health=health
        self.speed=speed   
        self.health_bar_height=5   # These are attributes of the character
        self.health_bar_length=50   
        self.attackanimationleft=attackanimationleft    
        self.attackanimationright=attackanimationright    
    
    def animation(self,frames):  # This is the method that allows each character to have animations. These include walking and attacking
        screen.blit(frames[self.frame_count-len(frames)],(self.x,self.y))   
        self.frame_count+=1   
        if self.frame_count>=len(frames):    
            self.frame_count=0    # This creates a loop
        
    def health_bar(self): # A method to draw a health bar for each character
        Text(str(self.health-self.damage_taken)+"/"+str(self.health),self.x+35,self.y-30,25)
        pygame.draw.rect(screen,Colours["Green"],(self.x+35,self.y-10, self.health_bar_length,self.health_bar_height))    
          
    def execute(self,player): # execute method that puts all the methods together. This is so that later on, the entire object could run with one method
        if self.alive:    
            self.move(player)    
            self.health_bar()  

def Text(words,x,y,size):    # This creates text on the screen.
    font = pygame.font.SysFont("comicans",size,True)    
    text=font.render(str(words),1,Colours["Black"])    
    screen.blit(text,[x,y])  

run = True

while run:# This is the main loop that runs the entire program.
    for event in pygame.event.get():
        position = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
             run=False

    
    keys = pygame.key.get_pressed()
    click = pygame.mouse.get_pressed()


    
