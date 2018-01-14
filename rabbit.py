import random

class Rabbit:
    """A class for Rabbits meant for running Monte Carlo Simulations on Population"""

    def __init__(self, gender=2):
        # we can't assume that the random number generator was seeded
        # random.seed()   # we'll just use the timer to seed the pseudo-random number generator 
        # Note:  moved seeding to the Warren class
        # print ("Creating Rabbit")  #debug
        if gender not in (0,1):
            self.sex=random.randint(0,1)  # female 1, male 0
        else:
            self.sex=gender
        self.age=1  # can't breed until age 3
        self.alive=True
        self.mortality=10

    def getOlder(self):
        if self.alive==True:    # We only need to age living rabbits.  
            self.age+=1
            self.mortality+=10

    def hasLitter(self):
        return random.randint(2, 12) 

    def hasDied(self):
        test=random.randint(1,100)
        if test<=self.mortality:
            self.alive=False


class Warren:
    """A class for working with lists of Rabbits"""

    def __init__(self):
        random.seed()
        self.w=[]      # This is our list of Rabbits
        a=Rabbit(gender=0)  # All Warrens start with a male and female rabbit
        b=Rabbit(gender=1)
        self.w.append(a)
        self.w.append(b)

    def allAlive(self):
        """Check that there is at least one living male and one living female Rabbit"""
        maleAlive=False
        femaleAlive=False
        for i in self.w:        # I realize there are more efficient ways to do do this, but I was in a hurry
            if i.alive and i.sex==0:
                maleAlive=True
            if i.alive and i.sex==1:
                femaleAlive=True
            if maleAlive and femaleAlive:
                break
        return (maleAlive and femaleAlive)
        
    def litter(self):
        for i in self.w:
            if i.sex==1 and i.age>2 and i.alive:   # Alive, female, and older than 2 generations means litter
                count=i.hasLitter() 
                for j in range(count):
                    x=Rabbit()
                    self.w.append(x)
                    
    def countRabbits(self):
        count=0
        for i in self.w:
            if i.alive:
                count+=1
        return count

    def nextGen(self):
        """The main method for a generation of Rabbits"""
        
        # Check to make sure the rabbits aren't all dead
        # And that we have at least one male and one female
        if not self.allAlive():  # This is a fail condition
            return -1

        # Age everyone
        for i in self.w:
            i.getOlder()
            
        # Create Litters
        self.litter()
        
        # Kill Rabbits
        for i in self.w:
            i.hasDied()
            
        return self.countRabbits()  # return with the number of rabbits
            
        


if __name__=='__main__':
    a=Rabbit(gender=0)
    b=Rabbit(gender=1)
    print (a.sex, " ", b.sex)
    numRabbits=1500
    l=[]
    for i in range (numRabbits):
        x=Rabbit()
        l.append(x)
    femaleCount=0
    maleCount=0
    for i in l:
        if i.sex:
            femaleCount+=1
        else:
            maleCount+=1
    print("Female: ", femaleCount, ", ", ((femaleCount*1.0)/(numRabbits*1.0))*100,"%")
    print("Male: ", maleCount, ", ", ((maleCount*1.0)/numRabbits*1.0)*100,"%")

    r=Warren()
    for i in r.w:
        print (i.sex)