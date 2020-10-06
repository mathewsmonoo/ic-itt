from methods import Dados, create_individual
from classes import Schedule

if __name__ == '__main__':
    print('**Inside Main Script!**\n')
    dados = Dados()
    mySch = Schedule(dados,0)
    mySch.initialize()
    mySch.print_grid()
    dadoss = Dados()
    mySchs = Schedule(dados,1)
    mySchs.print_grid()
    mySchs.initialize()
    print('\n**Ending Main Script!**')
    
"""
    dados = Dados()
    mySch = Schedule(dados,0)
    mySch.initialize()
    mySch.print_grid()
    dadoss = Dados()
    mySchs = Schedule(dadoss,0)
    mySchs.initialize()
    mySchs.print_grid()
"""