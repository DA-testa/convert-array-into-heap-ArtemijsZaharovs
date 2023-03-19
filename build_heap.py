//221RDC035, Artemijs Zaharovs
def sif (data, i, swaps):
    n = len(data)
    index = i
    l = 2*i + 1
    if l < n and data[l] < data[index]:
        index = l
    r = 2*i + 2
    if r < n and data[r] < data[index]:
        index = r
    if i != index:
        data[i], data[index] = data[index], data[i]
        swaps.append((i, index))
        sif(data, index, swaps)


def build_heap(data):
    
    n = len(data)
    swaps = []
    for i in range(n//2, -1, -1):
        sif(data, i, swaps)
    return swaps


def main():

    n = int(input())
    data = list(map(int, input().split()))
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
