class User:
    def __init__(self, name, age, money):
        self.name= name
        self._age= age
        self.__money= money
        
    #now i am gonna use a getter
    @property
    def get_age(self):
        return self.__age
    #this don't have any setter so this is a read only
    
    @property
    def salary(self):
        return self.__money
    
    @salary.setter
    def salary(self, money):
        self.__money= money
        if(money < 0 ):
            print("So sad. Be careful next time")
            
        else:
            print("Have a good day ^^ ")
    
    
kakashi= User("Hatake", 29, 3000)

kakashi.salary= 900
print(kakashi.salary)
#getter use korar karone ekhon salary ta function holeo attribute hishabe 
#use kora jacche  
    
    
