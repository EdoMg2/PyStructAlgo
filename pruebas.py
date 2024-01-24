"""def merge_Sort(A):

    if len(A) > 1:
        m = len(A) // 2
        B = A[:m]
        C = A[m:]

        merge_Sort(B)
        merge_Sort(C)
        i = 0
        j = 0
        k = 0

        while i< len(B) and j < len(C):
            if B[i] < C[i]:
                A[k] = B

A = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(A)
m = len(A) // 2
B = A[:m]
C = A[m:]
print(B, '+', C)"""


def Merge(B,C):
    D = []
    j = len(D)
    print('B', B,'C', C)
    while len(B) != 0 and len(C) != 0:
        b = B[0]
        c = C[0]
        if b <= c:
            if len(D) == 0:
                D.insert(j, b)
                B.pop(0)
            else:
                D.insert(j+1, b)
                B.pop(0)
                print('B despues de pop:', B)
        else:
            if len(D) == 0:
                D.insert(j, c)
                C.pop(0)

            else:
                D.insert(j + 1, C)
                C.pop(0)
                print('C despues de pop:', C)

    D = D + B + C
    print('D',D)
    return D

def test(text):
    #print(text)
    lol= text + ' lol'
    return text, lol
print(test('hola')[1])

a= [5, 6, 4, 4]
b= [3, 8, 6, 2]
print(a)
a.pop(1)
print(a)
Merge(a,b)


