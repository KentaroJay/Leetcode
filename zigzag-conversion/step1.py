class Solution:
    def convert(self, s: str, numRows: int) -> str:
        last_row_idx = numRows - 1
        current_row = None
        direction = 1
        rows = ["" for _ in range(numRows)]

        def get_next_row(current_row: int | None) -> int:
            if current_row is None:
                return 0

            nonlocal direction
            current_row += direction
            if last_row_idx < current_row:
                direction = -1
                current_row -= 2
                return current_row
            if current_row < 0:
                direction = 1
                current_row += 2
                return current_row
            return current_row

        for char in s:
            current_row = get_next_row(current_row=current_row)
            rows[current_row] += char

        return "".join(rows)


if __name__ == "__main__":
    solution = Solution()
    output = solution.convert("skibiditoilet", 3)
    print(output)
