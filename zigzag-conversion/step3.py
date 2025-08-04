class Solution:
    def convert(self, s: str, numRows: int) -> str:
        direction = 1
        def get_next_row_from(current_row: int | None) -> int:
            if current_row is None:
                return 0

            if numRows == 1:
                return 0

            nonlocal direction
            last_row_idx = numRows - 1
            if current_row == 0:
                direction = 1
            if current_row == last_row_idx:
                direction = -1
            return current_row + direction

        current_row = None
        rows = ["" for _ in range(numRows)]
        for char in s:
            current_row = get_next_row_from(current_row)
            rows[current_row] += char
        return "".join(rows)


if __name__ == "__main__":
    solution = Solution()
    assert "PAHNAPLSIIGYIR" == solution.convert("PAYPALISHIRING", 3)
    assert "PINALSIGYAHRPI" == solution.convert("PAYPALISHIRING", 4)
    assert "A" == solution.convert("A", 1)
