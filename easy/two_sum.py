# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    return [i,j]

def main():
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    target = 9
    ret = sol.twoSum(nums, target)
    print(nums)
    print(target)
    print(ret)

if __name__ == '__main__':
    main()
