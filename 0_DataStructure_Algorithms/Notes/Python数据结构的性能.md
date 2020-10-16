# Python 数据结构的性能

[TOC]

---

* [Time Complexity in Python](https://wiki.python.org/moin/TimeComplexity)

## 列表

当扩展列表时，可以使用 `append` 或 拼接运算符，`append` 方法复杂度为 $O(1)$，而拼接运算符复杂度为 $O(k)$， 其中 k 是要拼接的列表的大小。

当列表末尾调用 `pop` 时，复杂度为 $O(1)$， 而挡在列表中第一个元素或中间任何地方调用 `pop` 时，复杂度为 $O(n)$，其原因是当一个元素从列表前部取出时，列表中的其他元素都需要移动一个位置。

| Operation          | Big-O Efficiency   |
| ------------------ | ------------------ |
| index [ ]          | $O(1)$             |
| index assignment   | $O(1)$             |
| append             | $O(1)$             |
| pop()              | $O(1)$             |
| pop(i)             | $O(n)$             |
| insert(i, element) | $O(n)$             |
| del operator       | $O(n)$             |
| iteration          | $O(n)$             |
| contains (in)      | $O(n)$             |
| get slice [a:b]    | $O(k)$             |
| del slice          | $O(n)$             |
| set slice          | $O(n+k)$           |
| reverse            | $O(n)$             |
| concatenate        | $O(k)$             |
| sort               | $O(n\cdot log(n))$ |
| multiply           | $O(n\cdot k)$      |



## 字典

字典的 `get` 和 `set` 操作都是 $O(1)$， 另一个重要操作是 contains，检查一个key是否再字典中也是 $O(1)$。

| Operation     | Big-O Efficiency |
| ------------- | ---------------- |
| copy          | $O(n)$           |
| get item      | $O(1)$           |
| set item      | $O(1)$           |
| delete item   | $O(1)$           |
| contains (in) | $O(1)$           |
| iteration     | $O(n)$           |

