'''
Informações sobre o como fazer a atividade:

* O script deverá ter o formato: seunome_sobrenome.py (sem espaços)
  Para pessoas com multiplos sobrenomes, colocar apenas o ultimo.
  Caracteres com acentos devem ser substituidos pelo equivalente sem acento.
  
* Não adicione nada no script fora dos locais onde está escrito :
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    
'''

### Seu código inicia aqui ###

nome = 'lawrence_donizetti_custodio_faccine_junior' # # coloque aqui o nome completo sem espaços (colocar '_' entre as palavras e.g. gustavo_voltani_von_atzingen) no formato de uma string
CPF = '48291015805' # Coloque seu RG no formato int (sem pontos, traços ou espaços) ex: Se '123.456.789.7':  CPF = 1234567897
data_nascimento = '27/06/1997' # Coloque sua data de nascimento no formato 'dd/mm/aaaa' (string)

### Seu código termina aqui ###


def progressao_aritmetica(a1, r, n):
    '''
    Crie uma função que recebe um número inteiro a1, a razão de progressão aritmética r 
    e um número inteiro n > 1 e retorna uma lista com os n primeiros termos da progressão aritmética
    
    PA: https://pt.wikipedia.org/wiki/Progress%C3%A3o_aritm%C3%A9tica 
    
    Test
    -----------
    >>> soma_pa(1, 2, 4)
    [1, 3, 5, 7]
    ''' 
    lista_pa = []
    ### Seu código inicia aqui ###	
    lista_pa.append(a1)
    for i in range(1, n):
        aux = lista_pa[i-1] + r
        lista_pa.append(aux)
    ### Seu código termina aqui ###
    return lista_pa

def soma_pa(a1, r, n):
    '''
    Crie uma função que recebe um número inteiro a1, a razão de progressão aritmética r 
    e um número inteiro n > 1 e retorna a soma dos n primeiros termos da progressão aritmética
    
    PA: https://pt.wikipedia.org/wiki/Progress%C3%A3o_aritm%C3%A9tica 
    
    Return
    -----------
    soma: int
    
    Test
    -----------
    >>> soma_pa(1, 2, 4)
    16
    '''
    soma = 0
    ### Seu código inicia aqui ###	
    lista_pa = []
    lista_pa.append(a1)
    soma = a1
    for i in range(1, n):
        aux = lista_pa[i-1] + r
        lista_pa.append(aux)
        soma = soma + aux
    ### Seu código termina aqui ###
    return soma

def progressao_geometrica(a1, q, n):
    '''
    Crie uma função que recebe um número inteiro a1, a razão de progressão geométrica q 
    e um número inteiro n e retorna uma lista com os n primeiros termos da progressão geométrica
    
    https://pt.wikipedia.org/wiki/Progress%C3%A3o_geom%C3%A9trica 
    
    Test
    -----------
    >>> progressao_geometrica(1, 2, 4)
    [1, 2, 4, 8]
    >>> progressao_geometrica(1, 2, 3)
    [1, 2, 4]
    '''
    pg = []
    ### Seu código inicia aqui ###	
    pg.append(a1)
    for i in range(1, n):
        aux = pg[i-1]*q
        pg.append(aux)
    ### Seu código termina aqui ###
    return pg

def soma_pg(a1, q, n):
    '''
    Crie uma função que recebe um número inteiro a1, a razão de progressão geométrica q > 1
    e um número inteiro n e retorna a soma dos n primeiros termos da progressão geométrica
    
    https://pt.wikipedia.org/wiki/Progress%C3%A3o_geom%C3%A9trica
    
    Test
    -----------
    >>> soma_pg(1, 2, 3)
    7
    >>> soma_pg(1, 2, 4)
    15
    '''
    soma = 0
    ### Seu código inicia aqui ###	
    pg = []
    pg.append(a1)
    soma = a1
    for i in range(1, n):
        aux = pg[i-1]*q
        pg.append(aux)
        soma = soma + aux
    ### Seu código termina aqui ###
    return soma

def fibonacci(n):
    '''
    Crie uma função que recebe um número inteiro n e retorna uma lista com os n primeiros termos da sequência de Fibonacci
    
    https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci  0, 1, 1, 2, 3, 5, 8, ...
    
    Test
    -----------
    >>> fibonacci(4)
    [0, 1, 1, 2]
    >>> fibonacci(2)
    [0, 1]
    '''
    fib = []
    ### Seu código inicia aqui ###	
    fib.append(0)
    for i in range(1, n):
        if(i == 1 or i == 2):
            fib.append(1)
        else:
            fib.append(fib[i-1] + fib[i-2])
    ### Seu código termina aqui ###
    return fib

def soma_fibonacci(n):
    '''
    Crie uma função que recebe um número inteiro n e retorna a soma dos n primeiros termos da sequência de Fibonacci
    
    https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci 0, 1, 1, 2, 3, 5, 8, ...
    
    Test
    -----------
    >>> soma_fibonacci(4)
    4
    >>> soma_fibonacci(5)
    7
    >>> soma_fibonacci(1)
    0
    >>> soma_fibonacci(2)
    1
    '''
    soma = 0
    ### Seu código inicia aqui ###	
    fib = []
    fib.append(0)
    for i in range(1, n):
        if(i == 1 or i == 2):
            fib.append(1)
        else:
            fib.append(fib[i-1] + fib[i-2])
        soma = soma + fib[i]
    ### Seu código termina aqui ###
    return soma

def primo(n):
    '''
    Crie uma função que recebe um número inteiro n e retorna True se ele é primo e False caso contrário
    Test
    -----------
    >>> primo(7)
    True
    >>> primo(8)
    False
    '''
    resultado = False
    ### Seu código inicia aqui ###	
    resultado = True
    for i in range(1, n):
        if(n % i == 0 and i != 1 and i != n):
            resultado = False
            break
    ### Seu código termina aqui ###
    return resultado

def fit_linear(x, y):
    '''
    Crie uma função que recebe duas listas de números x e y e retorna uma lista com os coeficientes da 
    equação linear [A, B], considerando que y = A + B*x
    
    Test
    -----------
    >>> fit_linear([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    [0, 1]
    
    >>> fit_linear([1, 2, 3, 4, 5], [11, 21, 31, 41, 51])
    [1, 10]
    '''
    A, B = 0, 0
    ### Seu código inicia aqui ###
    media_x = 0 	
    media_y = 0
    SS_xy = 0
    SS_xx = 0
    n = len(x)
    for i in range(n):
        media_x = media_x + x[i]
        media_y = media_y + y[i]
        SS_xy = SS_xy + (x[i] * y[i])
        SS_xx = SS_xx + (x[i] * x[i])
    media_x = media_x / n
    media_y = media_y / n
    SS_xy = SS_xy - n*media_y*media_x
    SS_xx = SS_xx - n*media_x*media_x

    B = SS_xy / SS_xx
    A = media_y - B*media_x
    ### Seu código termina aqui ###
    return A, B
