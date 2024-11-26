#1) faça uma calculadora com as 4 operações configuradas ( +,-,*,/)

expressao_matematica = input("Digite uma expressão matemática:")

resultado = eval(expressao_matematica)

print("O resultado da expressão matemática é:", resultado)

# para que o enunciado apareça no código, é necessário usar input
# eval vai ser usada sempre para executar qualquer código, como foi
# usado no exercicío acima e isso é perigo, pois ele não mostrará
# caso o código tenha sido digitado errado, em caso de se e se não 
# if - else