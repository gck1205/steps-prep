# Recursive Implementation of Binary Search in Python
# Pre-conditions:
# 1. Sorted Array in Ascending Order
# CHECK IF A NUMBER EXISTS IN A SORTED ARRAY
# Time complexity : O(log(n))[Base 2]
def binary_search(nums, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            return binary_search(nums, target, mid + 1, high)
        else:
            return binary_search(nums, target, low, mid - 1)


def main():
    nums = [2, 5, 7, 11, 14, 21, 27, 30, 36]

    target = 27
    print(binary_search(nums, target, 0, len(nums) - 1))

    target = 38
    print(binary_search(nums, target, 0, len(nums) - 1))


if __name__ == "__main__":
    main()