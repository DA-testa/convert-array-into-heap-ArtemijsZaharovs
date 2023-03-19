#221RDC035, Artemijs Zaharovs, 18.gr.
import os
def sif(data, i, swaps):
    n = len(data)
    x = i
    l = 2*i + 1
    if l < n and data[l] < data[x]:
        x = l
    r = 2*i + 2
    if r < n and data[r] < data[x]:
        x = r
    if i != x:
        data[i], data[x] = data[x], data[i]
        swaps.append((i, x))
        sif(data, x, swaps)


def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n//2, -1, -1):
        sif(data, i, swaps)
    return swaps



def main():
    input_method = input().strip()
    if input_method == 'I':
        n = int(input())
        data = list(map(int, input().split()))
    elif input_method == 'F':
        file_name = input().strip()
        file_path = os.path.join("tests", file_name)
        with open(file_path) as file:
            n = int(file.readline().strip())
            data = list(map(int, file.readline().strip().split()))
    else:
        print('Invalid input method')
        return
    
    
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
