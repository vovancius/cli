import operator
class Film:
    def __init__(self,name,director,year,budget,time,size):
        self.__name=name
        self.__director=director
        self.__year=year
        self.__budget=budget
        self.__time=time
        self.__size=size
        
    @property
    def name(self):
        return self.__name
    
    @property
    def director(self):
        return self.__director
    
    @property
    def year(self):
        return self.__year
    
    @property
    def budget(self):
        return self.__budget
    
    @property
    def time(self):
        return self.__time
    
    @property
    def size(self):
        return self.__size
    
    @name.setter
    def name(self,value):
        self.__name=value
        
    @director.setter
    def director(self,value):
        self.__director=value
        
    @year.setter
    def year(self,value):
        self.__year=value
        
    @budget.setter
    def budget(self,value):
        self.__budget=value
        
    @time.setter
    def time(self,value):
        self.__time=value
        
    @size.setter
    def size(self,value):
        self.__size=value
        
    def __eq__(self, other):
        return (float)(self.__size) == other
    
    def __gt__(self, other):
        return (float)(self.__size) > other
    
    def __lt__(self, other):
        return (float)(self.__size) < other

    def __ge__(self, other):
        return (float)(self.__size) >= other
    
    def __le__(self, other):
        return (float)(self.__size) <= other
    
    def __str__(self):
        return f"{self.name} {self.director} {self.year} {self.budget} {self.time} {self.size}"

class Storage:
    def __init__(self):
        self.__films=[]

    def add_to_list(self,elems):
        self.__films.append(elems)
    
    def print(self):
        for i in range(len(self.__films)):
            print(f"\nFilm{i}:")
            print(f"Name: {self.__films[i].name}")
            print(f"Director: {self.__films[i].director}")
            print(f"Release Year: {self.__films[i].year}")
            print(f"Budget: {self.__films[i].budget}")
            print(f"Running Time: {self.__films[i].time}")
            print(f"File Size: {self.__films[i].size}")

    def help(self):
        print("Write:\n'--print' to print the list\n'--add' to add elements\n'--sort' to sort by attribute\n'--DbA' to delete by attribute\n'--DbI' to delete by by index\n'--PbA' to print all elements by attribute\n'--exit' to exit")

    def sort(self,attrib):
            self.__films.sort(key=operator.attrgetter(attrib))
            
    def delete_by_index(self,index):
        self.__films.pop(index)
   
    def delete_by_attribute(self,atr1,atr2):
        tmp=[]
        for i in range(len(self.__films)):
            if (getattr(self.__films[i],atr1)!=atr2):
                tmp.append(self.__films[i])
        self.__films=tmp
      
    def print_by_attribute(self,atr1,atr2):
        for film in self.__films:
            if (getattr(film,atr1) == atr2):
                print(film)

    def transformation(self,inp1):
        if inp1 == "Name":
            return "name"
        elif inp1 == "Director":
            return "director"
        elif inp1 == "Release Year":
            return "year"
        elif inp1 == "Budget":
            return "budget"
        elif inp1 == "Running Time":
            return "time"
        elif inp1 == "File Size":
            return "size"

storage=Storage()
try:
    for i in range(5):
        value=[]
        inp=input("Enter: 'Name','Director','Release Year','Budget','Running Time','File Size'(in Gb)\n").split(",")
        for i in range(len(inp)):
            value.append(inp[i])
        film=Film(value[0],value[1],value[2],value[3],value[4],value[5])
        if film > 50:
            print("Can a movie weigh so much?")
        elif (film > 20 and film < 50):
            print("That's pretty big weight!")
        storage.add_to_list(film)
except IndexError:
    print("You typed wrong amount of attributes")
    print("Better luck next time")
    exit()
print("\nWrite '--help' to see commands")
inp=''
while inp != "--exit":
    inp=input()
    
    if inp=="--print":
        storage.print()
        
    elif inp=="--add":
        try:
            value=[]
            inp=input("Enter: 'Name','Director','Release Year','Budget','Running Time','File Size (in Gb)'\n").split(",")
            for i in range(len(inp)):
                value.append(inp[i])
            film=Film(value[0],value[1],value[2],value[3],value[4],value[5])
            storage.add_to_list(film)
        except IndexError:
            print("You typed wrong amount of attributes")
            
    elif inp == "--help":
        storage.help()
        
    elif inp=="--sort":
        try:
            inp1=input("Enter attribute name:")
            storage.sort(storage.transformation(inp1))
        except TypeError:
            print("You typed attribute name not right")
        
    elif inp=="--DbA":
        try:
            atr1=input("Enter attribute name:")
            atr2=input("Enter value:")
            storage.delete_by_attribute(storage.transformation(atr1),atr2)
        except TypeError:
            print("You typed attribute name not right")
            
    elif inp=="--DbI":
        try:
            index=int(input("Enter index of film:"))
            storage.delete_by_index(index)
        except IndexError:
            print("You typed wrong index")
        
    elif inp=="--PbA":
        try:
            atr1=input("Enter attribute name to print:")
            atr2=input("Enter value:")
            storage.print_by_attribute(storage.transformation(atr1),atr2)
        except TypeError:
            print("You typed attribute name not right")
            
    else:
        print("You typed wrong command")

