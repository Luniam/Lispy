import math
import operator as op

#Explicitly stating Scheme objects
Symbol = str
List = list 
Number = (int, float)
Env = dict


def parse(program):
    '''parse combines tokenize and readFromTokens'''
    return readFromTokens(tokenize(program))


def tokenize(chars):
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()


def readFromTokens(tokens):
    if len(tokens) == 0:
        raise ValueError("Unexpected end of line while parsing")
    token = tokens.pop(0)
    if token == '(':
        L = []
        try :
            while (tokens[0] != ')'):
                L.append(readFromTokens(tokens))
        except IndexError:
            raise ValueError("Unexpected end of line while parsing")
        tokens.pop(0)
        return L
    elif token == ')':
        raise SyntaxError("Missing (")
    else:
        return atom(token)


def atom(token):
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return Symbol(token)


def standardEnv():
    env = Env()
    env.update(math.vars)

program = "(begin (define r 10) (* pi (* r r)))"
program2 = "(define circle-area (lambda (r) (* pi (* r r))))"
print parse(program)
print parse(program2)
