"""Task 1"""


def validate_numeric(func):
    
    def inner(*args, **kwargs):
        
        for i in args:
            
            if not isinstance(i, (int, float)):
                
                return 'The input arguments must be numeric'
                
        for e , i in kwargs.items():
            
            if not isinstance(i, (int, float)):
                return 'The input arguments must be numeric'
        
        
        return func(*args, **kwargs)
    
    return inner



@validate_numeric
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

print(sum(1, 2))
print(sum(1, "2"))
print(sum(a=1, b="a"))
print(sum(a=1, b=3.4))



