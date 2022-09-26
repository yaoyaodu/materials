# LaTeX基本数学公式

来源：[使用LaTeX基本数学公式_nankeyimeng的博客-CSDN博客](https://blog.csdn.net/qq_32126633/article/details/78725235)

资料：

* LaTeX公式篇：https://zhuanlan.zhihu.com/p/110756681
* LaTeX公式手册（全网最全）：https://www.cnblogs.com/1024th/p/11623258.html
* [color - How can I make a coloured footrule using fancyhdr? - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/461675/how-can-i-make-a-coloured-footrule-using-fancyhdr)
* [Latex 定制 — Sphinx documentation (osgeo.cn)](https://www.osgeo.cn/sphinx/latex.html)

# 使用LaTeX写公式的基本语法

正文中的公式用 `$...$` 来定义，单独显示的用 `$$...$$` 来定义。docsify需要将公式用···tex···进行包围。

1. 行内公式       $f(x) = \sum*_{i=0}^{N}\int_*{a}^{b} g(t,i) \text{ d}t$

2. 行间公式

   ```tex
   f(x) = \sum*_{i=0}^{N}\int_*{a}^{b} g(t,i) \text{ d}t
   ```
   
   docsify不支持$$包围

$$
f(x) = \sum*_{i=0}^{N}\int_*{a}^{b} g(t,i) \text{ d}t
$$



​		用tex出错

$$
\varGamma(x) = \frac{\int_{\alpha}^{\beta} g(t)(x-t)^2\text{ d}t }{\phi(x)\sum_{i=0}^{N-1} \omega_i} \tag{2}
$$





# 基本LaTeX公式命令

## 希腊字母

> | 命令       | 显示 |      | 命令     | 显示 |
> | :--------- | :--- | :--- | :------- | :--- |
> | `\alpha`   | α    |      | `\beta`  | β    |
> | `\gamma`   | γ    |      | `\delta` | δ    |
> | `\epsilon` | ϵ    |      | `\zeta`  | ζ    |
> | `\eta`     | η    |      | `\theta` | θ    |
> | `\iota`    | ι    |      | `\kappa` | κ    |
> | `\lambda`  | λ    |      | `\mu`    | μ    |
> | `\xi`      | ξ    |      | `\nu`    | ν    |
> | `\pi`      | π    |      | `\rho`   | ρ    |
> | `\sigma`   | σ    |      | `\tau`   | τ    |
> | `\upsilon` | υ    |      | `\phi`   | ϕ    |
> | `\chi`     | χ    |      | `\psi`   | ψ    |
> | `\omega`   | ω    |      |          |      |

如果使用大写的希腊字母，把命令的首字母变成大写即可，例如 `\Gamma` 输出的是 Γ。

如果使用斜体大写希腊字母，再在大写希腊字母的*LaTeX*命令前加上var，例如`\varGamma` 生成 Γ。



## 简单运算

拉丁字母、阿拉伯数字和 +-*/= 运算符均可以直接输入获得。

| 命令     | 含义       | 命令      | 含义 |
| :------- | ---------- | :-------- | ---- |
| `\cdot`  | 乘法的圆点 | `\bmod`   | 取模 |
| `\neq`   | 不等号     | `'`       | 求导 |
| `\equiv` | 恒等于     | `\bigcap` |      |

## 和号、积分号、乘积

> | 命令      | 含义 | 显示 | 命令      | 含义 | 显示 |
> | :-------- | ---- | :--- | :-------- | ---- | :--- |
> | `\sum`    | 求和 | ∑    | `\int`    | 积分 | ∫    |
> | `\prod`   | 乘积 | ∏    | `\iint`   |      | ∬    |
> | `\bigcup` |      | ⋃    | `\bigcap` |      | ⋂    |



## 其它常用命令

> | 命令             |                           | 命令          |                        |
> | :--------------- | ------------------------- | :------------ | ---------------------- |
> | `\sqrt`          | 平方根                    | `\sqrt[n]`    | n次方根                |
> | `\lim_{x \to 0}` | 极限                      | `\frac{1}{2}` | 分式                   |
> | `^`              | 上标                      | `_`           | 下标                   |
> | `\overline`      | 在表达式上方画出水平线    | `\underline`  | 在表达式下方画出水平线 |
> | `\underline{~}`  | 数学公式环境下插入_的方式 |               |                        |

 

> **注意**：上标和下标在只有一个字符时，可以不用中括号: `x^2`和`x^{2}`的结果是一样的。

## 三圆点、矩阵

| 命令     | 含义         | 命令       | 含义   |
| :------- | ------------ | :--------- | ------ |
| `\ldots` | 点位于基线上 | `\matrix`  | 无括号 |
| `\cdots` | 点设置为居中 | `\bmatrix` | 大括号 |
| `\vdots` | 使其垂直     | `\vmatrix` | 垂直线 |
| `\ddots` | 对角线排列   | `\pmatrix` | 圆括号 |

## 行列

`&`用于分隔列，`\`用于分隔行。

# 总结

本文介绍的是一些基本的*LaTeX* 公式命令。未尽之处，大家可以参考[这里](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)。