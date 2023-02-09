class Computer:

    # What attributes will it need?

    # How will you set up your constructor?
    
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,description,meomery,processor_type, hard_drive_capacity, operating_system,year_made,price):
        self.memory=meomery
        self.description=description
        self.hard_drive_capacity=hard_drive_capacity
        self.processor_type=processor_type
        self.price=price
        self.year_made=year_made
        self.operating_system=operating_system
         # You'll remove this when you fill out your constructor



    # What methods will you need?


    def printdetails(self):
        print(self.description)
        print(self.memory)
        print(self.processor_type)
        print(self.hard_drive_capacity)
        print(self.operating_system)
        print(self.price)    
            
# def main():
#     c=Computer("good",64,"h",67,"u",45,67)
#     c.printdetails()
# main()