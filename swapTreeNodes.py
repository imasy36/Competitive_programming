def inorder(ind:list, n):
    if n==-1:
        return []
    return inorder(ind,ind[n-1][0]) + [n] + inorder(ind,ind[n-1][1])

def getDepth(indexes, n):
    if n==-1:
        return 0
    return max(getDepth(indexes, indexes[n-1][0]), getDepth(indexes, indexes[n-1][1]))+1

def getDepthIndexes(indexes, n, i):
    if i==-1:
        return []
    if n==0:
        return [i-1]
    return getDepthIndexes(indexes, n-1, indexes[i-1][0]) + getDepthIndexes(indexes, n-1, indexes[i-1][1])
    
def swapNodes(indexes, queries):
    res = []
    for x in range(len(queries)):
        q = queries[x]
        for i in range(q-1, getDepth(indexes,1), q):
            temp = getDepthIndexes(indexes, i, 1)
            #print(i, " ", temp)
            for j in temp:
                indexes[j][0], indexes[j][1] = indexes[j][1], indexes[j][0]
        res.append(inorder(indexes,1))
    return res

if __name__=='__main__':
    n = int(input())
    indexes = []
    for i in range(n):
        indexes.append([int(x) for x in input().split()])
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(int(input()))
    for x in swapNodes(indexes, queries):
        print(x)
    