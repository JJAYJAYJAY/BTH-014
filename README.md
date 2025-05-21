# BTH-014（English Version）

## introduction

This project tests the serialization functionality of the `pickle` module under mainstream operating systems including *
*Linux**, **macOS**, and **Windows**, using Python versions **3.6**, **3.9**, and **3.11**.

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
│   │   ├── test_basic_types.py //基本类型的序列化
│   │   ├── test_container.py // 容器类型的序列化
│   │   ├── test_customer_class.py //自定义类的序列化
│   │   ├── test_function.py  //函数的序列化
│   │   ├── test_moudle.py  //常见模块的序列化 如datatime
│   │   ├── test_nested.py     //嵌套结构
│   │   ├── test_reference.py  //循环引用结构
│   ├── diff_op
│   │   ├── compare.py //比较不同OS的pickle
│   │   ├── win-main.sh //程序入口，生成在win下的序列化结果
│   │   ├── mac-main.sh //程序入口，生成在mac和linux下的序列化结果
│   ├── diff_py    
│   │   ├── compare.py //比较不同py版本的pickle
│   │   ├── win-main.sh //程序入口，生成在不同py版本下的序列化结果
│   ├── fuzzing  
│   │   ├── generate_data.py //模糊测试数据生成
│   │   ├── generate_seed.py //模糊测试种子生成
│   │   ├── test_fuzzing.py //模糊测试
│   ├── lib_pickle
│   ├── tool
│   ├── README.md
```

## 使用方法


