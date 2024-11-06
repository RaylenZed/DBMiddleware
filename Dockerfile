# 使用官方Python镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录内容到工作目录
COPY . .

# 安装依赖
RUN pip install -i https://mirrors.cloud.tencent.com/pypi/simple flask mysql-connector-python

# 暴露端口
EXPOSE 5000

# 运行应用
CMD ["python", "db_middleware.py"]
