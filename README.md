# BTH-014

## Introduce

本项目测试Linux、mac与win主流操作系统下的Python3.8、3.9、3.10、3.11、3.12版本的pickle模块的序列化功能。  
本项目使用conda环境进行不同版本下的管理测试。  
项目仅仅测试序列化模块的dump与dumps功能，故将源文件的load与loads功能删除。

## Project Structure

```
├── BTH-014
│   ├── Black_test
│   │   ├── test_basic_types.py //基本类型的序列化
│   │   ├── test_container.py // 容器类型的序列化
│   │   ├── test_customer_class.py //自定义类的序列化
│   │   ├── test_lambda.py  //lambda表达式的序列化
│   │   ├── test_moudle.py  //常见模块的序列化 如datatime
│   │   ├── test_nested.py     //嵌套结构
│   │   ├── test_reference.py  //循环引用结构
│   ├── White_test
│   ├── fuzz    
│   ├── main  
│   ├── README.md
│   ├── main-win.bat //win下的测试脚本
│   ├── main-linux.sh //linux与mac下的测试脚本
```

