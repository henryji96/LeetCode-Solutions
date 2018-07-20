#BFS [1, [2,3], [4, [5,6]]]

def flatten(l):
    ans = []
    queue = []

    for i in l:
        queue.append(i)
        while queue:
            t = queue.pop(0)
            if type(t) == list:
                queue += t
            else:
                ans.append(t)
    return ans


print(flatten([1, [2,3], [4, [5,6,[3]]]]))
