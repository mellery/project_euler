"""Project Euler 96: Su Doku

Solve fifty Sudoku puzzles from input/0096_sudoku.txt and sum the 3-digit
numbers found in the top-left corner of each solution.
"""

from pathlib import Path


def parse_puzzles(path):
    text = Path(path).read_text().strip().splitlines()
    puzzles = []
    grid = []
    for line in text:
        if line.startswith('Grid'):
            if grid:
                puzzles.append(grid)
                grid = []
        else:
            grid.append([int(c) for c in line.strip()])
    if grid:
        puzzles.append(grid)
    return puzzles


class DancingLinksSolver:
    # DLX exact cover for Sudoku. Build constraint matrix of size 9x9x9 rows
    # and 4*9*9 columns (cell, row, column, box constraints).
    def __init__(self, grid):
        self.grid = [row[:] for row in grid]
        # Build exact cover matrix rows as tuple (r,c,d) for possible placements
        self.rows = []
        self.row_index = {}
        for r in range(9):
            for c in range(9):
                for d in range(1, 10):
                    if grid[r][c] == 0 or grid[r][c] == d:
                        idx = len(self.rows)
                        self.rows.append((r, c, d))
                        self.row_index[(r, c, d)] = idx

        # column indices mapping
        # cell constraint: r*9 + c (0..80)
        # row constraint: 81 + r*9 + (d-1)
        # col constraint: 162 + c*9 + (d-1)
        # box constraint: 243 + b*9 + (d-1)
        self.cols = [[] for _ in range(324)]
        self.row_to_cols = [None] * len(self.rows)
        for idx, (r, c, d) in enumerate(self.rows):
            b = (r // 3) * 3 + (c // 3)
            col_idxs = [r * 9 + c,
                        81 + r * 9 + (d - 1),
                        162 + c * 9 + (d - 1),
                        243 + b * 9 + (d - 1)]
            self.row_to_cols[idx] = col_idxs
            for col in col_idxs:
                self.cols[col].append(idx)

        # initial cover: select rows from given clues
        self.active_rows = set()
        self.active_cols = set(range(324))
        for r in range(9):
            for c in range(9):
                d = grid[r][c]
                if d:
                    self.select_row(self.row_index[(r, c, d)])

    def select_row(self, ridx):
        if ridx in self.active_rows:
            return
        self.active_rows.add(ridx)
        # remove columns covered by this row
        # find the columns for this row
        r, c, d = self.rows[ridx]
        b = (r // 3) * 3 + (c // 3)
        col_idxs = [r * 9 + c,
                    81 + r * 9 + (d - 1),
                    162 + c * 9 + (d - 1),
                    243 + b * 9 + (d - 1)]
        for col in col_idxs:
            if col in self.active_cols:
                self.active_cols.remove(col)

    def deselect_row(self, ridx):
        if ridx not in self.active_rows:
            return
        self.active_rows.remove(ridx)
        r, c, d = self.rows[ridx]
        b = (r // 3) * 3 + (c // 3)
        col_idxs = [r * 9 + c,
                    81 + r * 9 + (d - 1),
                    162 + c * 9 + (d - 1),
                    243 + b * 9 + (d - 1)]
        for col in col_idxs:
            self.active_cols.add(col)

    def solve(self):
        solution = {}

        def search():
            if not self.active_cols:
                return True
            # choose smallest column
            # choose a column with minimal remaining rows
            best_col = None
            best_count = 10**9
            for c in self.active_cols:
                cnt = 0
                for r in self.cols[c]:
                    # count row only if all its columns are still active
                    ok_row = True
                    for col2 in self.row_to_cols[r]:
                        if col2 not in self.active_cols:
                            ok_row = False
                            break
                    if ok_row and r not in self.active_rows:
                        cnt += 1
                if best_col is None or cnt < best_count:
                    best_col = c
                    best_count = cnt
            col = best_col
            rows = [r for r in self.cols[col]
                    if all(col2 in self.active_cols for col2 in self.row_to_cols[r]) and r not in self.active_rows]
            if not rows:
                return False
            for r in rows:
                # cover row
                self.select_row(r)
                if search():
                    solution[len(solution)] = r
                    return True
                self.deselect_row(r)
            return False

        ok = search()
        if not ok:
            return False
        # build grid from selected rows
        for ridx in self.active_rows:
            r, c, d = self.rows[ridx]
            self.grid[r][c] = d
        return True


def top_left_number(grid):
    return 100 * grid[0][0] + 10 * grid[0][1] + grid[0][2]


def main():
    puzzles = parse_puzzles('input/0096_sudoku.txt')
    total = 0
    for p in puzzles:
        solver = DancingLinksSolver(p)
        ok = solver.solve()
        if not ok:
            raise RuntimeError('Failed to solve puzzle')
        total += top_left_number(solver.grid)
    print(total)


if __name__ == '__main__':
    main()
