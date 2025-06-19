# 使用官方 Python 镜像作为基础镜像
FROM swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/python:3.11-slim

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple && mkdir -p /app/songYu/

# 复制应用代码
COPY ./ /app/songYu/

# 设置工作目录
WORKDIR /app/songYu

# 暴露 FastAPI 默认端口
EXPOSE 8000

# 启动命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]