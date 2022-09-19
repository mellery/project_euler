import itertools

vals = [1,2,3,4,5,6,7,8,9,10]

combs = list(itertools.permutations(vals))
print(len(combs))
max_ans = 0
for i in combs:
    if (i[0] < min([i[1],i[2],i[3],i[4]])):
        if i[0]+i[6]+i[7] == i[1]+i[7]+i[8] == i[2]+i[8]+i[9] == i[3]+i[9]+i[5] == i[4]+i[5]+i[6]:
            val = [i[0],i[6],i[7],i[1],i[7],i[8],i[2],i[8],i[9],i[3],i[9],i[5],i[4],i[5],i[6]]
            string = [str(x) for x in val]
            temp = "".join(string)
            ans = int(temp)
            if len(temp) == 16 and ans > max_ans:
                max_ans = ans
                print(ans)
