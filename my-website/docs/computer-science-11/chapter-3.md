---
id: chapter-3
title: "Chapter 3: Algorithms and Problem Solving"
sidebar_label: "Chapter 3: Algorithms and Problem Solving"
sidebar_position: 3
---

# Unit 3: Algorithms and Problem Solving

## Student Learning Outcomes

By the end of this chapter, students will be able to:

- Describe and categorize different types of computational problems.
- Explain the importance of algorithms in problem-solving.
- Apply the generate-and-test method to solve computational problems.
- Differentiate between solvable and unsolvable problems.
- Understand problem complexity and categorize problems into P, NP, NP-Hard, NP-Complete.
- Identify common computational problems like sorting and searching.
- Apply algorithm design techniques such as divide and conquer, greedy methods, and dynamic programming.
- Implement and compare algorithms such as Bubble Sort, Binary Search, BFS, and DFS.
- Evaluate algorithms in terms of efficiency and scalability.
- Develop algorithmic thinking to solve problems systematically.

## Introduction

Understanding algorithms is essential not only for computer science but also for everyday problem-solving. We will start by learning what computational problems are and how to describe them clearly. Then, we will look at different types of algorithms and how they can help us solve various kinds of problems. We will also discuss how to measure the efficiency of algorithms to find the best solutions.

---

## 3.1 Understanding Computational Problems

A computational problem is a challenge that can be solved through a computational process, which involves an algorithm — a set of step-by-step instructions that a computer can execute.

- **Input:** The data or information given to the algorithm at the beginning of the problem.
- **Process:** The steps or rules (i.e., the algorithm) that are applied to the input to generate the output.
- **Output:** The solution or result produced by the algorithm after processing the input.

### 3.1.1 Characterizing Computational Problems

To solve a problem computationally, we need to understand its characteristics. This involves identifying the inputs, the desired outputs, and the process needed to transform the inputs into outputs.

#### 3.1.1.1 Classifying Computational Problems

Computational problems can be classified into different categories based on their characteristics and the methods required to solve them:

- **Decision Problems:** Problems where the output is a simple "yes" or "no."
- **Search Problems:** Problems where the task is to find a solution or an item that meets certain criteria.
- **Optimization Problems:** Problems where the goal is to find the best solution according to some criteria.
- **Counting Problems:** Problems where the objective is to count the number of ways certain conditions can be met.

#### 3.1.1.2 Well-defined vs. Ill-defined Problems

Problems can also be categorized based on how clearly they are defined:

- **Well-defined Problems:** These problems have clear goals, inputs, processes, and outputs. For instance, determining if a number is even is a well-defined problem — it has a clear goal, clear input (a single integer), a clear process (check if divisible by 2), and a clear output (even or odd).

- **Ill-defined Problems:** These problems lack clear definitions or may have ambiguous goals and requirements. For instance, "How to reduce poverty in Pakistan" is vague and broad.

![Figure 3.1: Flowchart for Finding an Even Number](/img/chapter-3/figure-3-1.svg)

*Figure 3.1: Flowchart for Finding an Even Number*

---

## 3.2 Algorithms for Problem Solving

Algorithms are step-by-step procedures for solving problems, much like a recipe provides steps for cooking a dish. Understanding algorithms is essential because they provide the logic behind software operations, allowing us to solve complex problems, optimize performance, and ensure accuracy in various applications.

> **Do You Know?** The Google search engine uses a complex algorithm called PageRank to determine the relevance of web pages. This algorithm considers various factors, including the number of links to a page and the quality of those links to rank pages in search results.

> **Tidbits:** When learning about algorithms, try to relate them to real-life tasks you already know. This will help you understand how algorithms work and why they are important.

### 3.2.1 Generate-and-Test Method

This method works by generating potential solutions to a problem and then testing each one to determine if it meets the required conditions. The process continues until a satisfactory solution is found or all possible solutions have been exhausted.

The Generate-and-Test method is particularly useful in scenarios where:

- The problem space is small, making it feasible to generate and test all possible solutions.
- There is no clear strategy for finding a solution, and an exhaustive search is necessary.
- Heuristics or rules can be applied to reduce the number of generated solutions, making the process more efficient.

