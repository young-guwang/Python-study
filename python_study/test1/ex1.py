# a = 9
# b = 9
# c = 81

# c = a * b
# print(str(a) + " * " + str(b) + " = " +  str(c))



# 구구단~!

# from 1 to 9

# list : 배열 + 순서, tuple 
#FD

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 0

# for i in a:
#     print (str(i),"단 시작합니다.")
#     for j in b:
#         c = i * j
#         print(str(i) + " * " + str(j) + " = " + str(c))
#     print (str(i),"단 끝났습니다.")

# if a > b:
#     # how can
# else:
    # when
    
def sub(a,b):
    if a > b:
        c = a - b
        print(c)
    
    else:
        c = b - a
        print(c)

sub(3, 6)