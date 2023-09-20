code = [1,1,0,1,0,0,0,1,1,
     1,1,1,0,0,1,0,1,1,
     1,0,0,1,0,1,1,1,1,
     0,1,1,1,1,1,1,1,0,
     0,0,0,0,1,1,1,0,1,
     1,0,1,1,1,1,0,1,1,
     1,0,1,1,1,0,0,0,1,
     0,0,0,1,0,0,0,0,0,
     1,1,0,0,1,1,0,0,0,
     0,1,0,1,1,1,0,0,0,
     1,0,0,0,0,0,1,1,0,
     0,0,0,0,0,0,0,1,0,
     1,1,1,0]

def calculate(parA, parB):
    result = []
    for bit in range(len(code)):
        result.append(code[bit])
        if (bit >= parA): result[bit] ^= result[bit-parA]
        if (bit >= parB): result[bit] ^= result[bit-parB]
    return (result.count(0), result.count(1), result)

best = (1, 0, 0, 0);
for i in range(112):
    for j in range(112):
        if i != j:
            res = calculate(i, j)
            if res[1] != 0 and best[0] > abs(res[0]/res[1] - 1):
                best = (abs(res[0]/res[1] - 1), i, j, res[0], res[1], res[2])
#print(best)
print("parameter A is %d" % min(best[1], best[2]))
print("parameter B is %d" % max(best[1], best[2]))
print("count of 0: %d" % best[3])
print("count of 1: %d" % best[4])
print(" ".join(["".join(list(map(str, code[x:x+8]))) for x in range(0, len(code), 8)]))

