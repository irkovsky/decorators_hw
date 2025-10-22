import os
import datetime
import functools


def logger1(old_function):
    
    @functools.wraps(old_function)
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        
        with open('main.log', 'a', encoding='utf-8') as f:
            l = [
                f'Дата записи в файл: {datetime.datetime.now()}\n',
                f'Функция {new_function.__name__}\n',
                f'Позиционные аргументы {args}\n',
                f'Именованные аргументы {kwargs}\n',
                f'Результат: {result}\n\n'
            ]
            
            f.writelines(l)
            
        return result   
    
    return new_function


def logger2(path):
    
    def __logger(old_function):
        
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
        
            with open(path, 'a', encoding='utf-8') as f:
                l = [
                    f'Дата записи в файл: {datetime.datetime.now()}\n',
                    f'Функция {old_function.__name__}\n',
                    f'Позиционные аргументы {args}\n',
                    f'Именованные аргументы {kwargs}\n',
                    f'Результат: {result}\n\n'
                ]
                
                f.writelines(l)
                
            return result

        return new_function

    return __logger


def logger3(path='cls.log'):
    
    def __logger(cls):
        original_init = getattr(cls, '__init__')
        
        def new_init(self, *args, **kwargs):       
            with open(path, 'w', encoding='utf-8') as f:
                l = [
                    f'Дата записи в файл: {datetime.datetime.now()}\n',
                    f'Итератор {cls.__name__}\n',
                    f'Позиционные аргументы {args}\n',
                    f'Именованные аргументы {kwargs}\n\n'
                ]
                f.writelines(l)
            
            original_init(self, *args, **kwargs)
        cls.__init__ = new_init
        
        return cls
    
    return __logger