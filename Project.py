import random


class student:
    def __init__(self, name):
        self.name = name
        self.gladness=50
        self.progress=0
        self.hungry=1
        self.alive=True
    def to_Study(self):
        print("time to study")
        self.progress+=0.12
        self.gladness-=5
        self.hungry += 1
    def to_sleep(self):
        print("Time to sleep")
        self.gladness+=3
        self.hungry += 1
    def rest(self):
        print("Time to rest")
        self.gladness+=5
        self.progress-=3

    def hungry(self):
        print("Time to eat")
        self.hungry-=1
        self.gladness+=1
    def is_alive(self):
        if self.progress<-0.5:
            print("Cast out...")
            self.alive=False
        elif self.gladness <= 0:
            print("Depression")
            self.alive=False
        elif self.progress>5:
            print("He improve yourself")
            self.alive=True
        elif self.hungry>3:
            print("Ваня съел математичку")
            self.alive = False
    def end_of_the_Day(self):
        print(f"Gladness={self.gladness}")
        print(f"Progress={self.progress}")
        print(f"Hungry={self.hungry}")
    def live(self,day):
        day= "Day"+str(day)+"of"+self.name+"life"
        print(f"{day:=^50}")
        live_cute=random.randint(1,3)
        if live_cute==1:
            self.to_Study()
        elif live_cute==2:
            self.to_sleep()
        elif live_cute==3:
            self.rest()
        self.end_of_the_Day()
        self.is_alive()
nick= student(name="Nick")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)

"""    print("Hello")
    def __init__(self, height= 160):
        self.height=100
        self.height=height
        print("i`m Kok")
nick= student()
kate= student(height=170)
print(nick.height)
print(kate.height)"""