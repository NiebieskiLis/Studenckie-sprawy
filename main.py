import random
import numpy as np


def Wybor(saveList,choosenOne) :

    a=random.choice(choosenOne)
    saveList.append(a)
    choosenOne.remove(a)
    print (a)
    return saveList , choosenOne

def Main ():
    savelist = np.genfromtxt("C:/Users/Aleksandra/Downloads/choosenOne - savelist.csv",
                             delimiter=',', dtype=str)
    savelist = savelist[:].tolist()


    choosenOne = np.genfromtxt("C:/Users/Aleksandra/Downloads/choosenOne - choosenone.csv",
                             delimiter=',', dtype=str)
    choosenOne = choosenOne[:].tolist()
    while len(savelist)<=19 :
        savelist, choosenOne = Wybor(savelist, choosenOne)
    np.savetxt('Wynik.csv',savelist ,fmt = '%s',  delimiter='\t', newline='\n')

Main()