'''calculator init'''
from decimal import Decimal
from typing import Callable
from apps.calculator.calculations import Calculations
from apps.calculator.operations import add, subtract, multiply, divide
from apps.calculator.calculation import Calculation
# pylint: disable=line-too-long

class Calculator:
    '''class calculator'''
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        '''add'''
        return Calculator._perform_operation(a, b, add)
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        '''subtract'''
        return Calculator._perform_operation(a, b, subtract)
    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        '''multiply'''
        return Calculator._perform_operation(a, b, multiply)
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        '''divide'''
        return Calculator._perform_operation(a, b, divide)
    