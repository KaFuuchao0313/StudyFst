# 主题12：Jordan 标准型

## 1. Jordan 块

### 1.1 定义

给定正整数 $k$ 和复数 $\lambda$，**Jordan 块**定义为：
$$J_k(\lambda) = \begin{pmatrix}
\lambda & 1 & 0 & \cdots & 0 \\
0 & \lambda & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda & 1 \\
0 & 0 & \cdots & 0 & \lambda
\end{pmatrix}_{k \times k}$$

### 1.2 幂零 Jordan 块

$J_k(0)$ 称为**幂零 Jordan 块**，满足：
- $J_k(0)^k = O$
- $J_k(0)^{k-1} \neq O$
- $\mathrm{rank}(J_k(0)^j) = \max(0, k - j)$

---

## 2. Jordan 标准型定理

### 2.1 存在性

> **定理**（Jordan 标准型）：设 $A \in \mathbb{C}^{n \times n}$ 的不同特征值为 $\lambda_1, \ldots, \lambda_s$，代数重数分别为 $n_1, \ldots, n_s$，则存在非奇异矩阵 $P$ 使得
> $$P^{-1} A P = J = \begin{pmatrix} J_1 & & \\ & \ddots & \\ & & J_s \end{pmatrix}$$
> 其中 $J_i$ 是关于特征值 $\lambda_i$ 的 Jordan 矩阵（若干 Jordan 块的直和）。

**证明思路**（分三步）：

**第一步**：Schur 分解

由 Schur 分解定理，存在酉矩阵 $U$ 使得 $U^H A U$ 是上三角阵 $T$。通过适当排列，可将 $T$ 分块为
$$T = \begin{pmatrix} T_1 & * \\ 0 & T_2 \end{pmatrix}$$
其中 $T_1$ 的对角元全为 $\lambda_1$，$T_2$ 的对角元不含 $\lambda_1$。

**第二步**：块对角化

由于 $T_1 - \lambda_1 I$ 幂零（特征值全为 0），$T_2 - \lambda_1 I$ 非奇异（特征值不含 $\lambda_1$），根据 Sylvester 方程理论，存在唯一的 $X$ 使得
$$T_1 X - X T_2 = -T_{12}$$

令 $P = \begin{pmatrix} I & X \\ 0 & I \end{pmatrix}$，则
$$P^{-1} T P = \begin{pmatrix} T_1 & 0 \\ 0 & T_2 \end{pmatrix}$$

重复此过程，可将 $T$ 块对角化为 $\mathrm{diag}(T_1, \ldots, T_s)$，其中 $T_i$ 的对角元全为 $\lambda_i$。

**第三步**：化 Jordan 块

设 $T_i = \lambda_i I + N_i$，其中 $N_i$ 是严格上三角阵（幂零）。只需证明：**任意严格上三角阵相似于幂零 Jordan 块的直和**。

这可通过归纳法证明：对于严格上三角阵 $N$，存在非奇异矩阵 $Q$ 使得
$$Q^{-1} N Q = \mathrm{diag}(J_{k_1}(0), J_{k_2}(0), \ldots)$$

综合以上三步，命题得证。 $\square$

### 2.2 唯一性

Jordan 标准型在不考虑 Jordan 块排列顺序的意义下是唯一的。

**证明思路**：

唯一性基于以下事实：
1. 秩是相似不变量
2. 若 $A \sim B$，则 $A - \lambda I \sim B - \lambda I$（相似性在平移下保持）

定义 **Weyr 特征**：
$$w_j(\lambda) = \mathrm{rank}(A - \lambda I)^{j-1} - \mathrm{rank}(A - \lambda I)^j$$

关键观察：$w_j(\lambda)$ 等于关于特征值 $\lambda$ 的 Jordan 块中阶数 $\geq j$ 的个数。

因此，Jordan 块的个数和阶数完全由 Weyr 特征决定，而 Weyr 特征是相似不变量，故 Jordan 标准型唯一。 $\square$

---

## 3. 几何分解

### 3.1 Jordan 矩阵的结构

关于特征值 $\lambda_i$ 的 Jordan 矩阵：
$$J_i = \mathrm{diag}(J_{k_1}(\lambda_i), J_{k_2}(\lambda_i), \ldots, J_{k_{g_i}}(\lambda_i))$$
其中 $k_1 + k_2 + \cdots + k_{g_i} = n_i$（代数重数）。

### 3.2 关键计数

- **代数重数**：$n_i = \sum_{j=1}^{g_i} k_j$
- **几何重数**：$g_i$（关于 $\lambda_i$ 的 Jordan 块个数）
- 几何重数 $\leq$ 代数重数

### 3.3 特征值的类型

| 类型 | 条件 |
|------|------|
| 简单 | 代数重数 = 1 |
| 半简单 | 几何重数 = 代数重数（所有 Jordan 块都是 1 阶） |
| 有亏损 | 几何重数 < 代数重数（存在大于 1 阶的 Jordan 块） |

---

## 4. Weyr 特征

### 4.1 定义

设 $\lambda$ 是 $A$ 的特征值，定义：
$$w_j = \mathrm{rank}(A - \lambda I)^{j-1} - \mathrm{rank}(A - \lambda I)^j, \quad j = 1, 2, \ldots$$

**Weyr 特征**为序列 $(w_1, w_2, \ldots)$。

### 4.2 刻画 Jordan 块

