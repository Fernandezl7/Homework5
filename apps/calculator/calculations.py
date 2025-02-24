'''calculations'''
from typing import List
from apps.calculator.calculation import Calculation

class Calculations:
    '''calculations class'''
    history: List[Calculation] = []
    @classmethod
    def add_calculation(cls, calculation: Calculation):
        '''classmethod add'''
        cls.history.append(calculation)
    @classmethod
    def get_history(cls)-> List[Calculation]:
        '''get history'''
        return cls.history
    @classmethod
    def clear_history(cls):
        '''clear history'''
        cls.history.clear()
    @classmethod
    def get_latest(cls)-> Calculation:
        '''get latest'''
        if cls.history:
            return cls.history[-1]
        return None
    @classmethod
    def find_by_operation(cls,operation_name: str) -> List[Calculation]:
        '''find by operation'''
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
        