![Figure 3.2: Flowchart of the Generate and Test Method](/img/chapter-3/figure-3-2.svg)

*Figure 3.2: Flowchart of the Generate and Test Method*

> **Do You Know?** The Generate-and-Test method is often used in AI applications, such as game playing and problem-solving, where the solution space is large and the best approach is to try different possibilities until one works!

---

## 3.3 Problem Solvability and Complexity

Problem solvability and complexity helps us determine whether a problem can be solved by an algorithm and, if so, how efficiently it can be solved.

### 3.3.1 Solvable vs. Unsolvable Problems

In computer science, problems are classified as solvable or unsolvable based on whether there exists an algorithm that can provide a solution:

- **Solvable Problems:** A problem is considered solvable if an algorithm can solve it within a finite amount of time. These problems have clearly defined inputs and outputs, and there is a step-by-step procedure to reach the solution.

  **Example:** Calculating the greatest common divisor (GCD) of two integers is a solvable problem. The Euclidean algorithm provides a clear and finite method to determine the GCD.

- **Unsolvable Problems:** A problem is unsolvable if no algorithm can be created that will provide a solution in all cases.

  **Example:** The **Halting Problem** is a famous example of an unsolvable problem. It involves determining whether a given program will eventually halt or continue to run forever. Alan Turing proved that no general algorithm can solve the Halting Problem for all possible program-input pairs.

> **Tidbits:** When tackling complex problems, it's essential to first determine whether the problem is solvable. This saves time and resources by ensuring you are working on a problem that can be resolved using an algorithm.

### 3.3.2 Tractable vs. Intractable Problems

Once a problem is determined to be solvable, the next consideration is its computational complexity — how efficiently it can be solved.

- **Tractable Problems:** A problem is considered tractable if it can be solved in **polynomial time**, denoted as **P**. Tractable problems are considered "efficiently solvable."

  **Example:** Sorting a list of numbers using algorithms such as Merge Sort or Quick Sort is a tractable problem because these algorithms have a polynomial time complexity of O(n log n).

- **Intractable Problems:** Intractable problems require super-polynomial time to solve, often growing exponentially with the size of the input. These problems are impractical to solve for large inputs.

  **Example:** The **Traveling Salesman Problem (TSP)** — finding the shortest possible route that visits a set of cities and returns to the origin — is NP-hard. As the number of cities increases, the number of possible routes grows factorially.

### 3.3.3 Complexity Classes (P, NP, NP-Hard, NP-Complete)

#### 3.3.3.1 Class P

Class P refers to problems that can be solved efficiently by a computer — even as the size of the problem grows.

**Example:** Sorting a list `[4, 1, 3, 2, 5]` into `[1, 2, 3, 4, 5]`. The time required grows at a manageable rate as the list size increases.

#### 3.3.3.2 Class NP

Class NP refers to problems for which, if a solution is given, it can be **checked quickly** by a computer. Finding the solution might be difficult, but verifying it is easy.

**Example:** Solving a **Sudoku** puzzle. Verifying that a completed Sudoku is correct is easy, but finding the solution can be hard.

![Figure 3.3: A Simple Sudoku Puzzle](/img/chapter-3/figure-3-3.svg)

*Figure 3.3: A Simple Sudoku Puzzle*

#### 3.3.3.3 Class NP-Hard

NP-Hard problems are at least as difficult as the hardest problems in NP. No efficient algorithm is known for finding a solution.

**Example:** The Traveling Salesman Problem (TSP) discussed in Section 3.3.2.

#### 3.3.3.4 NP-Complete

NP-Complete problems are both in NP and as hard as the hardest problems in NP. If you can solve one NP-Complete problem efficiently, you can solve all NP problems efficiently.

**Example:** The **Knapsack Problem** — given a knapsack with a maximum weight capacity and a set of items each with a weight and a value, find the most valuable combination of items without exceeding the weight capacity.

![Figure 3.4: Venn diagram of the complexity classes P, NP, NP-Hard, and NP-Complete](/img/chapter-3/figure-3-4.svg)

