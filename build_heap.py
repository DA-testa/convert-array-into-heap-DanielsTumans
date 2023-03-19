# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range (n// 2 -1 -1 -1):
        while True: 
            bebr = i
            left = 2 * n + 1
            right = 2 * n + 2
            
            
            
            if left < n and data[bebr] > data[left]:
                bebr = left
            if right < n and data[bebr] < data[right]:
                bebr = right
            if i!=bebr:
                swaps.append((i, bebr))
                data[i], data[bebr] = data[bebr], data[i]
                i = bebr
            
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():
    bebroni = input()
    if "I" in bebroni:
        n = int(input())
        data = list(map(int, input().split()))
        
    elif "F" in bebroni:
        files = input()
        
         with open(f"tests/{fn}") as filek:
            n = int(filek.readline())
            data = list(map(int, filek.readline().split()))

    
    assert len(data) == n
    swaps = build_heap(data)
   
    

   


    
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
   main()
