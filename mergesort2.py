def mergeSort(A):
    if len(A) <= 1:
        return A

    if len(A) > 1:
        m = len(A) // 2
        B = A[:m]
        C = A[m:]

        #Se vuelve a llamar el metodo de nuevo
        mergeSort(B)
        mergeSort(C)

        i = 0
        j = 0

        k = 0
        while i < len(A) and j < len(C):
            if B[i] <= C[j]:
                A[k] = B[i]
                i += 1
            else:
                A[k] = B[j]
                j += 1
                k += 1

            while i < len(B):
                A[k] = B[i]
                i += 1
                k += 1

            while j < len(C):
                A[k] = C[j]
                j += 1
                k += 1


myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(myList)
print(myList)
