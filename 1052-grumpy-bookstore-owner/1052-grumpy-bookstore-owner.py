class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        already_satisfied = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                already_satisfied += customers[i]
                customers[i] = 0
        best_we_can_make_satisfied = 0
        current_satisfied = 0
        for i, customers_at_time in enumerate(customers):
            current_satisfied += customers_at_time  # Add current to rolling total
            if i >= minutes:  # We need to remove some from the rolling total
                current_satisfied -= customers[i - minutes]
            best_we_can_make_satisfied = max(best_we_can_make_satisfied, current_satisfied)

        # The answer is the sum of the solutions for the 2 parts.
        return already_satisfied + best_we_can_make_satisfied