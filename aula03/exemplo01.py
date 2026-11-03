salario_atual = float(input('Informe o salário: '))
percentual = float(input('Informe o dígito para percentual: '))

percentual = percentual / 100

aumento = salario_atual * percentual
novo_salario = salario_atual + aumento

print(f'\nSalário anterior: {salario_atual}')
print(f'Reajuste de: {aumento}')
print(f'Novo salário: {novo_salario}')
