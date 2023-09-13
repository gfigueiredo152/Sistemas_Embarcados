def decimal_to_base(decimal_num, base):
    digits = "0123456789ABCDEF"
    result = ""

    while decimal_num > 0:
        remainder = decimal_num % base
        result = digits[remainder] + result
        decimal_num //= base

    return result

def convert_and_print_steps(decimal_num, base):
    digits = "0123456789ABCDEF"
    steps = []
    intermediate_result = decimal_num

    while intermediate_result > 0:
        remainder = intermediate_result % base
        step = f"{intermediate_result} = {intermediate_result} - {digits[remainder]}*{base}^{len(steps)} = {decimal_to_base(intermediate_result, base)}"
        intermediate_result //= base
        steps.append(step)

    steps.reverse()
    return steps

while True:
    print(" ")
    print("=================================")
    print("Escolha uma opção:")
    print("1. Converter para Hexadecimal")
    print("2. Converter para Octal")
    print("3. Converter para Binário")
    print("4. Sair")

    choice = input("Digite o número da opção desejada: ")

    if choice == '1':
        decimal_input = int(input("Digite um número decimal: "))
        hexadecimal = decimal_to_base(decimal_input, 16)
        print("\nResultado em Hexadecimal:", hexadecimal)
        print("\nPasso a Passo para a conversão para Hexadecimal:")
        steps = convert_and_print_steps(decimal_input, 16)
        for step in steps:
            print(step)

    elif choice == '2':
        decimal_input = int(input("Digite um número decimal: "))
        octal = decimal_to_base(decimal_input, 8)
        print("\nResultado em Octal:", octal)
        print("\nPasso a Passo para a conversão para Octal:")
        steps = convert_and_print_steps(decimal_input, 8)
        for step in steps:
            print(step)

    elif choice == '3':
        decimal_input = int(input("Digite um número decimal: "))
        binary = decimal_to_base(decimal_input, 2)
        print("\nResultado em Binário:", binary)
        print("\nPasso a Passo para a conversão para Binário:")
        steps = convert_and_print_steps(decimal_input, 2)
        for step in steps:
            print(step)

    elif choice == '4':
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Escolha novamente.")
