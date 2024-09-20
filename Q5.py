# Recebendo a string (pode ser definida manualmente ou digitada)
entrada = input("Digite a string que deseja inverter: ")

# Criando uma string vazia para guardar o resultado
resultado = ""

# Loop para inverter os caracteres
for i in range(len(entrada) - 1, -1, -1):
    resultado += entrada[i]

# Resultado
print("String invertida:", resultado)
