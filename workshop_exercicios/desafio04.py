class Animal:
    def falar(self):
        return ""

class Gato(Animal):
    def falar(self):
        return "Miau!"
    
class Cachorro(Animal):
    def falar(self):
        return "Au au!"
    
def main():
    animais = [Gato(), Cachorro()]

    for animal in animais:
        print(animal.falar())

main()
