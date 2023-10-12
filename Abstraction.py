from abc import ABC, abstractclassmethod

class animal(ABC):
    def __init__(self, name, food) -> None:
        self.name= name
        self.food= food
        
    @abstractclassmethod   
    def eat(self):
        pass
    
    @abstractclassmethod
    def move(self):
        pass
        
        
class Monkey(animal):
    def __init__(self, name, food):
        super().__init__(name, food)
    def eat(self):
        print(f'I like banana')
        
    def move(self):
        print(f'I can jump')
        
Banor= Monkey('Bandor','Kola' )
Banor.eat()
Banor.move()

    

    
