import re

NUM_OR_DOT = re.compile(r'^[0-9.]$') # Somente numeros de 0-9 e o "."
SPECIAL_KEYS = r"^[<C=]" # Caracteres dos botões especiais "<" "C" "="
ACCEPT_KEYS = r"^\d*\.?\d+([+\-*/^]\d*\.?\d+)*$" # Caracteres que serão permitidas no display
# Caracteres exibidos no display separados em grupos = num / operator / num
ACCEPT_KEYS_GROUPS = r"^(\d*\.?\d+)([+\-*/^])(\d*\.?\d+)*$" 



def isNumberOrDot(string):
    '''Verificar se é numero ou "."
    return: True | False
    '''
    return bool(NUM_OR_DOT.search(string))


def numberEquation(string):
    ''' Tranforma o texto em num / operator / num

    return:
        Retorna os numeros antes do operador
        O operador
        Os numeros depois do operador
    
    '''
    if string in '+-/*^':
        return None, string, None
    result = re.match(ACCEPT_KEYS_GROUPS, string)
    left_number = result.group(1)
    operator = result.group(2)
    right_number = result.group(3)
    return left_number, operator, right_number

def onlyNumer(string):
    ''' Pegar somente os números de um texto'''
    result = re.findall(r'\d+\.?\d*', string)
    return result[0]

def isSpecialKeys(string):
    '''Verifica se é um caracter de um botão especial'''
    specialKeys = re.compile(SPECIAL_KEYS)
    result = re.findall(specialKeys, string)
    return bool(result)
