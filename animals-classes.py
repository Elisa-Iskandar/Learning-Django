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
        super().__init__(length, name, weight, noise, friendliness)
        self.wingspan = wingspan
    def fly(self):
        if self.wingspan/self.weight>1:
            if self.wingspan <= self.weight:
                return 'flying, crashing'
            return 'flying'
        else:
            return 'can\'t fly'


snake = animal(name='Sammy',weight=10,length=20,noise='sssss',friendliness=1)

print(snake.speak())
print(snake.play())

giraffe = animal(name= 'Jerry',weight = 50, length=5,noise='hmm',friendliness=7)
dog = animal(name= 'Darius',weight=5,length=0.5,noise='woof',friendliness=10)

pigeon = bird(name = 'Bobby', weight=0.75, length = 0.2, noise='coo', friendliness = 3,wingspan = 0.3)
owl = bird(name = 'Oliver', weight=2, length = 0.2, noise='hoot', friendliness = 2,wingspan = 0.75)
parrot = bird(name = 'Pablo', weight=1, length = 0.2, noise='caw', friendliness = 4,wingspan = 2)



print(pigeon.speak())
print(pigeon.fly())
print(owl.speak())
print(owl.fly())
print(parrot.speak())
print(parrot.fly())
