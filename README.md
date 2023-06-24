# 项目启动指南

## 1. 后端启动

### 1.1 安装依赖包
在终端中，进入项目根目录，并安装Python依赖：

```bash
cd management_system
pip install -r requirements.txt
1.2 启动项目
使用以下命令启动后端服务：

```bash
Copy code
python manage.py runserver

## 2. 前端启动
### 2.1 安装依赖包
在终端中，进入前端项目目录，并安装npm依赖：

```bash
Copy code
cd management_system_vue
npm install # 安装依赖包
nvm install 18.16.0 # 本项目使用18.16.0版本的node

### 2.2 启动项目

使用以下命令启动前端服务：

```bash
Copy code
npm run serve