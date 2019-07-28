# pydemo
---
## 背景

Python越来越流行，因此对于自己要求加快提升python编程技巧。最好的方法还是不练习python编程技巧，于是把自己平时练习的python
例子都记录到github上，以便自己日后可以经常温故而知新。

## 搭建

* 安装python virtual environment
* 安装python依赖包(pip install -r requirements.txt)
* 安装MySQL_python-1.2.5(pip install whl\MySQL_python-1.2.5-cp27-none-win_amd64.whl)(Windows)

## 目录

```bash

-pydemo
|
|-common                                                 公共目录，用于存放脚本，安装依赖文件，配置文件等
|   |
|   |-sql                                                SQL脚本文件存放目录
|   |  |
|   |  |-create_user.sql                                 test用户创建脚本文件
|   |  |
|   |  |-person.sql                                      person表创建脚本文件
|   |
|   |-whl                                                wheel文件存放目录
|      |
|      |-MySQL_python-1.2.5-cp27-none-win_amd64.whl      MySQL_python wheel文件
|
|-src                                                    python源文件存放目录
|  |
|  |-demo_sqlalchemy.py                                  sqlalchemy库demo文件
|
|-README.md                                              项目说明文件
|
|-requirements.txt                                       python依赖说明文件


```
