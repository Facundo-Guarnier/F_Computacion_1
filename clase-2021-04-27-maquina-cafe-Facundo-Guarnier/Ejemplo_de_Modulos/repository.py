from persona import Persona


class Repository:
    def __init__(self):
        self.personas = {}

    @property
    def personas(self):
        return self.__personas

    @personas.setter
    def personas(self, value):
        self.__personas = value

    def find_all(self):
        lista = []
        for persona in self.personas.values():
            lista.append(persona)
        return lista

    def find_by_documento(self, documento):
        return self.personas[documento]

    def add(self, persona):
        self.personas[persona.documento] = persona

    def update(self, persona, documento):
        self.personas[documento] = persona

    def delete(self, documento):
        self.personas.pop(documento)


if __name__ == '__main__':
    r = Repository()
    print(r.find_all())
    r.add(Persona(22222222, 'Jose'))
    for p in r.find_all():
        print(p)
    print('- add')
    r.add(Persona(33333333, 'Maria'))
    for p in r.find_all():
        print(p)
    print('- find_by_documento')
    print(r.find_by_documento(33333333))
    print('- update')
    r.update(Persona(22222222, 'Pepe'), 22222222)
    print(r.find_by_documento(22222222))
    print('- delete')
    for p in r.find_all():
        print(p)
    r.delete(22222222)
    for p in r.find_all():
        print(p)
