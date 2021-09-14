# Tower of Hanoi (Recursion)



def move(start, end):
    global L, M, R

    # start에서 뺀 원형 판을 end에 옮겨준다.

    if start == 'L':
        L -= 1
    elif start == 'M':
        M -= 1
    elif start == 'R':
        R -= 1

    if end == 'L':
        L += 1
    elif end == 'M':
        M += 1
    elif end == 'R':
        R += 1

# start : 시작점
# tmp : 경유지
# end : 목적지

def hanoi(n, start, tmp, end):
    if n==1:
        move(start, end)
        print('{}--->{}\tL: {}\tM: {}\tR: {}\n'.format(start, end, L, M, R))
        return
    hanoi(n-1, start, end, tmp)
    hanoi(1, start, tmp, end)
    hanoi(n-1, tmp, start, end)

    '''
    만약 n = 3 이라면
    3, 'L', 'M', 'R'    ---> 출력3
    2, 'L', 'R', 'M'    ---> 출력2
    1, 'L', 'M', 'R'    ---> 출력1  
    
    1, 'L', 'M', 'R'    ---> 출력4
    3, 'M', 'L', 'R'    ---> 출력7
    2, 'L', 'M', 'R'    ---> 출력6
    1, 'M', 'L', 'R'    ---> 출력5
    
    '''


n = int(input('n : '))
L, M, R = n, 0, 0
hanoi(n,'L','M','R')
