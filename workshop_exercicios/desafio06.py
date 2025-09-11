"""ESTÁ ERRADO!!"""

class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        if isinstance(animal, Animal):
            self.animais.append(animal)
        else:
            print("Erro: Só é possível adicionar instâncias de Animal ou suas subclasses.")

    def listar_animais(self):
        for animal in self.animais:
            print(f"{animal.apresentar()} -> Som: {animal.falar()}")

    def filtrar_por_tipo(self, tipo):
        list_=[]
        for animal in self.animais :
            if isinstance(animal, tipo): 
                list_.append(animal)

        return (list)


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
    

animais = [Gato("Garfield", 5), Cachorro("Cripto", 7)]

for animal in animais:
    print(animal.apresentar(), animal.falar())
