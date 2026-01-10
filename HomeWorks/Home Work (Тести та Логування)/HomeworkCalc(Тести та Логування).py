import logging

logging.basicConfig(level=logging.WARNING, filename="logs.log", filemode='w',
    format="We have some error: %(asctime)s : %(levelname)s : %(message)s"
)

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            logging.error("Attempted to divide by zero")
            raise ZeroDivisionError("Division by zero!")
        return a / b

    def maximum(self, a, b):
        return max(a, b)

    def minimum(self, a, b):
        return min(a, b)

    def percent(self, number, pct):
        return (number * pct) / 100

    def power(self, a, b):
        return a ** b
