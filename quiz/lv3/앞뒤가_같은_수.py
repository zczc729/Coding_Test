"""
앞뒤가 같은 수는 바로 쓴 값과 거꾸로 쓴 값이 같은 수이다. 다음과 같은 예를 들 수 있다.

1
44
101
2002
8972798
1111111111111
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 
... 과 같이, 0 이상의 앞뒤가 같은 수를 크기 순으로 나열할 때, n 번째 수를 계산하는 프로그램을 작성하라.

n은 1부터 시작하며 크기에는 제한이 없다.

입출력예

예 1) 1 => 0
예 2) 4 => 3
예 3) 30 => 202
예 4) 100 => 909
예 5) 30000 => 200000002
예 6) 1000000 => 90000000009
"""
n = 900
num = 0
inc_num = 0
is_break = False

for i in range(n-1):
    is_num = False
    while True:
        inc_num += 1
        print("i : ", i)
        print("inc_num : ", inc_num)
        ls = list(str(inc_num))

        if len(ls) < 2:
            num = inc_num
            print("1. num : ", num)
            break
        else:
            for j in range(int(len(ls) / 2)):
                if ls[j] == ls[(j + 1) * -1]:
                    print("2. num : ", num)
                    num = inc_num
                    is_break = True
                    print("2. T/F : ", is_break)
                else:
                    is_break = False
            if is_break:
                break
    print("3. num : ", num)


print(num)

        



                

















