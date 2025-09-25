# Linear Search Algorithm Using Python
# Time complexity: O(n)
def linear_search(nums, target):
    for num in nums:
        if num == target:
            return True
    return False


def main():
    nums = [14, 21, 27, 30, 36, 2, 5, 7, 11]

    target = 27
    print(linear_search(nums, target))

    target = 100
    print(linear_search(nums, target))


if __name__ == "__main__":
    main()
"""
Linear or sequential search is the best one can do when searching through unsorted sequences
"""