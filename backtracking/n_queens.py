"""
The n-queens puzzle is the problem of placing n queens on an n x n 
chessboard such that no two queens attacj each other.

Given an integer n, return all distinct soluctions to the n-queen puzzle.
You may return the answer in any order

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectibely.

https://leetcode.com/problems/n-queens/
"""
class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        # Video to understand function annotation: https://youtu.be/6eyOQyG6FpE
        solutions = []
        state = []
        self.search(state, solutions, n) 
        return solutions  

    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return range(n)

        # find the next position in the state to populate
        position = len(state)
        candidates = set(range(n))
        # pure down candidates that palce the queen into attacks
        for row, col in enumerate(state):
            # discard the column index if it's occupied by a queen
            candidates.discard(col)
            dist = position - row
            # discard diagonals
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state)
            solutions.append(state_string)
            return

        for candidate in self.get_candidates(state, n):
            # recurse
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()

    def state_to_string(self, state, n):
        # ex [1, 3, 0, 2]
        # output: [".Q..", "...Q", "Q...", "..Q."] 
        ret = []
        for i in state:
            string = '.' * i + 'Q' + '.' * (n-i-1)
            ret.append(string)

