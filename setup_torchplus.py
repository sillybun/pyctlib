'''
@File       :   setup.py
@Author     :   Yuncheng Zhou & Yiteng Zhang
@Time       :   2020-10
@Version    :   1.0
@Contact    :   2247501256@qq.com
@Dect       :   None
'''
 
from setuptools import setup, find_packages
 
setup(
    name = "pyctlib",
    version = "0.1.0",
    keywords = ("pip", "pyctlib", "overload"),
    description = "This package is based on pytorch and try to provide a more user-friendly interface for pytorch",
    long_description = "We encapsulated a new type on top of torch.Tenser, which we also call it Tensor. It has the same function as torch.Tensor, but it can change to cuda device automatically. Also, we try to provide more useful module for torch users to make deep learning earier to be implemented.",
    license = "MIT Licence",
 
    url = "https://github.com/jiangfubang/balabala",       # 项目相关文件地址，一般是github，有没有都行吧
    author = "Zhang Yiteng & Zhou Yuncheng",
    author_email = "zytfdu@icloud.com",
 
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["numpy", "pyctlib", "torch"]        # 该模块需要的第三方库
)
