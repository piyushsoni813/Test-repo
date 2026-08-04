# Test-repo

This repository is a personal collection of LeetCode solutions written in Python and C++. It is directly linked to my LeetCode practice and intended to showcase problem-solving progress while naturally increasing my GitHub contribution graph through regular commits.

> NOTE: Replace <LEETCODE_USERNAME> with your actual LeetCode username where indicated below.

---

## Table of Contents

- [About](#about)
- [Repository Structure](#repository-structure)
- [How I organize solutions](#how-i-organize-solutions)
- [How to run / test solutions](#how-to-run--test-solutions)
- [Contributing (for me and others)](#contributing-for-me-and-others)
- [Tips to grow your contribution graph (honest, sustainable ways)](#tips-to-grow-your-contribution-graph-honest-sustainable-ways)
- [License](#license)
- [Contact](#contact)

---

## About

This repo stores LeetCode problem solutions I solve as part of regular practice. Solutions are written primarily in Python and C++ (see language breakdown in the repo).

The main goals are:

- Keep a well-organized archive of solutions for review and learning.
- Track progress over time and provide a public record of practice.
- Improve GitHub contributions by committing solutions regularly.

If you want to link this repository to your LeetCode profile (for anyone viewing), you can add your LeetCode URL to your GitHub profile or the README below. Example: https://leetcode.com/<LEETCODE_USERNAME>/

---

## Repository Structure

- python/        - Python solutions (recommended: one file per problem, named `p{problem-number}_{slug}.py`)
- cpp/           - C++ solutions (recommended: one file per problem, named `p{problem-number}_{slug}.cpp`)
- scripts/       - Optional utilities (e.g., template generators, test harnesses)
- README.md      - This file

Example file naming: `p1_two-sum.py`, `p2_add-two-numbers.cpp`

---

## How I organize solutions

- Each solution file contains the problem number and a short slug of the problem title in the filename.
- Add a short comment at the top with:
  - Problem title
  - Link to the LeetCode problem
  - Difficulty (Easy / Medium / Hard)
  - Date solved (YYYY-MM-DD)

Example header for a Python solution:

```python
# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Solved: 2026-08-04

class Solution:
    def twoSum(self, nums, target):
        ...
```

---

## How to run / test solutions

- For Python files, run with your chosen input harness or use LeetCode's online judge. Example:

  python python/p1_two-sum.py

- For C++ files, compile and run locally with your preferred flags:

  g++ -std=c++17 cpp/p1_two-sum.cpp -O2 -o p1 && ./p1

(You can add small test wrappers in `scripts/` to run examples for many problems.)

---

## Contributing (for me and others)

If you want to use this repo as your personal LeetCode archive and increase your contribution graph, follow these recommended steps:

1. Fork the repository (if you're not the repo owner).
2. Create a branch for your session or problem set (e.g., `feat/leetcode-2026-08-04`).
3. Add solution files under the appropriate language folder. Keep changes small and focused (one or a few problems per commit) — frequent small commits reflect steady progress.
4. Commit with clear messages like `Add p15 3sum (Python) — solved 2026-08-04`.
5. Open a pull request and merge into the main branch (or push directly if this is your personal repo).

Maintainers: if this is your personal repo, simply push commits directly to keep the contribution graph active. If collaborating, use PRs and review as usual.

---

## Tips to grow your contribution graph (honest, sustainable ways)

- Practice consistently: commit daily or several times a week with real work (solutions, refactors, tests, docs).
- Make meaningful commits: include tests, explanations, or small refactors rather than empty commits.
- Add README updates or notes about problem strategies — non-code contributions count too.
- Use branches for focused work and merge frequently.

Avoid gaming the graph with meaningless commits — the long-term value is in steady learning and documented progress.

---

## License

This repository is provided under the MIT License. See LICENSE file for details.

---

## Contact

GitHub: https://github.com/piyushsoni813
LeetCode: https://leetcode.com/<LEETCODE_USERNAME>/ (replace with your username)

Happy coding! Keep practicing and commit often to track your improvement.
