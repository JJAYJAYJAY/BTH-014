# BTH-014（English Version）

## introduction

This project tests the serialization functionality of the `pickle` module under mainstream operating systems including
**Linux**, **macOS**, and **Windows**, using Python versions **3.6**, **3.9**, and **3.11**.

This project uses **conda environments** to manage and test different Python versions.

`lib_pickle` contains the source code of the `pickle` module, and `pickle.py` is the main file of the module.

In this `pickle` library, the original C implementation call (original lines 1776–1790):

```python
try:
    from _pickle import (
        PickleError,
        PicklingError,
        UnpicklingError,
        Pickler,
        Unpickler,
        dump,
        dumps,
        load,
        loads
    )
except ImportError:
    Pickler, Unpickler = _Pickler, _Unpickler
    dump, dumps, load, loads = _dump, _dumps, _load, _loads
```

is replaced with the current implementation (lines 1107–1108):

```python
Pickler = _Pickler
dump, dumps = _dump, _dumps
```

The project only tests the `dump` and `dumps` functions of the serialization module, so the `load` and `loads` functions
have been removed from the `pickle` source file.

## Project Structure

```
├── BTH-014
│   ├── black_test
│   │   ├── Base_test_class.py # Base test class with encapsulated test units
│   │   ├── test_basic_types.py # Basic type serialization
│   │   ├── test_container.py # Container type serialization
│   │   ├── test_customer_class.py # Custom class serialization
│   │   ├── test_function.py # Function serialization
│   │   ├── test_moudle.py # Common module serialization (e.g., datetime)
│   │   ├── test_nested.py # Nested structure serialization
│   │   ├── test_reference.py # Circular reference serialization
│   ├── boundary_value_test
│   │   ├── test_in_point.py # Inner boundary testing
│   │   ├── test_off_point.py # Off-boundary testing
│   │   ├── test_on_point.py # On-boundary testing
│   │   ├── test_out_point.py # Outer boundary testing
│   ├── diff_test
│   │   ├── test_diff.py # Cross-OS/Python version comparisons
│   ├── fuzzing
│   │   ├── generate_data.py # Fuzzing test data generation
│   │   ├── generate_seed.py # Fuzzing test seed generation
│   │   ├── test_fuzzing.py # Fuzzing test execution
│   ├── white_test
│   │   ├── test_missing_in_black.py # Coverage for black-box test gaps
│   ├── lib_pickle # Modified pickle library
│   ├── README.md
│   ├── win-compare.bat # Windows comparison script
│   ├── win-main.bat # Windows main test script
│   ├── linux-mac-main.sh # Linux/macOS main test script
```
## Usage Instructions

### Prerequisites
1. Install conda environment manager
2. Create three conda environments:
   - `py36` (Python 3.6)
   - `py39` (Python 3.9)
   - `py311` (Python 3.11)

### Execution
**Windows**:
```powershell
win-main.bat
Linux/macOS:
```bash
chmod +x linux-mac-main.sh
./linux-mac-main.sh
```

### Output
|Directory Name | Content |
|---|---|
|res|Serialized results|
|test_result|Test reports|
### Comparison Testing
This project only provides a comparison testing script for Windows:
```powershell
win-compare.bat
```

---

# BTH-014（中文版本）

## 介绍

本项目在主流操作系统**Linux**、**macOS**和**Windows**下，使用Python版本**3.6**、**3.9**和**3.11**测试`pickle`模块的序列化功能。

本项目使用**conda环境**来管理和测试不同的Python版本。

`lib_pickle`包含`pickle`模块的源代码，`pickle.py`是该模块的主文件。

在这个`pickle`库中，原始的C实现调用（原始行1776-1790）：

```python
try:
    from _pickle import (
        PickleError,
        PicklingError,
        UnpicklingError,
        Pickler,
        Unpickler,
        dump,
        dumps,
        load,
        loads
    )
except ImportError:
    Pickler, Unpickler = _Pickler, _Unpickler
    dump, dumps, load, loads = _dump, _dumps, _load, _loads
```

替换为现文件(1107-1108)

```python
Pickler = _Pickler
dump, dumps, = _dump, _dumps
```

本项目仅测试序列化模块的`dump`和`dumps`函数，因此已从`pickle`源文件中删除了`load`和`loads`函数。

## 项目结构

```
├── BTH-014
│   ├── black_test
│   │   ├── Base_test_class.py //封装的测试单元基类
│   │   ├── test_basic_types.py //基本类型的序列化
│   │   ├── test_container.py // 容器类型的序列化
│   │   ├── test_customer_class.py //自定义类的序列化
│   │   ├── test_function.py  //函数的序列化
│   │   ├── test_moudle.py  //常见模块的序列化 如datatime
│   │   ├── test_nested.py     //嵌套结构
│   │   ├── test_reference.py  //循环引用结构
│   ├── boundary_value_test //边界测试
│   │   ├── test_in_point.py
│   │   ├── test_off_point.py
│   │   ├── test_on_point.py
│   │   ├── test_out_point.py
│   ├── diff_test
│   │   ├── test_diff.py //比较不同OS、不同py的pickle
│   ├── fuzzing  
│   │   ├── generate_data.py //模糊测试数据生成
│   │   ├── generate_seed.py //模糊测试种子生成
│   │   ├── test_fuzzing.py //模糊测试
│   ├── white_test //白盒测试
│   │   ├── test_missing_in_black.py  //测试黑盒测试中的遗漏行
│   ├── lib_pickle //移植的pickle库
│   ├── README.md
│   ├── win-compare.bat //win下的对比测试脚本
│   ├── win-main.bat //win下的主测试脚本
│   ├── linux-mac-main.sh //linux和mac下的主测试脚本
```

## 使用方法
### 使用前提
1. 安装conda环境管理器
2. 创建三个conda环境：
   - `py36`（Python 3.6）
   - `py39`（Python 3.9）
   - `py311`（Python 3.11）

之后请在win下输入以下命令
```shell
win-main.bat
```
在linux或mac下输入
```shell
chmod +x linux-mac-main.sh
.\linux-mac-main.sh
```

### 输出  
会生成如下结果  

|文件夹名|内容|
|---|---|
|res|储存序列化结果|
|test_result|测试报告|

### 对比测试
本项目只提供win下的对比测试脚本
```shell
win-compare.bat
```
