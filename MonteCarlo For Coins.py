##https://www.askpython.com/python/examples/monte-carlo-simulation
#Metodo de Monte Carlo
import random


def unbiased_coin_toss():
    #Realizamos un numero random de 0 a 1
    x = random.uniform(0, 1)
    
     
    if x > 0.5:
        #Cara
        return True
    else:
        #Escudo
        return False
    
    
    
    for i in range(10):
        print(unbiased_coin_toss())
    
N=10
 
results = []

for i in range(N):
    result = unbiased_coin_toss()
    results.append(result)
 
#Ver la cantidad total de veces que se suma cara
n_heads = sum(results)
 
#Probabilidad de las pruebas
p_heads = n_heads/N
 
print("Probability is {:.1f}".format(p_heads))