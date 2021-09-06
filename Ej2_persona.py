
class Persona:
    def greet(self, name: str = 'estudiante')-> None:
        print(f'Hola {name}')

pablo=Persona()
pablo.greet('Jaime')
pablo.greet('Chavo')

