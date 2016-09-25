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
    env.update(vars(math))
    env.update({
            "+" : op.add, "-" : op.sub, "*" : op.mul, "/" : op.div
        })
    return env

globalEnv = standardEnv()

def eval(x, env = globalEnv):
    print x
    if isinstance(x, Symbol):
        return env[x]

program = "(begin (define r 10) (* pi (* r r)))"
program3 = "(define r 10)"
##program2 = "(define circle-area (lambda (r) (* pi (* r r))))"
print parse(program3)