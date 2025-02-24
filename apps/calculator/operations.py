'''operations'''
from decimal import Decimal

def add(a: Decimal, b: Decimal)-> Decimal:
    '''add'''
    return a + b
def subtract(a: Decimal, b: Decimal)-> Decimal:
    '''subtract'''
    return a - b
def multiply(a: Decimal, b: Decimal)-> Decimal:
    '''multiply'''
    return a * b
def divide(a: Decimal, b: Decimal)-> Decimal:
    '''divide'''
    if b==0:
        raise ValueError("Unable to divide by 0")
    return a / b
