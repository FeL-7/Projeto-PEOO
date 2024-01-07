while True:
   try:
       x = int(input('Digite um Número: '))
       y = int(input('Digite outro Número: '))
       print(f'{x}/{y} = {x/y}')
   except ValueError:
       print('Eu disse um número!!!')
   except ZeroDivisionError:
       print('Divisão por Zero Não Pode!!!')
   else:
       break
