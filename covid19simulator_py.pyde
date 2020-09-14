# get a ball bouncing aroung the screen
# get lots of balls bouncing around the screen
# get people moving aroung infecting each other
# https://www.youtube.com/watch?v=T3TD_fD3AFk

w = 800
h = 800
number_of_people = 30

class Ball(object):
    global w,h
    
    def __init__(self,x_,y_,vx_,vy_):
        self.x=x_
        self.y=y_
        self.vx=vx_
        self.vy=vy_
    
    def move(self):
        if self.x < 0 or self.x > w:
            self.vx *= -1
        if self.y < 0 or self.y > h:
            self.vy *= -1
        self.x += self.vx
        self.y += self.vy
            
    def display(self):
        fill(127)
        ellipse(self.x,self.y,10,10)

class Person(Ball):
    global people, number_of_people
    
    def __init__(self,id_,x_,y_,vx_,vy_,status_):
        super(Person,self).__init__(x_,y_,vx_,vy_)
        self.id = id_
        self.status = status_
    
    def display(self):
        if self.status == "unexposed":
            fill(127)
        elif self.status == "infected":
            fill(255,0,0)
        ellipse(self.x,self.y,10,10)
        
    def collide(self):
        for i  in range(self.id+1, number_of_people):
            dx = self.x - people[i].x
            dy = self.y - people[i].y
            dist_squared = dx*dx + dy*dy
            if dist_squared < 200:
                #print("collision",self.id,i)
                if self.status == "infected" and people[i].status == "unexposed":
                    people[i].status = "infected"
                elif self.status == "unexposed" and people[i].status == "infected":
                    self.status = "infected"

people = []
for i in range(number_of_people):
    people.append(Person(i,random(w),random(h),random(-10,10),random(-10,10),"unexposed"))
people[0].status="infected"

def setup():
    global w, h
    size(w,h)
    background(32)
    noStroke()
    
def draw():
    background(32)
    for i in range(number_of_people):
        people[i].move()
        people[i].collide()
        people[i].display()
