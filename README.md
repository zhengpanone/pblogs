https://mblogs.readthedocs.io/en/latest/

```shell
# 项目初始化
uv init pblogs && cd pblogs
# uv 安装依赖
uv add requests
```

```shell
cd blogs
# 可以指定Python版本来创建虚拟环境
pipenv --python 3.10.4

# 由于项目是新建的，所以会自动生成Pipfile和Pipfile.lock文件
pipenv install

# 激活虚拟环境
pipenv shell

# 退出虚拟环境
exit

# 删除虚拟环境。删除虚拟环境不会删除项目目录，只是删除虚拟环境的目录
pipenv --rm

make clean latexpdf
```

