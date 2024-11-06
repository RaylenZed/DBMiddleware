# DBMiddleware

DBMiddleware 是一个轻量级的数据库中间件，用于简化数据库操作。它作为应用程序与数据库之间的桥梁，提供数据库管理、请求处理和配置设置的功能。

## 特性

- **无缝数据库连接**：提供简洁的连接接口。
- **可配置的设置**：通过 JSON 配置文件自定义。
- **Docker 支持**：使用提供的配置文件轻松通过 Docker 部署。

## 先决条件

- [Docker](https://www.docker.com/get-started)
- [Python](https://www.python.org/) 3.x

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/yourusername/DBMiddleware.git
cd DBMiddleware
```


### 2. 配置

在项目目录下找到 config.json.example 配置文件，将其复制为 config.json，并根据需要修改内容：
```json
{
    "databases": {
        "db1": {
             "host": "your_mysql_host1",
            "user": "your_mysql_user1",
            "password": "your_mysql_password1",
            "database": "your_mysql_database1",
            "api_keys": ["api_key_1", "api_key_2"]
        },
        "db2": {
            "host": "your_mysql_host2",
            "user": "your_mysql_user2",
            "password": "your_mysql_password2",
            "database": "your_mysql_database2",
            "api_keys": ["api_key_3", "api_key_4"]
        }
    }
}
```

### 3. Docker部署
项目包含了 Dockerfile 和 docker-compose.yml 文件，方便通过 Docker 部署。

1.	构建并运行 Docker 容器：

  ```bash
  docker-compose up -d
  ```

2. docker-compose up -d


###  4. 使用方法
容器启动后，DBMiddleware 将根据 db_middleware.py 文件中的逻辑处理请求。可参考该脚本，了解具体的端点、数据库操作和请求结构。

## 项目结构

- **db_middleware.py**：核心脚本，用于数据库操作和中间件逻辑。
- **config.json.example**：配置文件示例。
