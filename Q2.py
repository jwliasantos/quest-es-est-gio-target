#QUESTÃO 2
def fibonacci(n):
    # Cria a sequência de Fibonacci
    fib_sequence = [0, 1]  
    while fib_sequence[-1] < n:  
        next_value = fib_sequence[-1] + fib_sequence[-2]  
        fib_sequence.append(next_value)  
    
    return fib_sequence  

# Coloque um número desejado no terminal
numero = int(input("Informe um número: "))
sequencia = fibonacci(numero)  

# Para checar se o número faz parte da sequência
if numero in sequencia:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

#Alguns números pertencentes: 1,2,3,5...
#Alguns números não pertencentes: 4,6,7...