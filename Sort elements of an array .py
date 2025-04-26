# Q33. Program to sort the elements of an array

def arr_ascending(array):
    array.sort()
    return array
    
def arr_descending(array):
    array.sort(reverse = True)
    return array    
    
    
    
    
input_arr = list(map(int,input().split()))
print(f"In ascending order : {arr_ascending(input_arr)}")
print(f"In descending order : {arr_descending(input_arr)}")