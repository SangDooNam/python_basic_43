

def wrapped(*args, **kwargs):
    
    print('**********')


    if args:
        
        reform = ', '.join(str(i) for i in args)
        
        print(f'Positional arguments: {reform}')
    

    if kwargs:
        
        print(True)
        


wrapped(1, 2, 3)


# a = (1, 3, 5)

# print(list(a))