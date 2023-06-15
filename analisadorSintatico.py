from ply import yacc
from lexer import tokens

# Regras de produção da gramática
def p_statement(p):
    '''
    statement : ID '=' expression
              | expression
    '''
    if len(p) == 4:
        # Atribuição
        p[0] = ('=', p[1], p[3])
    else:
        # Expressão
        p[0] = p[1]

def p_expression(p):
    '''
    expression : expression '+' term
               | expression '-' term
               | term
    '''
    if len(p) == 4:
        # Operação binária
        p[0] = (p[2], p[1], p[3])
    else:
        # Termo
        p[0] = p[1]

def p_term(p):
    '''
    term : term '*' factor
         | term '/' factor
         | factor
    '''
    if len(p) == 4:
        # Operação binária
        p[0] = (p[2], p[1], p[3])
    else:
        # Fator
        p[0] = p[1]

def p_factor(p):
    '''
    factor : '(' expression ')'
           | NUMBER
           | ID
    '''
    if len(p) == 4:
        # Expressão entre parênteses
        p[0] = p[2]
    else:
        # Número ou identificador
        p[0] = p[1]

def p_error(p):
    print(f"Erro de sintaxe: token inesperado '{p.value}'")

# Criação do analisador sintático
parser = yacc.yacc()

# Teste do analisador sintático
input_text = "x = 5 + (3 * 2)"
result = parser.parse(input_text)
print(result)
