"""
problem01에서 작성한 함수에 docstring을 작성하여 함수에 대한 설명을 달아보고, help(함수명)으로 해당 설명을 출력해본다.
"""
def result(*args):

    args = input("input your favorite color: ")
    
    if args == 'red':
        print('apple')
    
    elif args == 'yellow':
        print('banana')
    
    elif args == 'green':
        print('melon')
    
    else:
        print('I don\'t know')


