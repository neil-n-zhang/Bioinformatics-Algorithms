# Compare each two numbers, get the bigger and smaller ones O(n/2), then compare among bigger and smaller numbers O(n/2*2)

import numpy as np
numbers=[10,2,7,4,5]
if len(numbers)%2==0:
    big = np.zeros(len(numbers) // 2)
    small = np.zeros(len(numbers) // 2)
    for i in list(range(0,len(numbers),2)):
        if numbers[i]<numbers[i+1]:
            big[i//2]=numbers[i+1]
            small[i//2]=numbers[i]
        else:
            big[i//2] = numbers[i]
            small[i//2] = numbers[i+1]
else:
    big = np.zeros(int(len(numbers) / 2)+1)
    small = np.zeros(int(len(numbers) / 2)+1)
    for i in list(range(0, len(numbers)-1, 2)):
        if numbers[i] < numbers[i + 1]:
            big[i // 2] = numbers[i + 1]
            small[i // 2] = numbers[i]
        else:
            big[i // 2] = numbers[i]
            small[i // 2] = numbers[i + 1]
    big[-1]=numbers[-1]
    small[-1] = numbers[-1]

biggest=big[0]
smallest=small[0]
for i in list(range(len(big))):
    if biggest<big[i]:
        biggest=big[i]
    if smallest>small[i]:
        smallest = small[i]

print(smallest,biggest)