# Prueba IGX

You are given a rooted tree $T = (V, E)$ with $V = \{1, 2, ..., n\}$. The vertex $1$ is the root of $T$. You are then given $Q$ queries. Each query consists of two vertices $u, v \in V$ and the goal is to judge whether $u$ is an ancestor of $v$. Note that a vertex is considered to be an ancestor of itself.

**Input**  
The first line contains two positive integers $n$ ($1 \le n \le 10^5$) and $Q$ ($1 \le Q \le 10^5$). Each of the following $n - 1$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), meaning that there is an edge between $u$ and $v$ in $T$. Each of the following $Q$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) which corresponds to a query.

**Output**  
For each query, display YES if $u$ is ancestor of $v$, otherwise display NO.

## Example

| input | output |
|---|---|
| 4 5 | YES |
| 1 3 | YES |
| 3 2 | NO |
| 2 4 | YES |
| 1 4 | YES |
| 4 4 | NO |
| 4 1 |  |
| 3 4 |  |
| 4 3 |  |