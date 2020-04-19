class Solution:
    def search(self, nums, target):
        def binarySearch(arr, n):
            piv = len(arr) // 2
            if n == arr[piv]:
                return piv
            elif len(arr) == 1:
                return -1
            elif n < arr[piv]:
                return binarySearch(arr[:piv], n)
            else:
                res = binarySearch(arr[piv:], n)
                return (piv + res) if res >= 0 else -1

        def rotatedSearch(arr, n):
            if len(arr) == 0 or (len(arr) == 1 and n != arr[0]):
                return -1
            else:
                piv = len(arr) // 2
                if n == arr[piv]:
                    return piv
                elif piv-1 == 0:
                    if n == arr[0]:
                        return 0
                    else:
                        res = rotatedSearch(arr[1:], n)
                        return res+1 if res >= 0 else -1
                elif arr[0] < arr[piv-1]:  # left sorted, rigth rotated
                    if arr[0] <= n <= arr[piv-1]:
                        return binarySearch(arr[:piv], n)
                    else:
                        res = rotatedSearch(arr[piv:], n)
                        return piv + res if res >= 0 else -1
                else:  # left rotated, right sorted
                    if arr[piv] <= n <= arr[-1]:
                        res = binarySearch(arr[piv:], n)
                        return piv + res if res >= 0 else -1
                    else:
                        return rotatedSearch(arr[:piv], n)

        return rotatedSearch(nums, target)
