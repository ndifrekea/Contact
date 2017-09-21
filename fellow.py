class School:
    def __init__(self, eits = [], fellows = []):
        self.eits = eits
        self.fellows = fellows

    def register_eit(self,eit):
        self.eits.append(eit)
        return print("{} this EIT was registered" .format(eit.name))

class Fellow:
    __fellow_count=[]

    def __init__(self, name = "", nationality = "", happiness_level = 0):
        self.name = name
        self.nationality = nationality
        self.happiness_level = happiness_level
        self.__fellow_count.append(self)
        if len(self.__fellow_count) > 4:
            self.__fellow_count.pop(-1)
            raise ValueError("Enyi stop that")
            print(" ")

    def eat(self):
        self.happiness_level += 1

    def teach(self):
        self.happiness_level -= 1

    def get_happiness_level(self):
        print(self.happiness_level)

class Eit:
    def __init__(self, name = "", nationality = "", fun_facts = ""):
        self.name = name
        self.nationality = nationality
        self.fun_fact = fun_facts

    def new_eit(self):
       print("Name: " + self.name,"\nCountry: " + self.nationality,"\nFun Fact: " + self.fun_fact +"\n")


new_fellow= Fellow()
new_fellow2= Fellow()
new_fellow3= Fellow()
new_fellow4= Fellow()
new_fellow5= Fellow()

new_fellow.eat()
new_fellow.eat()

new_fellow.get_happiness_level()

new_student= Eit("Ndifreke","Ghana","I laugh alot")
new_student2=Eit("Mazi","Nigeria", "Jones alot")


new_student.new_eit()

new_student2.new_eit()

register=School()
register.register_eit(new_student)


