""""
CLARA BARBA ARMENGOL

Módulo de gestión de números primos
"""


def esPrimo(numero):
    """
    Devuelve **True** si su argumento es primo, y False si no lo es.
    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    for prueba in range(2, int(numero ** 0.5) + 1):                             
        if numero % prueba == 0: return False

    return True 


def primos(numero):
    """
    Devuelve una **tupla** con todos los números primos menores que su argumento.
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    return tuple([ prueba for prueba in range(2, 50) if esPrimo(prueba) ])


def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    factores = tuple()

    for i in primos(numero+1):
        while numero % i == 0:
            factores = factores + (i,)
           # factores.append(i)
            numero = numero//i

    return factores



def fact2dic(numero1, numero2):
        """
        Pasa de descompon a un diccionario (para facilitar cálcula mcm y mcd)
        """
        diccionario = []
        factores1 = descompon(numero1)
        factores2 = descompon(numero2)
        factores = set(factores1) | set(factores2)
        # crear diccionario vacío
        dic1 = {factor : 0 for factor in factores}
        dic2 = {factor : 0 for factor in factores}
        for factor in factores1:
            dic1[factor] += 1

        for factor in factores2:
            dic2[factor]+= 1
        return dic1, dic2



def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcm(90, 14)
    630
    """
    dic1,dic2 = fact2dic(numero1,numero2)
    mcm = 1
    for factor in dic1:
        mcm = mcm * factor**max(dic1[factor],dic2[factor])
    return mcm


def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    >>> mcd(924, 780)
    12
    """
    dic1, dic2 = fact2dic(numero1, numero2)
    mcd = 1
    for factor in  dic1 | dic2:
        mcd = mcd * factor ** min(dic1[factor],dic2[factor])
    return mcd 

def fact2dicN(*numeros):
        """
        Pasa de descompon a un diccionario (para facilitar cálcula mcmN y mcdN)
        """
        diccionario = []
        for i = 0:
        factores1 = descompon(numeros[i])
        factores = set(factores1) | set(factores2)

        # crear diccionario vacío
        dic1 = {factor : 0 for factor in factores}
        dic2 = {factor : 0 for factor in factores}
        for factor in factores1:
            dic1[factor] += 1

        for factor in factores2:
            dic2[factor]+= 1
        return dic1, dic2


def mcmN(*numeros): 
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    """
    dicN = fact2dicN(*numeros)
    mcmN = 1
    for factor in dicN:
        mcmN = mcmN * factor**max(dicN[factor])
    return mcmN


def mcdN(*numeros): 
    """
    Devuelve el máximo común divisor de sus argumentos
    """
    dicN = fact2dicN(*numeros)
    mcdN = 1
    for factor in  dicN:
        mcdN = mcdN * factor ** min(dicN[factor])
    return mcdN


import doctest
doctest.testmod()
