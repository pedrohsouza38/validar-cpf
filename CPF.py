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

# --- Interface do Aplicativo ---
if __name__ == "__main__":
    cpf_input = input("Digite o CPF (com ou sem pontuação): ")
    
    # Validação e exibição
    if validar_cpf(cpf_input):
        print("CPF válido!")
    else:
        print("CPF inválido!")