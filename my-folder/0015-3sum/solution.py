class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array
        result = set()  # Use a set to store unique triplets

        for leftmost in range(len(nums) - 2):  # Fix the first number
            # Skip duplicates for the `leftmost` pointer
            if leftmost > 0 and nums[leftmost] == nums[leftmost - 1]:
                continue

            left, right = leftmost + 1, len(nums) - 1  # Initialize pointers

            while left < right:
                current_sum = nums[leftmost] + nums[left] + nums[right]

                if current_sum == 0:
                    result.add((nums[leftmost], nums[left], nums[right]))  # Add triplet as a tuple

                    # Move pointers and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # Increase the sum by moving `left` rightward
                else:
                    right -= 1  # Decrease the sum by moving `right` leftward

        return [list(triplet) for triplet in result]  # Convert set of tuples back to a list of lists

