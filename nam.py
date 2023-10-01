"""Task 1"""


# def validate_numeric(func):
    
#     def inner(*args, **kwargs):
        
#         for i in args:
            
#             if not isinstance(i, (int, float)):
                
#                 return 'The input arguments must be numeric'
                
#         for e , i in kwargs.items():
            
#             if not isinstance(i, (int, float)):
#                 return 'The input arguments must be numeric'
        
        
#         return func(*args, **kwargs)
    
#     return inner



# @validate_numeric
# def sum(a, b):
#     """Return the sum of two numbers."""
#     return a + b

# print(sum(1, 2))
# print(sum(1, "2"))
# print(sum(a=1, b="a"))
# print(sum(a=1, b=3.4))




"""Task 2"""


# def validate_numeric(func):
    
#     def inner(*args, **kwargs):
        
#         for i in args:
            
#             if not isinstance(i, (int, float)):
                
#                 return 'The input arguments must be numeric'
                
#         for e , i in kwargs.items():
            
#             if not isinstance(i, (int, float)):
#                 return 'The input arguments must be numeric'
        
        
#         return func(*args, **kwargs)
    
#     return inner

# def debug(func):
    
#     def wrapped(*args, **kwargs):
        
#         print('**********')

#         if args:
            
#             reform_args = ','.join(str(i) for i in args)
            
#             print(f'Positional arguments: {reform_args}')
#             print('There are no keyword arguments')
            
            
            
        
#         elif kwargs:
            
#             reform_kwargs = ','.join(f'{str(key)}={str(value)}' for key, value in kwargs.items())
            
#             print('There are no positional arguments')
#             print(f'Positional arguments: {reform_kwargs}')
            
            
#         try:     
            
#             print(f'Result: {func(*args, **kwargs)}')
        
#         except TypeError:
            
#             print(f'Result: The input arguments must be numeric')
        
#     return wrapped    



# @debug
# def sum(a, b):
#     """Return the sum of two numbers."""
#     return a + b


# sum(1, 2)
# sum(a=1, b=2)
# sum(1, "a")

# sum(1, 2)
# sum(1, "2")
# sum(a=1, b="a")
# sum(a=1, b=3.4)

#----------------------------------------------------------------

# def debug(func):
    
#     def wrapped(*args, **kwargs):
        
#         print('**********')

#         if args:
            
#             reform_args = ','.join(str(i) for i in args)
            
#             print(f'Positional arguments: {reform_args}')
#         else:
#             print('There are no positional arguments')
            
            
#         if kwargs:
            
#             reform_kwargs = ','.join(f'{str(key)}={str(value)}' for key, value in kwargs.items())
            
#             print(f'Keyword arguments: {reform_kwargs}')
#         else:
#             print('There are no keyword arguments')
            
            
#         try:     
            
#             print(f'Result: {func(*args, **kwargs)}')
        
#         except TypeError:
            
#             print(f'Result: The input arguments must be numeric')
        
#     return wrapped    



# @debug
# def sum(a, b):
#     """Return the sum of two numbers."""
#     return a + b


# sum(1, 2)
# sum(a=1, b=2)
# sum(1, "a")

# sum(1, 2)
# sum(1, "2")
# sum(a=1, b="a")
# sum(a=1, b=3.4)



"""Task 3"""

# {<function sum at 0x7fcd34ced840>: {(1, 2): 3,(3, 2): 5}} 
# cache_dict[func][args] = func(*args)

def cache(func):
    
    cache_dict = {}
    
    def wrapped(*args):
        
        if func not in cache_dict:
            cache_dict[func] = {}
            
        if args in cache_dict[func]:
            print("Using the cache")
            return cache_dict[func][args]
        else:
            result = func(*args)
            cache_dict[func][args] = result
            print("Calculating")
            return result
        
    
    return wrapped



@cache
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

print(sum(1, 2))
print(sum(1, 2))
print(sum(3, 2))
print(sum(3, 2))
print(sum(2, 1))