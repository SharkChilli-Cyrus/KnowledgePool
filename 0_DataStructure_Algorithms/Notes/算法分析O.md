# 算法分析 O

[TOC]

---

## 什么是算法分析

为了解决同一种问题可能会有许多种不同的算法，在比较不同种类的算法中以某种度量方式进行比较，最终选用更加高效的算法，而**算法分析**就是基于每种算法使用的计算资源量来比较不同算法之间的差异。

- 基于所需的**空间**资源
- 基于所需的**时间**资源

**基准测试**计算的是程序执行的实际时间，它并不能真正提供一个有用的度量，因为它取决于机器配置，程序设计，选用的编译器和使用的编程语言。因此，需要一个**独立于所使用的程序或计算机**的度量，用以比较不同实现方法的算法效率。



## 大 O 符号

可以通过量化算法执行的步骤或所需要的操作来度量算法的效率，一个比较好的基本计算单位是对执行语句进行计数。

例如：

```python
total = 0
for _ in range(n):
    total += i
```

赋值语句 `total = 0` 计数为1，进行n次循环以累加前n个数，因此我们可以用函数 $T(n) = 1 + n$ 来度量这个算法，即 $1 + n$ 步长，其中 $n$ 称为**问题的规模** ，而我们的目标是**表示出算法的执行时间是如何相对问题规模的大小而改变的**。

事实上，确定 $T(n)$ 中最主要的部分比计算总的步长 $1 + n$ 更重要，即问题规模变大时，$T(n)$ 中最主要的部分几乎能反映整体的变化情况，而其他分量的影响则可以忽略不计。

而函数 $T(n)$ 中最主要的部分即是随着 $n$ 的增加而增加最快的部分，称之为**函数的数量级**，通常用大 $O$ 表示，写为 $O(f(n))$。

对于某一确定步长为 $T(n) = 5n^2 + 27n + 9527$ 的算法，随着 $n$ 的增大， 分量 $n^2$ 则变得越来越重要，因此我们可以说 $T(n)$ 的数量级为 $f(n)=n^2$，或者 $O(n^2)$

以下是大 $O$ 的常用表示方程：

| **$f(n)$** | **Name**    |
| :--------- | ----------- |
| $1$        | Constant    |
| $log(n)$   | Logarithmic |
| $n$        | Linear      |
| $nlog(n)$  | Log Linear  |
| $n^2$      | Quadratic   |
| $n^3$      | Cubic       |
| $2^n$      | Exponential |

![O](https://tva1.sinaimg.cn/large/007S8ZIlgy1gixlot0h2lj30ih0d73zx.jpg)

例如：

```python
a = 1
b = 2
c = 3

for i in range(n):
    for j in range(n):
        x = j * j
        y = j * j
        z = i * j
        
for k in range(n):
    p = a * k + 1
    q = b * b
    
d = 4
```

针对上面这段代码， $T(n) = 3 + 3\cdot n^2 + 2\cdot n + 1 \Rightarrow O(n^2)$



## 实例 - 字符串的乱序检查

乱序字符串指的是一个字符串是另一个字符串的重新排列，例如 `hello` 和 `ohell`，`python` 和 `nopyth`。为简单起见，约束检测的两个字符串具有相同的长度且由26个小写字母组合而成。

### Solution 1

```python
def check1(s1, s2):
    alist = list(s2)
    
    run_option = True
    pos1 = 0
    while pos1 < len(s1) and run_option:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
          	else:
                pos2 = pos2 + 1
                
 		if found:
            alist[pos2] = None
      	else:
            run_option = False
       	pos1 += 1
        
 	return run_option    
```

分析如上解法，两个字符串的长度同为 n，s1 的每个字符都会在 s2 中最多进行 n 个字符的迭代，同时在 s2 中使用 `None` 对已匹配的字符进行替换，因此总共的访问次数可以写成 1 到 n 的整数和：

$\sum_{i=1}^{n} i=\frac{n(1+n)}{2}=\frac{1}{2}n^2+\frac{1}{2}n$，这个算法的复杂度即为 $O(n^2)$。

