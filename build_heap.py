# python3
def build_heap(data):
    swaps = []
    n = len(data)
    for i in range (n// 2 -1 -1 -1):
      while True:
         bebr = i
         left = 2 * i + 1
         right = 2 * i + 2
         if left < n and data[left] < data[bebr]:
            bebr = left
         if right < n and data[right] < data[bebr]:
            bebr = right
         if i!=bebr:
            swaps.append((i, bebr))
            data[i], data[bebr] = data[bebr], data[i]
            i = bebr       
         else:
            break
    return swaps        
            
            
            
            
            



    


def main():
    bebroni = input()
    if "I" in bebroni:
        n = int(input())
        data = list(map(int, input().split()))
        
    elif "F" in bebroni:
        files = input()
        
        with open(f"tests/{files}") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
       return

    
    assert len(data) == n
    swaps = build_heap(data)
   
    

   


    
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
   main()
