import sys
import random

n = int(input('Enter no. of objects: '))
dataset = list(map(int,input('Enter the objects: ').split()))
k = int(input('Enter no. of clusters: '))

Dict = {}
meansOld = random.sample(dataset, k)
means = meansOld.copy()

for x in range(5):
    for i in range(k):
        Dict[i] = []
    for i in range(len(dataset)):
        minIndex = 0
        minValue = sys.maxsize
        for j in range(len(means)):
            if abs(means[j] - dataset[i]) < minValue:
                minValue = abs(means[j] - dataset[i])
                minIndex = j
        Dict[minIndex].append(dataset[i])
    for key in Dict:
        su = sum(Dict[key])
        num = len(Dict[key])

        means[key] = su/num
    print('Reassigning: ', Dict, 'Mean = ', means)
    if(meansOld == means):
        break
    meansOld = means.copy()
    Dict.clear()
print('Final Answer: ', Dict)


# Enter no. of objects: 5
# Enter the objects: 1 3 9 4 12
# Enter no. of clusters: 2
# Reassigning:  {0: [9, 12], 1: [1, 3, 4]} Mean =  [10.5, 2.6666666666666665]       
# Reassigning:  {0: [9, 12], 1: [1, 3, 4]} Mean =  [10.5, 2.6666666666666665]       
# Final Answer:  {0: [9, 12], 1: [1, 3, 4]}