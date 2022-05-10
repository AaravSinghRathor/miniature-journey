# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
#
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations.
# The list must not contain the same combination twice,
# and the combinations may be returned in any order.
# https://leetcode.com/problems/combination-sum-iii/

import sys
# sys.setrecursionlimit(10)


class Solution:

    def __init__(self):

        self.possible_solutions = []

    def find_combination_sum(self, current_number, total_sum, possible_solution_list, k):

        print('*'*30)
        print(f"Current Number: {current_number}. Total Sum: {total_sum}. Possible list: {possible_solution_list}")

        if total_sum == 0:
            if len(possible_solution_list) == k:
                print("solution found")
                self.possible_solutions.append(possible_solution_list)
                return
            else:
                print("returning as total sum is 0 and size exceeded or lower size")
                return

        if current_number == 0:
            print("returning as current_number is 0")
            return

        if len(possible_solution_list) >= k:
            print("returning as list size exceed")
            return

        if current_number <= total_sum:
            self.find_combination_sum(
                current_number - 1, total_sum-current_number, possible_solution_list + [current_number], k)
        self.find_combination_sum(current_number - 1, total_sum, possible_solution_list, k)

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:

        self.find_combination_sum(9, n, [], k)
        return self.possible_solutions


print(Solution().combinationSum3(3, 9))
