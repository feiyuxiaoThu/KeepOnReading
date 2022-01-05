# 字符串、向量和数组

## 标准库类型 string

+ 直接初始化与拷贝初始化

  ```c++
  string s5 = "hiya"; // 拷贝
  string s6("hiya"); // 直接
  string s7(10,'c'); //直接
  ```

+ 使用 getline 读取一整行
+ 字符串字面值和 string 是不同的类型

### 处理每一个字符：使用基于范围的 for 语句

```c++
string str("some string");
for (auto c : str)
    cout << c <<endl; // 每行输出 str 中的一个字符
```

## 标准库类型 vector

标准库类型 vector 表示对象的集合，其中所有对象的类型都相同。集合中每一个对象都有一个索引可以用于访问对象。

...

## 迭代器介绍