*Figure 3.4: Venn diagram of the complexity classes P, NP, NP-Hard, and NP-Complete*

> **Do You Know?** The question of whether P equals NP is one of the most important unsolved problems in computer science. It has significant implications for cryptography, algorithm design, and the overall understanding of computational complexity.

---

## 3.4 Algorithm Analysis

Algorithm analysis is the process of determining the computational complexity of algorithms, which includes their time and space complexity. This analysis helps predict the algorithm's performance and is crucial for selecting the best algorithm for a particular task.

### 3.4.1 Time Complexity

Time complexity is a measure of how the running time of an algorithm increases as the size of the input data grows. It helps us understand how efficiently an algorithm performs when dealing with larger amounts of data.

#### 3.4.1.1 Big O Notation

Big O notation is a mathematical way to describe the time complexity of an algorithm. It provides an upper bound on the time an algorithm will take to complete as the input size grows.

**Common examples:**

| Notation | Name | Description |
|----------|------|-------------|
| **O(1)** | Constant Time | Runtime remains the same regardless of input size. |
| **O(n)** | Linear Time | Runtime grows linearly with input size. Example: searching through n students one by one. |
| **O(n²)** | Quadratic Time | Runtime increases with the square of input size. Example: comparing every pair of n students. |
| **O(log n)** | Logarithmic Time | Runtime grows very slowly. Example: binary search — each step halves the search range. |

![Figure 3.5: Growth of asymptotic notations](/img/chapter-3/figure-3-5.svg)

*Figure 3.5: Growth of asymptotic notations*

When comparing time complexities, **O(1)** (constant time) is the most efficient — the runtime stays the same no matter how large the input is.

### 3.4.2 Space Complexity

Space complexity measures how the amount of memory an algorithm uses changes as the size of the input data increases. It helps us understand how efficiently an algorithm uses memory when handling large datasets.

**Example:** If an algorithm needs to store a list of numbers, its space complexity tells us how much memory will be required as the volume of numbers increases.

---

## 3.5 Algorithm Design Techniques

Algorithm design involves creating systematic methods to solve problems efficiently and effectively. There are several well-known techniques that help in developing robust algorithms.

### 3.5.1 Divide and Conquer

Divide and Conquer is a powerful technique that works by breaking a large problem into smaller, more manageable parts. Each smaller part is solved independently, and then their solutions are combined to solve the original problem.

This approach is particularly effective for problems that can be divided into similar smaller problems.

![Figure 3.6: Merge Sort process using Divide and Conquer](/img/chapter-3/figure-3-6.svg)

*Figure 3.6: Merge Sort process using Divide and Conquer*

> **Do You Know?** Big O notation helps computer scientists understand the efficiency of an algorithm in the worst-case scenario, allowing them to predict how well it will perform as the size of the input data increases.

### 3.5.2 Greedy Algorithms

Greedy algorithms work by making a sequence of choices, each of which is **locally optimal**, with the hope that these choices will lead to a globally optimal solution. The greedy approach is often used when a problem has an optimal substructure.

**Example:** The **Coin Change Problem** — given coins of different denominations, make a specific amount with the fewest coins possible. A greedy algorithm would choose the largest denomination coin that does not exceed the remaining amount, then subtract and repeat.

> **Tidbits:** Greedy algorithms are often faster and easier to implement than other techniques, but don't always guarantee the optimal solution for every problem. Always analyze the problem to ensure a greedy approach is appropriate.

### 3.5.3 Dynamic Programming

Dynamic Programming (DP) is an optimization technique used to solve problems by breaking them down into simpler subproblems and **storing the results** of these subproblems to avoid redundant calculations. DP is particularly useful for problems with overlapping subproblems and optimal substructure.

**Example:** The **Fibonacci sequence** — instead of recalculating Fibonacci numbers repeatedly, DP stores the results of each Fibonacci number as it is computed, allowing the algorithm to retrieve these values directly when needed.

### 3.5.4 Backtracking

Backtracking is a method used in solving problems where you build up a solution step by step. If you find that a particular path doesn't lead to a solution, you go back and try a different path. It's like trying out different routes on a map and turning back if you're going the wrong way.

