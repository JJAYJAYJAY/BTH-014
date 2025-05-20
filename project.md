# 项目描述

## 简介

`pickle` 模块实现了用于序列化和反序列化 Python 对象结构的二进制协议。  
“Pickling” 是指将 Python 对象层次结构转换为字节流的过程，而 “unpickling” 则是其逆过程，即将字节流（来自二进制文件或类字节对象）转换回对象层次结构。Pickling（和 unpickling）也被称为 “序列化（serialization）”、“编组（marshalling）” 或 “扁平化（flattening）”；然而，为避免混淆，这里使用的术语是 “pickling” 和 “unpickling”。

我希望了解 `pickle` 的稳定性和正确性：同样的输入是否总是会生成相同的（序列化）输出？  
我们将“相同的输入和输出”定义为哈希值完全一致（等价是不够的）。这意味着一个输入必须在所有情况下生成相同的 pickle 文件。  
可能影响的因素包括不同操作系统、不同 Python 版本（但不包括不同的 `pickle` 版本）、浮点数精度和递归数据结构（例如 JSON）。  
请保持开放思维，考虑其他可能影响的因素。  
请确保只考虑**完全相同的输入**：如果改变输入（例如，将 `x = 2+3` 改为 `x = 3+2` 或重命名变量），结果可能等价，但在对生成的 pickle 文件进行哈希（如 sha256）时将不再相同。  

## 你的任务

你的任务是开发一个用于测试 `pickle` 的稳定性和正确性的测试套件。  
你应使用在课程中学到的测试技术（等价划分、边界值、模糊测试等）。  
由于 `pickle` 库的源代码是开放的，你还可以使用白盒测试方法（例如 all-def、all-uses）来进行测试。  
所有结果和发现都必须**可复现**。  

## 最终报告

你必须提交一个最终报告，内容按照测试计划和管理讲座中的要求撰写。  

### 你的最终报告应包括：
- 你的测试套件及所采用的测试策略。
- 通过可追溯性矩阵展示测试套件的完整性。
- 你的测试套件的发现和结果。
- 说明你为什么选择（或不选择）某种测试技术（例如，边界值分析）。
- 你的测试套件的局限性和不足之处。

报告不得超过 8 页，需列出所有团队成员及其在报告和代码中的具体贡献。  
你的代码必须符合 PEP8 编码风格，并存放在 GitHub、GitLab 或类似平台上。请提供你的代码仓库链接。  

## 一些参考链接

- https://stackoverflow.com/questions/985294/is-the-pickling-process-deterministic
- https://stackoverflow.com/questions/21271479/python-pickle-not-one-to-one-different-pickles-give-same-object
- https://stackoverflow.com/questions/75927084/are-pickle-files-reproducible