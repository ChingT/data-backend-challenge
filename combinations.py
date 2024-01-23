from typing import Sequence


class Combinations:
    def __init__(self, array: Sequence, constraints: list[set]) -> None:
        self.array = list(array)
        self.constraints = constraints
        self.num_combinations = 0

    def calculate(self) -> int:
        """Calculate the number of all valid combinations."""
        self.num_combinations = 0
        self.find_subset(set(), 0)
        return self.num_combinations

    def find_subset(self, subset: set, index: int) -> None:
        """Generate subsets by recursively including and excluding elements."""
        if not self.is_valid(subset):
            return

        self.num_combinations += 1

        for i in range(index, len(self.array)):
            # Include the current element in the subset
            subset.add(self.array[i])

            # Recursively generate subsets with the current element included
            self.find_subset(subset, i + 1)

            # Exclude the current element from the subset (backtracking)
            subset.remove(self.array[i])

    def is_valid(self, subset: set) -> bool:
        """Check if a subset contains any invalid combination (constraint)."""

        for constraint in self.constraints:
            if constraint.issubset(subset):
                return False
        return True


def run_example():
    n = 4
    # Items 1 and 2 cannot be together; items 2 and 3 cannot be together.
    constraints = [{1, 2}, {2, 3}]
    num_combinations = Combinations(range(n), constraints).calculate()
    print(f"constraints: {constraints}")
    print(f"number of combinations for {n} itmes: {num_combinations}")


if __name__ == "__main__":
    run_example()
