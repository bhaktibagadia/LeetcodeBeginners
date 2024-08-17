class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # hare and tortoise method
        # slow and fast pointer approach
        # linked list cycle detection method
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast        