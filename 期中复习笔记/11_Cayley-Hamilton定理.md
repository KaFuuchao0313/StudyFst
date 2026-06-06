# 主题11：Cayley-Hamilton 定理

## 1. 定理陈述

> **定理**（Cayley-Hamilton）：设 $p_A(\lambda) = \det(\lambda I - A)$ 是 $A \in \mathbb{C}^{n \times n}$ 的特征多项式，则
> $$p_A(A) = O$$

即每个方阵都满足它自己的特征方程。

---

## 2. 证明要点

### 2.1 利用 Schur 分解

设 $A$ 的 Schur 分解为 $A = U T U^H$，其中 $T$ 是上三角阵，对角元为特征值 $\lambda_1, \ldots, \lambda_n$。

特征多项式 $p_A(\lambda) = \prod_{i=1}^n (\lambda - \lambda_i)$。

由于 $p_A(A) = U p_A(T) U^H$，只需证明 $p_A(T) = O$。

**完整证明**：

设 $T$ 的特征值为 $\lambda_1, \ldots, \lambda_n$，特征多项式 $p_A(\lambda) = \prod_{i=1}^n (\lambda - \lambda_i)$。

我们需证明 $p_A(T) = \prod_{i=1}^n (T - \lambda_i I) = O$。

**关键引理**：设 $T$ 是形如 $T = \begin{pmatrix} \alpha & * \\ 0 & T_1 \end{pmatrix}$ 的上三角阵，其中 $\alpha$ 是标量，$T_1$ 是 $n-1$ 阶上三角阵。若 $T_1$ 左上角的 $k \times k$ 子块是全零矩阵，则 $(T - \alpha I)$ 左上角的 $(k+1) \times (k+1)$ 子块是全零矩阵。

**证明**：
注意到 $T - \alpha I = \begin{pmatrix} 0 & * \\ 0 & T_1 - \alpha I \end{pmatrix}$。

若 $T_1$ 左上角 $k \times k$ 子块为零，则 $T_1 - \alpha I$ 左上角 $k \times k$ 子块也为零（对角元减去 $\alpha$ 后变成 $-\alpha$，但我们关注的是分块结构）。

实际上，更精确地说：记 $T$ 的分块为
$$T = \begin{pmatrix} \lambda_1 & t^T \\ 0 & T' \end{pmatrix}$$

其中 $T'$ 是 $n-1$ 阶上三角阵，对角元为 $\lambda_2, \ldots, \lambda_n$。

计算 $(T - \lambda_1 I)$：
$$(T - \lambda_1 I) = \begin{pmatrix} 0 & t^T \\ 0 & T' - \lambda_1 I \end{pmatrix}$$

左上角的 $1 \times 1$ 子块是 $[0]$。

假设 $(T - \lambda_1 I)(T - \lambda_2 I) \cdots (T - \lambda_k I)$ 左上角的 $k \times k$ 子块是全零矩阵。考虑
$$(T - \lambda_1 I)(T - \lambda_2 I) \cdots (T - \lambda_k I)(T - \lambda_{k+1} I)$$

设前 $k$ 个矩阵的乘积为 $\begin{pmatrix} 0_k & * \\ 0 & B \end{pmatrix}$，其中 $0_k$ 是 $k \times k$ 零矩阵。

乘以 $(T - \lambda_{k+1} I)$ 后，左上角的 $(k+1) \times (k+1)$ 子块仍为零矩阵（由上三角阵乘法性质）。

由数学归纳法，$p_A(T)$ 左上角的 $n \times n$ 子块（即整个矩阵）是全零矩阵。 $\square$

### 2.2 扰动法（邵老师证明）

**核心思想**：对于有重特征值的矩阵，通过微小扰动使特征值分离，从而可对角化；再利用连续性过渡回原矩阵。

**证明概要**：
1. 定义 $A(\epsilon) = A + \epsilon D$，其中 $D$ 是使 $A(\epsilon)$ 的特征值互不相同的对角阵，$\epsilon > 0$ 足够小。

