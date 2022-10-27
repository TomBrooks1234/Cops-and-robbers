from superwires import games,color
import random, pickle

games.init(screen_width = 640, screen_height = 480, fps = 50) #creating game window 


class Robber(games.Sprite): #creating window class and inherting sprite class from superwires games programm
    
    image = games.load_image("robberrr2.png") #load robbers image 

    def __init__(self, x = games.screen.width/2,
                                y = games.screen.height/2,):
        """ Initialize Robber object and create Text object for score. """
        super(Robber, self).__init__(image = Robber.image,
                                  x = games.screen.width/2,
                                  y = games.screen.height/2
                                  )

        self.score = games.Text(value = 0, size = 25, color = color.black, # creating score counter
                                top = 5, right = games.screen.width - 10,
                                is_collideable = False)
        games.screen.add(self.score) #adding counter to sccreen

    
    

    def update(self): #creating method so user can move robber 
        """ Takes keyboard inputs to move the robber sprite. """
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x = (self.x)-4

        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x = (self.x)+4

        if games.keyboard.is_pressed(games.K_UP):
            self.y = (self.y)-4

        if games.keyboard.is_pressed(games.K_DOWN):
            self.y = (self.y)+4
        self.check_collide()

#if the robber is at the end of the window he will stay there and not go of the screen 

        if self.x<0:
            self.x = 0 
        elif self.x > games.screen.width:
            self.x = games.screen.width

        if self.y<0:
            self.y = 0
        elif self.y > games.screen.height:
            self.y = games.screen.height
 
    def check_collide(self):
        """ Check for collision with money bag """
        for bag in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            bag.handle_collide()

    def end_game(self):
        """ End the game. """
        
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)
        
    def handle_collide(self):
        """"controls what happen when the robber colides with the cops """
        self.destroy()
        self.end_game()
        
        global highScore 
        highScore = self.score.value # setting high score of the game to the final score before robber dies 
        loadGui() #loads graphical leaderboard 


class Money_bag(games.Sprite): #creates money bag class inherits sprite class from superwires 
    
    image = games.load_image("money bagg1.png") #loads money bag image 

    def __init__(self, x=300, y = 90):
        
        super(Money_bag, self).__init__(image = Money_bag.image,
                                    x = x, y = y)
    
    def handle_collide(self):
        """ Move to a random screen location after colliding with robber """
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)


class Cop(games.Sprite):
    """Cop class"""
    
    image = games.load_image("coper2.png") #load cop image 

    def __init__(self,x,y):
        
        super(Cop, self).__init__(image = Cop.image,
                                  x=x,
                                  y=y,
                                  bottom = games.screen.height,
                                  dx=2,dy=2,
                                  )

    def update(self):
        """random movment algorithm for cop"""
        self.x =self.x
        self.y = self.y
        odds_change= 75 #set random movent chance 
        odds_change2 = 200

        #stop the cop from moving of the screen 
        if self.x<0:
            self.dx= -self.dx 
        elif self.x > games.screen.width:
            self.dx = -self.dx
    
        if self.y <0:
            self.dy = -self.dy
        elif self.y > games.screen.height:
            self.dy = -self.dy

#algorithm to make the cop move randomly round the screen 
        elif random.randrange(odds_change) == 0:
            if self.dx == 0:
                num= random.randint(0,1)
                if num ==0:
                    self.dx =2
                elif num == 1:
                    self.dx = -2
            self.dx = -self.dx

        elif random.randrange(odds_change2) == 0:
           self.dx = 0

        elif random.randrange(odds_change) == 0:
            if self.dy == 0:
                num= random.randint(0,1)
                if num ==0:
                    self.dy =2
                elif num == 1:
                    self.dy = -2
            self.dy = -self.dy

        elif random.randrange(odds_change2) == 0:
           self.dx = 0
           
        self.check_collide()
        


    def check_collide(self):
        #check to see if in contact with robber 
        for sprite in self.overlapping_sprites:
            
            sprite.handle_collide()


    def handle_collide(self):
        is_collidable = False 

    

def main():
    city_image = games.load_image("city.jpg", transparent = False) #loads background image 
    games.screen.background = city_image #adds background image to window 

    Robberr = Robber() #creates robber object 
    games.screen.add(Robberr) #adds robber to screen
    
    
    
    MoneyBag = Money_bag() #creates money bag object 
    games.screen.add(MoneyBag) #adds money bag to screen
    
    copper= Cop(x=1,y=1) #creates cop objects 
    copper2 =Cop(x=639,y=479)
    games.screen.add(copper) #adds cop objects to screen 
    games.screen.add(copper2)

    games.mouse.is_visible = False

    games.screen.event_grab = True
    
    games.screen.mainloop()


from tkinter import *

class Application(Frame):
    """ creating graphical user interface class """ 
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)  
        self.grid() #creates grid for window so i can position widgets 
        self.create_widgets() # initiates screat widget method 

    def create_widgets(self):
        #creates label to tell user to enter name 
        self.name_lbl = Label(self, text = "Enter player name")
        self.name_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # create label for password      
        self.pw_lbl = Label(self, text = "Name: ")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)

        # create entry widget to accept user name     
        self.name_ent = Entry(self)
        self.name_ent.grid(row = 1, column = 1, sticky = W)

        #creates submit button which when pressed loads leaderboard 
        self.submit_bttn = Button(self, text = "Submit", command = self.create_widgets1)
        self.submit_bttn.grid(row = 2, column = 2, sticky = W) 

        #creates space for leaderboard 
        self.leaderboard = Text(self, width = 35, height = 15, wrap = WORD)
        self.leaderboard.grid(row = 3, column = 0, columnspan = 2, sticky = W)

        
    def create_widgets1(self):
        """ Create button, text, and entry widgets. """

        name = self.name_ent.get() # gets name input from name entry box
        numb = int(highScore) #sets high score number as an integer 

        add = [name,numb] #creates list with user name and high score 

        openf = open('file', 'ab') #opens external file
        pickle.dump(add, openf) #saves new high score to file

        openf.close() #closes file 

        #printing list 
        pkl_file = open('file', 'rb')

        llist=[[]] #creates 2d list tp store leaderboard 
    
        for x in range(6): #loop to read pickle file 
            line =pickle.load(pkl_file)
            if x ==0:
                llist[0]=line #stores file lines to 2d list 
            else:
                llist.append(line)

        slist = sorted(llist,key=lambda l:l[1], reverse=True) #orders list 

        #re writting list with 5 top scores 
        output = open('file', 'wb')
        for x in range (5):
            pickle.dump(slist[x], output)

        output.close()

        pkl_file.close()

        pkl_file = open('file', 'rb')
        #reading new top 5 scores 
        llist=[[]]
        
        for x in range(5):
            line =pickle.load(pkl_file)
            if x ==0:
                llist[0]=line
            else:
                llist.append(line)
        
        # adds high scores list to leaderboard 
        
        leaderB = "leaderboard \n",llist[0][0],llist[0][1],"\n",llist[1][0],llist[1][1],"\n",llist[2][0],llist[2][1],"\n",llist[3][0],llist[3][1],"\n",llist[4][0],llist[4][1],"\n"
                                    
        self.leaderboard.delete(0.0, END) #clears existing leaderboard text 
        self.leaderboard.insert(0.0, leaderB) #adds high scores to leader board

def loadGui():
    root = Tk() #create root window
    root.title("Leaderboard") #naming root window
    root.geometry("640x480") #setting size of window 

    app = Application(root) #creating window 

    root.mainloop() #event loop for gui
    
main()


