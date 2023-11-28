import random

class animal:
    def __init__(self,length=0, name='Unnamed', weight=0, noise='', friendliness=0):
        self.length = length
        self.name = name
        self.weight = weight
        self.noise = noise
        self.friendliness = friendliness
    def speak(self):
        return self.noise
    def play(self):
        num = random.randint(1,10)
        if num>self.friendliness:
            return 'run away'
        elif num<=self.friendliness:
            return 'play'

class bird(animal):
    def __init__(self, length=0, name='Unnamed', weight=0, noise='', friendliness=0,wingspan = 0):
        super().__init__(length,name,weight,noise,friendliness)
        self.wingspan = wingspan

snake = animal(name='Sammy',weight=10,length=20,noise='sssss',friendliness=1)

print(snake.speak())
print(snake.play())

giraffe = animal(name= 'Jerry',weight = 50, length=5,noise='hmm',friendliness=7)
dog = animal(name= 'Darius',weight=5,length=0.5,noise='woof',friendliness=10)

pigeon = bird(name = 'Bobby', weight=1, length = 0.2, noise='coo', friendliness = 3,wingspan = 0.5)

print(pigeon.speak())
