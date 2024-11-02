class spider():
    legs = 8
    head = 1

    def __init__(self,colour,name,web,poisonous):
        self.colour = colour
        self.name = name
        self.web = web
        self.poisonous = poisonous

    def introduce(self):
        print("I am",self.name,"and I am the colour",self.colour)    


sp1 = spider("orange","happy","web","notpoisonous")   
sp2 = spider("green","silly","web","poisonous") 

print(sp1.name)
sp2.introduce()