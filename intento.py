class Lista:
    def __init__(self):
        self.r = 0
        self.l = len(self)

    def mergeSort(self, l, r):
        if self.l < self.r:
            m = self.l + (self.r - self.l) // 2

            mergeSort(self, self.l, m)
            mergeSort(arr, m + 1, r)
            merge(self, self.l, m, self.l)
            contador= contador + merge(arr, l, m, r)
            return contador
    def merge(self,l,m,r):
        n1 = m - l + 1
        n2 = r - m

        B = [0] * (n1)
        C = [0] * (n2)

        for i in range(0, n1):
            B[i] = A[l + i]

        for j in range(0, n2):
            C[j] = A[m + 1 + j]

        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            if B[i] <= C[j]:
                A[k] = B[i]
                i += 1
            else:
                A[k] = C[j]
                j += 1
            k += 1


        while i < n1:
            A[k] = B[i]
            i += 1
            k += 1


        while j < n2:
            A[k] = C[j]
            j += 1
            k += 1
        return k