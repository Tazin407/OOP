from abc import ABC, abstractclassmethod

class Ride_Sharing:
    def __init__(self,name):
        self.name= name
        self.riders= []
        self.drivers= []
        
    def add_rider(self,rider):
        self.rider= rider
        self.riders.append(rider)
        
    def add_driver(self, driver):
        self.driver= driver
        self.drivers.append(driver)
        
        
class User(ABC):
    def __init__(self,name, email, n_id) -> None:
        self.name= name
        self.email= email
        self.n_id= n_id
        super().__init__()
        
    def display_profile(self):
        raise NotImplementedError
    
class Driver(User):
    def __init__(self, name, email, n_id, current_location) -> None:
        self.current_location= current_location
        self.__wallet= None
        super().__init__(name, email, n_id)
        
    def display_profile(self):
        print(f"Driver {self.name} has been assigned for your ride")
        return super().display_profile()
    
    # def __repr__(self) -> str:
    #     print(self.name)
    #     return super().__repr__()
        
        
class Rider(User):
    def __init__(self, name, email, n_id, current_location) -> None:
        self.wallet= None
        self.current_ride= None
        self.current_location= current_location
        super().__init__(name, email, n_id)
        
    def display_profile(self):
        
        return super().display_profile()    
    
    def request_ride(self,uber,destination):
        if not self.current_ride:
            ob= Ride_Matching(uber.drivers)
            res= ob.has_driver(self,destination)
            self.current_location= res
            print(f"A ride has been booked for {self.name}")
            return True
        else: 
            return False
      
 
 
class Ride():
    def __init__(self,start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver= None
        self.rider= None
        
    def start_ride(self):
        pass
    def end_ride(self):
        pass
    def __repr__(self) -> str:
        print(f"Ride has started from {self.start_location} to {self.end_location}")
       
 
class Ride_Matching:
    def __init__(self,drivers) -> None:
        self.drivers= drivers
        
    def has_driver(self, rider,destination):
        if len(self.drivers) > 0:
            ride= Ride(rider.current_location, destination)
            print(f"Driver {self.drivers[0].name} has been assigned")
            return ride
            
        else :
            print(f"No driver found")
            
            
uber= Ride_Sharing("UBER")
mokbul= Driver("Mokbul", "mokbul23@gmail.com", 23324, "Tokyo")
uber.add_driver(mokbul)

sasuke= Rider("Sasuke Uchiha", "Sasuke@gmail.com", 32423, "Konoha")
uber.add_rider(sasuke)

if sasuke.request_ride(uber, "Moon"):
    print("Enjoy your travel")
    
else:
    print(f"Bad luck this time")