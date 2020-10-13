from methods import Dados, create_individual
from classes import Schedule

if __name__ == '__main__':
    print('**Inside Main Script!**\n')
    #1
    dados = Dados()
    mySch = Schedule(dados,0)
    mySch.initialize()
    mySch.print_grid()
    
    ##2
    #dadoss = Dados()
    mySchs = Schedule(dados,1)
    mySchs.initialize()
    mySchs.print_grid()
    
    print('\n**Ending Main Script!**')
    
    
    ##3
    # dadost = Dados()
    # myScht = Schedule(dadost,2)
    # myScht.initialize()
    # myScht.print_grid()
    
    ##another one
    # dados = Dados()
    # mySch = Schedule(dados,0)
    # mySch.initialize()
    # mySch.print_grid()
    # dadoss = Dados()
    # mySchs = Schedule(dadoss,0)
    # mySchs.initialize()
    # mySchs.print_grid()
