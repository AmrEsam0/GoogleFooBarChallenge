def solution(x, y):
    z = ((x+y-1)*(x+y-2))/2 + x
    return str(z)

if __name__ == '__main__':
    print(solution(5, 10))