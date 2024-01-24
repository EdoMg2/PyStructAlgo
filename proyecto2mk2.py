import sys, threading
sys.setrecursionlimit(10**8) # max depth of recursion
#threading.stack_size(2**27)  # new thread will get stack of such size

class Tree:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]

        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().rstrip().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def IsBinarySearchTree(self):
        if self.n == 0: return True
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        x = 0
        def inorder(x):
            if x != -1:
                inorder(self.left[x])
                self.result.append(self.key[x])
                inorder(self.right[x])

        inorder(x)

        for x in range(1, len(self.result)):
            if self.result[x] < self.result[x-1]:
                return False

        return True


if __name__ == '__main__':

    Tree = Tree()
    #print(Tree)
    Tree.read()
    if Tree.IsBinarySearchTree() == True:
        print("CORRECT")
    else:
        print("INCORRECT")




