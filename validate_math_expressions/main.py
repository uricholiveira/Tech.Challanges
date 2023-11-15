EXPRESSION_ACCEPTED = ['expressão bem formada']
EXPRESSION_NOT_ACCEPTED = ['expressão inválida', False]


def check_expression(expression):
    expression = expression.replace(' ', '')
    expressions = list(expression)
    var_expression = 'xyz'
    var_binary = '+-*/'
    result = []
    for (index, char) in enumerate(expression):
        if char in var_expression:
            #           Verificar se há duas variáveis/expressões consecutivas
            if result and result[-1] in var_expression:
                return EXPRESSION_NOT_ACCEPTED
            if result and result[-1] == ')':
                return EXPRESSION_NOT_ACCEPTED
            result.append(char)
        elif char in var_binary:
            #           Verificar se há dois operadores binários consecutivos
            if result and result[-1] in var_binary:
                return EXPRESSION_NOT_ACCEPTED
            result.append(char)
        elif char == '(':
            # Verificar se não há operador antes do parêntese de abertura
            if result and result[-1] == ')':
                return EXPRESSION_NOT_ACCEPTED
            if result and result[-1] in var_expression:
                return EXPRESSION_NOT_ACCEPTED
            result.append(char)
        elif len(result) < len(expressions):
            result.append(char)
        elif char == ')':
            while result[-1] != '(':
                result.pop()
                if len(result) == 0:
                    return EXPRESSION_NOT_ACCEPTED
            result.pop()
    if len(result) == 0 or ''.join(result).replace(' ', '') == expression.replace(' ', ''):
        return EXPRESSION_ACCEPTED
    return EXPRESSION_NOT_ACCEPTED


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Hello World!')
