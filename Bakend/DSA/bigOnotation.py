def binary_search(arr, target):
    l,h = 0, len(arr)-1

    while l<=h:
        mid = (l+h)//2
        print(mid)
        if arr[mid]== target:
            return mid
        elif arr[mid]<target:
            l=mid+1
        elif arr[mid]>target:
            h = arr[mid]+1

# Example usage
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 9

result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found in the array")
