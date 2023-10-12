
class shopping:
    cart=[]# class er attribute. etai instance attribute
    def __init__(self,name, location) -> None:
        self.name= name
        self.location= location
        
    @staticmethod
    #eta static. tai ekhane self lagbe na. static kono self wala attribute ke 
    #access o korte parbe na. etar jonno kono instance(object) o lagbe na.
    def multiply(a,b):
        print(a*b)
    @classmethod
    
    def buy(self, product):
        print(f'I wanna buy {product}')   
  
  
shopping.buy('Bottle')  
shopping.multiply(3,3)