# validar-cpf
Exercício de Lógica com Python

Desenvolver um aplicativo que leia um CPF e após a sua validação exiba na tela:
  CPF válido! ou
  CPF inválido!

import re

def validar_cpf(cpf):

    # 1. Limpeza: Remove pontos, traços e espaços, mantendo apenas números
    cpf = re.sub(r'\D', '', cpf)

    # 2. Estrutura de Decisão: Verifica se o tamanho é 11 ou se é uma sequência repetida
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # 3. Cálculo dos Dígitos Verificadores
    for i in range(9, 11):
        # Seleciona os primeiros i dígitos
        digitos = cpf[:i]
        
        # Gera a sequência de multiplicadores (10..2 ou 11..2)
        contador = i + 1
        soma = 0
        
        # Calcula a soma dos produtos
        for digito in digitos:
            soma += int(digito) * contador
            contador -= 1
        
        # Regra do Módulo 11 (resto da divisão)
        resto = soma % 11
        dv = 0 if resto < 2 else 11 - resto
        
        # Adiciona o dígito calculado para a próxima verificação
        cpf = cpf[:i] + str(dv)
    
    # 4. Verificação Final: O CPF calculado é igual ao fornecido?
    return cpf == cpf

#Interface do Aplicativo
if __name__ == "__main__":
    cpf_input = input("Digite o CPF (com ou sem pontuação): ")
    
    # Validação e exibição
    if validar_cpf(cpf_input):
        print("CPF válido!")
    else:
        print("CPF inválido!")

Explicação e Justificativa das Estruturas de Decisão

O uso de estruturas de decisão (if, elif, else) e repetição (for) é crucial para a lógica de validação de CPF, pois o cálculo não é uma operação matemática direta, mas sim uma verificação baseada em regras.

1. if len(cpf) != 11 or cpf == cpf[0] * 11:

Justificativa: Esta é a primeira barreira. Valida se o usuário digitou a quantidade correta de números e evita casos falsos positivos comuns, como "111.111.111-11".

2. for i in range(9, 11):

Justificativa: Esta estrutura de repetição permite reutilizar a mesma lógica matemática para calcular o primeiro dígito verificador (usando os 9 primeiros) e o segundo dígito verificador (usando os 10 primeiros),
tornando o código mais eficiente e compacto.

3. if resto < 2 else 11 - resto

Justificativa: É a aplicação direta da regra da Receita Federal: se o resto da divisão por 11 for menor que 2, o dígito verificador é 0, caso contrário, é 11 menos o resto.

4. if validar_cpf(cpf_input):

Justificativa: Decide qual mensagem exibir ao usuário ("CPF válido!" ou "CPF inválido!") com base no resultado retornado pela função.