2. 由于 $A(\epsilon)$ 有 $n$ 个互不相同的特征值，故可对角化：$A(\epsilon) = V(\epsilon) \Lambda(\epsilon) V(\epsilon)^{-1}$。

3. 特征多项式 $p_{A(\epsilon)}(\lambda) = \prod_{i=1}^n (\lambda - \lambda_i(\epsilon))$。

4. 对于可对角化矩阵，容易验证 $p_{A(\epsilon)}(A(\epsilon)) = O$：
   $$p_{A(\epsilon)}(A(\epsilon)) = V(\epsilon) p_{A(\epsilon)}(\Lambda(\epsilon)) V(\epsilon)^{-1} = V(\epsilon) \cdot O \cdot V(\epsilon)^{-1} = O$$

5. 令 $\epsilon \to 0$，由连续性得 $p_A(A) = O$。 $\square$

---

## 3. 应用

### 3.1 表示矩阵的幂

**高次幂**：可将 $A^n$ 表示为 $I, A, \ldots, A^{n-1}$ 的线性组合。

**例**：设 $A \in \mathbb{C}^{3 \times 3}$，特征多项式 $p_A(\lambda) = \lambda^3 - 2\lambda^2 + \lambda - 1$，则
$$A^3 = 2A^2 - A + I$$
$$A^4 = A \cdot A^3 = 2A^3 - A^2 + A = 3A^2 - 2A + 2I$$

### 3.2 求逆矩阵

若 $A$ 非奇异，特征多项式 $p_A(\lambda) = \lambda^n + a_{n-1}\lambda^{n-1} + \cdots + a_1 \lambda + a_0$，则 $a_0 = (-1)^n \det(A) \neq 0$。

由 $p_A(A) = O$ 得：
$$A^{-1} = -\frac{1}{a_0}(A^{n-1} + a_{n-1}A^{n-2} + \cdots + a_1 I)$$

### 3.3 伴随矩阵的表示

$A$ 的伴随矩阵 $\mathrm{adj}(A)$ 可表示为 $A$ 的不超过 $n-1$ 次多项式。

---

## 4. 极小多项式

### 4.1 定义

使 $A$ 零化的**最低次数**的首一多项式称为 $A$ 的**极小多项式**，记作 $m_A(\lambda)$。

### 4.2 性质

1. 极小多项式存在且唯一
2. 极小多项式整除特征多项式：$m_A \mid p_A$
3. 相似矩阵有相同的极小多项式
4. 特征多项式的每个根都是极小多项式的根

### 4.3 与 Jordan 标准型的联系

设 $A$ 的 Jordan 标准型中，特征值 $\lambda_i$ 对应的最大 Jordan 块阶数为 $k_i$，则
$$m_A(\lambda) = \prod_{i=1}^s (\lambda - \lambda_i)^{k_i}$$

### 4.4 可对角化的极小多项式判别

> **定理**：$A$ 可对角化 $\Leftrightarrow$ 极小多项式无重根

---

## 5. Frobenius 友阵

### 5.1 定义

对于 $n$ 次首一多项式 $p(\lambda) = \lambda^n + a_{n-1}\lambda^{n-1} + \cdots + a_1 \lambda + a_0$，其 **Frobenius 友阵**为：
$$F = \begin{pmatrix} 
0 & 0 & \cdots & 0 & -a_0 \\
1 & 0 & \cdots & 0 & -a_1 \\
0 & 1 & \cdots & 0 & -a_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \cdots & 1 & -a_{n-1}
\end{pmatrix}$$

### 5.2 性质

- $F$ 的特征多项式为 $p(\lambda)$
- $F$ 的极小多项式也为 $p(\lambda)$
- $F$ 是非退化的（每个特征值几何重数为 1）
- $F$ 的特征值 $\lambda$ 对应的特征向量为 $(1, \lambda, \lambda^2, \ldots, \lambda^{n-1})^T$

### 5.3 多项式求根与矩阵特征值

**多项式求根问题** $\Leftrightarrow$ **友阵求特征值问题**
