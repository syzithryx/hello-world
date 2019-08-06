class tree:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

    def path(self,pathList):
        if len(pathList) >= 1:
            if pathList[0] == 0:
                if self.left == None:
                    self.left = tree(0)
                return self.left.path(pathList[1:])
            else:
                if self.right == None:
                    self.right = tree(0)
                return self.right.path(pathList[1:])
        else:
            return self

    def printOut(self,layers=10,tabs=0):
        if layers > 0:
            if self.left != None:
                self.left.printOut(layers-1,tabs+1)
            print('\t'*tabs+str(self.value))
            if self.right != None:
                self.right.printOut(layers-1,tabs+1)

    def maxDepth(self,layers=10):
        if layers > 0:
            if self.left == None or self.left.value == 0:
                L = 1
            else:
                L = self.left.maxDepth(layers-1)
            if self.right == None or self.right.value == 0:
                R = 1
            else:
                R = self.right.maxDepth(layers-1)
            return max(L,R)+1
        else:
            return 1

    def minDepth(self,layers=10):
        if layers > 0:
            if self.left == None or self.left.value == 0:
                L = 1
            else:
                L = self.left.minDepth(layers-1)+1
            if self.right == None or self.right.value == 0:
                R = 1
            else:
                R = self.right.minDepth(layers-1)+1
            return min(L, R)
        else:
            return 1

t = tree(1,tree(3),tree(2))
primes = [2,3]
for i in range(4,211):
    path = []
    branch = t
    for p in primes:
        if i % p == 0:
            path += [1]
        else:
            path += [0]
        branch = t.path(path)
        if branch.value == 0:
            break
    if 1 not in path:
        primes += [i]
    branch.value = i
t.printOut(t.minDepth())
