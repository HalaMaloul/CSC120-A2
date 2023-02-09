from computer import * #importing the Computer class

class ResaleShop:

    # What attributes will it need?
    inventory=[]
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):  
        self.inventory=[]
    
    


     # You'll remove this when you fill out your constructor

    # What methods will you need?
    def buy(self,c:Computer):       # add a computer to the inventory (buying a computer)
        self.inventory.append(c)
        

        
        
    def update_price(self,c:Computer,newprice):  #updating a computer's price
        if c in self.inventory:
            c.price=newprice
        else:
            print("this item is not found")

    
    def updateos(self,c:Computer,new_os): #updating a computer's OS
        if c in self.inventory:
            c.operating_system=new_os
        else:
            print("item is not found")
    
    def sell(self,c:Computer): #selling a computer (remove from inventory)
        self.inventory.remove(c)
    
    
    def refurbish(self,c:Computer): #refurbishing a computer
        if c in self.inventory: 
            if int(c.year_made)<2000:
                c.price=0
            elif int(c.year_made)<2012:
                c.price=250
            elif int(c.year_made)<2018:
                c.price=550
            else:
                c.price=1000

          
        else:
            print("item not found,please select another item to refurbish")



    def print_inventory(self,c:Computer): #printing the inventory
        if self.inventory:
         for c in self.inventory:
                c.printdetails()
        else:
                print("No inventory to display")
        
   #call computer constructor
   # to create a new computer instance
def main():

    c=Computer("Mac Pro(late 2013)","3.5GHc 6-Core Intel EXeon E5",1024,64,"macOs Big Sur",2013,1500)
    c2=("good",64,"h",67,"u",45,67)

    myStore=ResaleShop()
    myStore.buy(c)
    print(myStore.inventory)
    myStore.sell(c)
    print(myStore.inventory)
    myStore.refurbish(c)
    myStore.print_inventory(c)
   




main()