- $w_1$：几何重数（Jordan 块个数）
- $w_j - w_{j+1}$：阶数 $\geq j$ 的 Jordan 块个数

---

## 5. 应用

### 5.1 可对角化条件

$A$ 可对角化 $\Leftrightarrow$ Jordan 标准型是对角阵 $\Leftrightarrow$ 所有 Jordan 块都是 1 阶 $\Leftrightarrow$ 所有特征值都是半简单的

### 5.2 矩阵函数

设 $A$ 的 Jordan 标准型为 $J = P^{-1}AP$，对于解析函数 $f$：
$$f(A) = P f(J) P^{-1}$$

对于 $k$ 阶 Jordan 块 $J_k(\lambda)$：
$$f(J_k(\lambda)) = \begin{pmatrix}
f(\lambda) & f'(\lambda) & \frac{f''(\lambda)}{2!} & \cdots & \frac{f^{(k-1)}(\lambda)}{(k-1)!} \\
0 & f(\lambda) & f'(\lambda) & \cdots & \frac{f^{(k-2)}(\lambda)}{(k-2)!} \\
\vdots & \vdots & \ddots & \ddots & \vdots \\
0 & 0 & \cdots & f(\lambda) & f'(\lambda) \\
0 & 0 & \cdots & 0 & f(\lambda)
\end{pmatrix}$$

**推导**：
设 $J_k(\lambda) = \lambda I + N$，其中 $N = J_k(0)$ 是幂零 Jordan 块。

由 Taylor 展开，$f(J_k(\lambda)) = f(\lambda I + N) = f(\lambda)I + f'(\lambda)N + \frac{f''(\lambda)}{2!}N^2 + \cdots$

由于 $N^k = O$，级数终止于 $N^{k-1}$ 项。

注意到 $N^j$ 将 1 向右上方移动 $j$ 步，即得上述矩阵形式。

### 5.3 $A$ 与 $A^T$ 相似

> **定理**：对于任意 $A \in \mathbb{C}^{n \times n}$，$A$ 与 $A^T$ 相似。

**证明**：利用逆序矩阵 $R$（反对角线全为 1，其余为 0），可验证 $R J_k(\lambda) R^{-1} = J_k(\lambda)^T$。

设 $A$ 的 Jordan 标准型为 $J = P^{-1}AP$，则
$$A^T = (PJP^{-1})^T = (P^{-1})^T J^T P^T = (P^T)^{-1} J^T P^T$$

由 $J = \mathrm{diag}(J_{k_1}(\lambda_1), \ldots, J_{k_m}(\lambda_m))$，定义
$$R = \mathrm{diag}(R_{k_1}, \ldots, R_{k_m})$$

其中 $R_{k_i}$ 是 $k_i$ 阶逆序矩阵。则
$$R J R^{-1} = J^T$$

因此 $J \sim J^T$，从而 $A \sim A^T$。 $\square$

### 5.4 Jordan-Chevalley 分解

> **定理**：任意复方阵 $A$ 可唯一分解为
> $$A = D + N$$
> 其中 $D$ 可对角化，$N$ 幂零，且 $DN = ND$。

**证明**：
设 $A$ 的 Jordan 标准型为 $J = P^{-1}AP = \mathrm{diag}(J_{k_1}(\lambda_1), \ldots, J_{k_m}(\lambda_m))$。

每个 Jordan 块可分解为 $J_{k_i}(\lambda_i) = \lambda_i I_{k_i} + J_{k_i}(0)$。

令
$$\tilde{D} = \mathrm{diag}(\lambda_1 I_{k_1}, \ldots, \lambda_m I_{k_m}), \quad \tilde{N} = \mathrm{diag}(J_{k_1}(0), \ldots, J_{k_m}(0))$$

则 $J = \tilde{D} + \tilde{N}$，其中 $\tilde{D}$ 是对角阵，$\tilde{N}$ 是幂零阵，且 $\tilde{D}\tilde{N} = \tilde{N}\tilde{D}$。

定义 $D = P\tilde{D}P^{-1}$，$N = P\tilde{N}P^{-1}$，则 $A = D + N$，且 $D$ 可对角化，$N$ 幂零，$DN = ND$。

**唯一性**：设 $A = D_1 + N_1 = D_2 + N_2$ 是两个分解，则 $D_1 - D_2 = N_2 - N_1$。

由于 $D_1, D_2$ 可对角化且与 $N_1, N_2$ 交换，故 $D_1 - D_2$ 可对角化且幂零，从而 $D_1 - D_2 = O$，即 $D_1 = D_2$，$N_1 = N_2$。 $\square$

---

## 6. 实 Jordan 标准型

实方阵的复特征值成共轭对出现。对于共轭特征值 $a \pm bi$，对应的实 Jordan 块为：
$$\begin{pmatrix}
C & I & & \\
& C & \ddots & \\
& & \ddots & I \\
& & & C
\end{pmatrix}, \quad C = \begin{pmatrix} a & b \\ -b & a \end{pmatrix}$$

---

## 7. 数值不稳定性

Jordan 标准型在数值计算中是不稳定的。方阵元素的微小扰动可能导致 Jordan 结构的剧烈变化。

**例**：$J_n(0) + \epsilon E_{1n}$ 的特征值为 $\epsilon^{1/n}$ 的 $n$ 次根，当 $n$ 较大时远离原点。