This method is often used for problems where you need to look at all possible options, like puzzles or problems that involve different combinations.

---

## 3.6 Commonly Used Algorithms

### 3.6.1 Sorting Algorithms

Sorting algorithms are used to arrange data in a particular order, such as ascending or descending. Sorting is a fundamental operation that often serves as a prerequisite for other tasks like searching and data analysis.

#### 3.6.1.1 Bubble Sort

Bubble Sort works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order. This process is repeated until the list is sorted.

**Process:**
1. Start at the beginning of the list.
2. Compare each pair of adjacent elements.
3. Swap them if they are in the wrong order.
4. Continue the process until no more swaps are needed.

**Example:** For the list `[5, 3, 8, 4, 2]`, Bubble Sort will first compare 5 and 3, swap them, then move to the next pair. After several passes, the algorithm will sort the list as `[2, 3, 4, 5, 8]`.

**Complexity:** O(n²) — inefficient for large datasets, but easy to understand and implement.

> **Tidbits:** While Bubble Sort is easy to implement, consider using more efficient sorting algorithms like Quick Sort or Merge Sort for larger datasets to save time and resources.

#### 3.6.1.2 Selection Sort

Selection Sort works by selecting the smallest element from the unsorted part of the list and swapping it with the first element of the unsorted part. This process is repeated for the remaining unsorted portion.

**Process:**
1. Find the minimum element in the unsorted part of the list.
2. Swap it with the first unsorted element.
3. Move the boundary of the sorted and unsorted sections by one element.
4. Repeat the process for the remaining elements.

**Example:** For the list `[29, 10, 14, 37, 13]`, Selection Sort finds the smallest element (10) and swaps it with 29. The list becomes `[10, 29, 14, 37, 13]`. The process continues until the list is fully sorted.

**Complexity:** O(n²) — not efficient for large datasets but straightforward to implement.

---

### 3.6.2 Search Algorithms

Search algorithms are designed to find specific elements within a dataset. They are critical for tasks such as information retrieval, database queries, and decision-making processes.

#### 3.6.2.1 Linear Search

A linear search checks each item one by one until the target is found.

**Process:**
1. Start at the beginning of the list.
2. Compare each item with the target.
3. If they don't match, move to the next item.
4. Repeat until found or end of list is reached.

**Example:** Searching for "Islamabad" in `[Karachi, Lahore, Islamabad, Faisalabad]`:
- Check Karachi → not a match.
- Check Lahore → not a match.
- Check Islamabad → **found!**

#### 3.6.2.2 Binary Search

Binary Search is an efficient algorithm for finding an item in a **sorted list**. It works by repeatedly dividing the search interval in half.

**Process:**
1. Start with the middle element of the sorted list.
2. If the middle element is the target, return its position.
3. If the target is smaller, repeat the search on the left half.
4. If the target is larger, repeat the search on the right half.

**Example:** Searching for `7` in `[1, 3, 5, 7, 9, 11, 13]` — Binary Search starts at the middle element (7) and finds the target immediately.

**Complexity:** O(log n) — much faster than linear search, especially for large datasets.

![Figure 3.7: Binary Search Process](/img/chapter-3/figure-3-7.svg)

*Figure 3.7: Binary Search Process — the search interval is halved at each step*

> **Do You Know?** Binary Search is only effective on sorted lists. If your data isn't sorted, consider using a sorting algorithm like Merge Sort before applying Binary Search!

---

### 3.6.3 Graph Algorithms

Graph algorithms are used to explore and analyze graphs — data structures made up of nodes (vertices) connected by edges. These algorithms are essential for network analysis, route planning, and social network analysis.

#### 3.6.3.1 Breadth-First Search (BFS)

BFS explores all the nodes of a graph **level by level**, starting from a given node. It uses a **queue** to keep track of nodes to be explored.

**Process:**
1. Start from the root node and enqueue it.
2. Dequeue a node, process it, and enqueue all its unvisited neighbors.
3. Repeat until the queue is empty.

**Example:** In a social network graph, BFS can find the shortest path between two people (e.g., finding the degree of separation between two users).

