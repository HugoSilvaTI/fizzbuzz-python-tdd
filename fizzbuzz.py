'''
-- FizzBuzz --

#Regras:
# - Para cada número de 1 a 100:
# - Se o número for divisível por 3, imprimir "Fizz"
# - Se o número for divisível por 5, imprimir "Buzz"
# - Se o número for divisível por 3 e por 5, imprimir "FizzBuzz"
# - Caso contrário, imprimir o próprio número

Metodo (TDD): Red, Green, Refactor'''

def fizzbuzz(numero):
    resultado = "" #String vazia para armazenar o resultado
    if numero % 3 == 0: #Verifica se o número é divisível por 3
        resultado += "Fizz"
    if numero % 5 == 0: #verifica se o número é divisível por 5
        resultado += "Buzz"
    return resultado or str(numero)
    #    - CASO A: Se 'resultado' tiver algo dentro ("Fizz", "Buzz" ou "FizzBuzz"), 
    #      uma string não-vazia é considerada "Verdadeira". Então, o 'or' retorna
    #      o próprio 'resultado'.
    #
    #    - CASO B: Se o número não for múltiplo de 3 nem de 5, 'resultado' continuará
    #      sendo uma string vazia (""). Uma string vazia é considerada "Falsa".
    #      Nesse caso, o 'or' pula para o próximo valor, que é 'str(numero)',
    #      e o retorna.

# --- Bloco para Execução ---
if __name__ == "__main__":
    for numero in range(1, 101):
        resultado_final = fizzbuzz(numero)
        print(resultado_final)

#Para imprimir o resultado final escreva python FizzBuzz.py no terminalPS C:\Users\Hugo Silva\Documents\Workspaces\FizzBuzz>