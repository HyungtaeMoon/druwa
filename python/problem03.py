"""
한 개 또는 두 개의 숫자 인자를 전달받아, 하나가 오면 제곱, 두개를 받으면 두 수의 곱을 반환해주는 함수를 정의하고 사용해본다.
"""
def square(*args):

    squares = []

    for i in args:
        squares.append(i**2)

    return squares
