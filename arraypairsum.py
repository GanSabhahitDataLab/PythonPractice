# Find out number of pairs in the array which sums upto amount K

def arraypair_sum(ar, K):
    min = 0
    max = len(ar) - 1
    pair = set()
    while min < max:
        print("Iteration ", min, max)
    if ar[min] + ar[max] == K:
        pair.add((ar[min], ar[max]))
    print(pair)
    if ar[min] + ar[max] > K:
        max = max - 1
    else:
        min = min + 1

    return len(pair)
