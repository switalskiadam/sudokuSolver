

test_array = [[[[3, 4, 5], [7, 6, 9], [2, 1, 8]],
[[6, 8, 9], [4, 2, 1], [5, 7, 3]], 
[[2, 1, 7], [8, 5, 3], [9, 4, 6]]], 
[[[9, 6, 3], [2, 4, 8], [1, 5, 7]], 
[[4, 7, 2], [3, 1, 5], [8, 6, 9]], 
[[8, 5, 1], [9, 7, 6], [3, 2, 4]]], 
[[[1, 9, 4], [5, 8, 7], [6, 3, 2]], 
[[5, 2, 8], [6, 3, 4], [7, 9, 1]], 
[[7, 3, 6], [1, 9, 2], [4, 8, 5]]]]

print('===========================================')
print('|| ' + t + ' ||')


def printChunk(chunk):
    """Converts list of 3 into a board like print"""
    l = str(chunk).replace(',',' |').replace('[','').replace(']','')
    return str(l)

t = []
for c in test_array[0][0]:
    s = printChunk(c)
    t.append(s)
t = str(t).replace(',',' || ').replace('\'','').replace('[','').replace(']','')
print(t)

for i in test_array:
    for s in i:
        print(s)
