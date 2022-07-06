from repository import Repository
from interfaz import Interfaz

if __name__ == '__main__':
    repo = Repository()
    interfaz = Interfaz()
    repo.add(interfaz.input())

#    for p in repo.find_all():
#        print(p)

    documento = int(input('Documento a buscar: '))
    interfaz.show(repo.find_by_documento(documento))
