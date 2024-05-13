class Pessoa():
  def __init__(self, name, age):
    self.__name = name # Encapsulation
    self.age= age

  def calc(self, x, y):
    return x * y
  
  def get_name(self):
    return self.__name

  def __str__(self):
    return f"Meu nome é {self.__name} e tenho {self.age} anos"

class Pessoa_2(Pessoa): # Inheritance
  def __init__(self, name, age):
    super().__init__(name, age)
  
  # Override -> Same signature -> Polymorphism
  def calc(self, x, y):
    return x * y * 100
  
class Pessoa_3(Pessoa):
  def __init__(self, name, age, gender):
    super().__init__(name, age)
    self.__gender = gender

  # Overload -> Different signature
  def calc(self, x, y, z):
    return x * y * z
  
  # Overriding the str function, note the way we can get the name parameter versus the age parameter.
  def __str__(self):
    return f"Meu nome é {self.get_name()} e tenho {self.age} anos. Sou {self.__gender}"

joao = Pessoa("joao", 15)
bruno = Pessoa_2("bruno", 20)
higor = Pessoa_3("higor", 12, "m")
print(joao.calc(2,3))
print(bruno.calc(2,3))
print(higor.calc(2,3,4))
print(joao)
print(bruno)
print(higor)
print(joao.__dict__)
print(higor.__dict__)

