def isPalinArray(arr):
    for i in arr:
        if str(i) != str(i)[::-1]:
            return False   # Return Python boolean False
    return True            # If all are palindromes
