

# def wrapped(*args, **kwargs):
    
#     print('**********')


#     if args:
        
#         reform = ', '.join(str(i) for i in args)
        
#         print(f'Positional arguments: {reform}')
    

#     if kwargs:
        
#         print(True)
        


# def wrapped():
    
#     return '**********'



# print(wrapped)


# a = (1, 3, 5)

# print(list(a))

# def cache(func):
    
#     def wrapped(*args):
        
#         cache_dict = {func : {}}
        
#         cache_dict[func].update({args: func(*args)})
        
#         print(cache_dict)
        
#         # print(cache_dict)
#         return func(*args)
    
#     return wrapped




# @cache
# def sum(a, b):
#     """Return the sum of two numbers."""
#     return a + b

# print(sum(1, 2))
# print(sum(1, 2))
# print(sum(3, 2))
# print(sum(3, 2))
# print(sum(2, 1))


# def sum(a, b):
#     """Return the sum of two numbers."""
#     return a + b


# a = [1 , 4]

# print(sum)

# dict_ex = {'apple' : {'red': 5}}


# print(dict_ex['apple'])


def cache(func):
    cache_dict = {}
    
    def wrapped(*args):
        # if args in cache_dict:
        #     print("Using cached value")
        #     return cache_dict[args]
        
        result = func(*args)
        cache_dict[args] = result
        
        print(cache_dict)
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