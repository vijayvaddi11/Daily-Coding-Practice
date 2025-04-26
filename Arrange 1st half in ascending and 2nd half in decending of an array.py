# Q32. Sort first half in ascending order and second half in descending order in an array

def dividing_arr(array):
    
    first_half_arr=[]
    second_half_arr=[]
    
    if(len(input_arr)%2==0):
        first_half = len(input_arr)//2
        for num in range(0,first_half):
            first_half_arr.append(input_arr[num])
        print("First Half:",first_half_arr)
        for num2 in range(first_half,len(input_arr)):
            second_half_arr.append(input_arr[num2])
        print("Second Half:",second_half_arr)
        
    else:
        first_half = len(input_arr)//2
        for num in range(0,first_half+1):
            first_half_arr.append(input_arr[num])
        print("First Half:",first_half_arr)
        for num2 in range(first_half+1,len(input_arr)):
            second_half_arr.append(input_arr[num2])
        print("Second Half:",second_half_arr)
        
    return first_half_arr,second_half_arr    
    
    
   
input_arr = list(map(int,input().split()))   
first, second = dividing_arr(input_arr)
first.sort()
second.sort(reverse=True)
print(first+second)