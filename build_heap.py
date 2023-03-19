
def sif(data, swap, i):
    k = len(data)
    index = i

    l = 2 * i + 1
    if l < k and data[l] < data[index]:
        index = l

    r = 2 * i + 2
    if r < k and data[r] < data[index]:
        index = r

    if i != index:
        swap.append((i, index))
        data[i], data[index] = data[index], data[i]
        sif(data, swap, index)

def build_heap(data):
    swap = []
    k = len(data)

    for i in range(n // 2, -1, -1):
        sif(data, swap, i)

    return swap

def main():
    k = int(input())
    data = list(map(int, input().split()))

    swap = build_heap(data)

    print(len(swap))
    for i, j in swap:
        print(i, j)

if __name__ == '__main__':
    main()