**Complexity:** O(V + E), where V is the number of vertices and E is the number of edges.

#### 3.6.3.2 Depth-First Search (DFS)

DFS explores as far down a branch as possible before **backtracking** to explore other branches. It uses a **stack** to manage nodes.

**Process:**
1. Start from the root node and push it onto the stack.
2. Pop a node, process it, and push all its unvisited neighbors onto the stack.
3. Repeat until the stack is empty.

**Example:** DFS can be used to solve mazes — the algorithm explores one possible path to the end, and if it hits a dead end, it backtracks and tries another path.

**Complexity:** O(V + E) — similar to BFS. However, DFS is more memory-efficient for deep graphs, while BFS is better suited for shallow graphs.

![Figure 3.8: Comparison of BFS and DFS traversal](/img/chapter-3/figure-3-8.svg)

*Figure 3.8: Comparison of BFS and DFS traversal — BFS Output: 0,1,2,3,4,5,6,7 | DFS Output: 0,1,3,4,7,5,2,6*

---

## Exercise

### Multiple Choice Questions

1. The characteristic of a well-defined problem is:
   - a) Ambiguous goals and unclear requirements
   - b) Vague processes and inputs
   - **c) Clear goals, inputs, processes, and outputs**
   - d) Undefined solutions

2. Complexity class representing problems solvable efficiently by a deterministic algorithm:
   - a) NP
   - b) NP-Hard
   - c) NP-Complete
   - **d) P**

3. The statement that applies to unsolvable problems:
   - a) They can be solved in polynomial time
   - **b) They cannot be solved by any algorithm**
   - c) They are always in NP class
   - d) They require exponential time to solve

4. The meaning of NP in computational complexity:
   - **a) Non-deterministic Polynomial time**
   - b) Negative Polynomial time
   - c) Non-trivial Polynomial time
   - d) Numerical Polynomial time

5. Search algorithm more efficient for large datasets:
   - a) Bubble Sort
   - **b) Binary Search**
   - c) Selection Sort
   - d) Linear Search

6. A scenario where Dynamic Programming proves most useful:
   - a) Problems without overlapping subproblems
   - b) Problems solved by making local choices
   - **c) Problems with overlapping subproblems and optimal substructure**
   - d) Problems divided into independent subproblems

7. An algorithm that sorts data by stepping through the list and swapping adjacent elements if needed:
   - a) Selection Sort
   - b) Quick Sort
   - **c) Bubble Sort**
   - d) Merge Sort

8. Time complexity of Depth-First Search (DFS) in a graph:
   - a) O(n log n)
   - b) O(V)
   - **c) O(V + E)**
   - d) O(n)

9. Best description of time complexity:
   - a) Amount of memory an algorithm needs
   - **b) Time taken as a function of input size**
   - c) Efficiency as input size grows
   - d) Upper bound of space requirements

10. An algorithm with a time complexity of O(n log n):
    - a) Bubble Sort
    - b) Binary Search
    - **c) Merge Sort**
    - d) Insertion Sort

### Short Questions

1. Differentiate between well-defined and ill-defined problems within the realm of computational problem-solving.
2. Outline the main steps involved in the Generate-and-Test method.
3. Compare tractable and intractable problems in the context of computational complexity.
4. Summarize the key idea behind Greedy Algorithms.
5. Discuss the advantages of using Dynamic Programming.
6. Compare the advantages of Breadth-First Search (BFS) with Depth-First Search (DFS) in graph traversal.
7. Explain the importance of breaking down a problem into smaller components in algorithmic thinking.
8. Identify the key factors used to evaluate the performance of an algorithm.

### Long Questions

1. Provide a detailed explanation of why the Halting Problem is considered unsolvable and its implications in computer science.
2. Discuss the characteristics of search problems and compare the efficiency of Linear Search and Binary Search algorithms.
3. Discuss the nature of optimization problems and provide examples of their applications in real-world scenarios.
4. Explain the process and time complexity of the Bubble Sort algorithm. Compare it with another sorting algorithm of your choice in terms of efficiency.
5. Discuss the differences between time complexity and space complexity. How do they impact the choice of algorithm for a specific problem?
