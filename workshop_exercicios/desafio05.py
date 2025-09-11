class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

    def falar(self):
        return ""

class Gato(Animal):
    def falar(self):
        return "Miau!"
    
class Cachorro(Animal):
    def falar(self):
        return "Au au!"
    

animais = [Gato("Garfild", 3), Cachorro("Cripto", 7)]

for animal in animais:
    print(animal.apresentar(), animal.falar())
