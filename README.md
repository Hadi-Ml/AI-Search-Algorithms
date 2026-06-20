# Artificial Intelligence (AI) State-Space Search Algorithms

This repository provides clean, comprehensive, and benchmarking-ready Python implementations of traditional **State-Space Search Algorithms** in Artificial Intelligence. It covers both **Uninformed (Blind) Search** and **Informed (Heuristic) Search** strategies, mapping directly to the foundational theories found in textbook AI architecture (e.g., Russell & Norvig's *Artificial Intelligence: A Modern Approach*).

---

## 🛠️ Repository Structure

The project consists of the following core implementations:

* **`Breadth First Search.py`**: Explores the state space level by level. Guaranteed to find the shallowest goal.
* **`Depth First Search.py`**: Deeply traverses a single path until a dead-end is reached before backtracking.
* **`Depth Limited Search.py`**: A variant of DFS constrained by a maximum depth limit ($l$) to handle infinite paths.
* **`Iterative Deepening Search.py`**: Iteratively steps up depth limits, combining DFS's space efficiency with BFS's completeness.
* **`Uniform Cost Search.py`**: Evaluates nodes based on optimal step costs, expanding the cheapest paths first.
* **`Harisaneh Serach.py`**: An informed **Greedy Best-First Search** utilizing a heuristic function $h(n)$ to prioritize nodes closest to the goal.
* **`A Star.py`**: A highly efficient, informed algorithm that minimizes total estimated cost: $f(n) = g(n) + h(n)$.
* **`All Search Algorithms.py`**: A combined test script containing a comparative analysis and benchmark suite for the implemented algorithms.

---

## ⚡ Built-in Libraries & Data Structures

To maximize execution efficiency and maintain high performance, this project strictly utilizes Python's robust built-in modules without requiring heavy external dependencies:

* **`collections (deque)`**: Utilized in **BFS** and **UCS** to achieve $O(1)$ time complexity for queue pop operations, significantly outperforming standard Python lists ($O(n)$).
* **`itertools`**: Applied for memory-efficient state generation, combinations, and systematic space transitions.
* **`time`**: Used to benchmark and precisely measure the execution time of each algorithm, enabling practical performance comparisons.

---

## 📊 Comprehensive Algorithm Comparison

The efficiency of these search strategies is evaluated using four standard AI metrics where:
* $b$: Branching factor
* $d$: Depth of the shallowest optimal solution
* $m$: Maximum depth of the state space
* $l$: Predetermined depth limit
* $C^*$: Cost of the optimal solution
* $\epsilon$: Minimum positive cost bound for transitions

| Search Strategy | Algorithm | Completeness | Time Complexity | Space Complexity | Optimality |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Uninformed** | **BFS** | Yes (if $b$ is finite) | $O(b^d)$ | $O(b^d)$ | Yes (if edge costs are equal) |
| **Uninformed** | **DFS** | No (fails in infinite spaces) | $O(b^m)$ | $O(bm)$ | No |
| **Uninformed** | **DLS** | No (if $d > l$) | $O(b^l)$ | $O(bl)$ | No |
| **Uninformed** | **IDS** | Yes (if $b$ is finite) | $O(b^d)$ | $O(bd)$ | Yes (if edge costs are equal) |
| **Uninformed** | **UCS** | Yes | $O(b^{1 + \lfloor C^* / \epsilon \rfloor})$ | $O(b^{1 + \lfloor C^* / \epsilon \rfloor})$ | **Yes** (by total path cost) |
| **Informed** | **Greedy Search** | No (can get stuck in loops) | $O(b^m)$ | $O(b^m)$ | No |
| **Informed** | **A\* Search** | **Yes** | $O(b^d)$ | $O(b^d)$ | **Yes** (if $h(n)$ is admissible/consistent) |

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.x installed on your local environment.

```bash
python --version
