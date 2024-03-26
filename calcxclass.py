class Calculator:

    @staticmethod
    def summa(a, b):
        return a + b

    @staticmethod
    def difference(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return a / b


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))


calc = Calculator()


result_sum = calc.summa(a, b)
result_diff = calc.difference(a, b)
result_mult = calc.multiplication(a, b)
result_div = calc.division(a, b)

print("Summa:", result_sum)
print("Difference:", result_diff)
print("Multiplication:", result_mult)
print("Division:", result_div)



