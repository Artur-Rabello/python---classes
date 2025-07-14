class Calculadora:
  def soma(self, x, y):
      return x + y
  
  def sub(self, x, y):
      return x - y
  
  def mult(self, x, y):
      return x * y
  
  def div(self, x, y):
      return x / y

op = input("qual a operacao +, -, *, /: ")
num1 = int(input("digite o primeiro valor: "))
num2 = int(input("digite o segundo valor: "))

calc = Calculadora()

if op == "+":
  resultado = calc.soma(num1, num2)
  print(resultado)

elif op == "-":
  resultado = calc.sub(num1, num2)
  print(resultado)

elif op == "*":
  resultado = calc.mult(num1, num2)
  print(resultado)

elif op == "/":
  resultado = calc.div(num1, num2)
  print(resultado)

else:
   print("insira uma operacao valida")