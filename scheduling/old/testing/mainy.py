from methods import Dados, create_individual
from classes import Schedule

if __name__ == '__main__':
    print('**Inside Main Script!**\n')
    dados = Dados()
    myInd = create_individual(dados,5)
    print(myInd)
    print('\n**Ending Main Script!**')