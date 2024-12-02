# 方法一：使用 Nix 环境运行（推荐）

> [!TIP]
> 由于不同用户的环境差别很大，我没办法一一进行测试。这种情况下，最好的方法就是用 Nix，因为它可以确保这个评教脚本无论在什么环境下都可用（包括 WSLg）。

1. 克隆本仓库
2. 用文本编辑器打开work.py文件，找到下面两行代码

   ```c++
   username = ''
   password = ''
   ```

   引号内分别填入uis用户名和密码
3. 在 shell 中执行 `nix-shell`
4. 执行 `python3 work.py`

# 方法二：手动配置

1. 安装python3

2. 命令行下`pip3 install -r requirements.txt`安装selenium

3. 在clone或者下载本项目获得work.py（python脚本）

4. 下载对应浏览器以及webdriver

   ```bash
   sudo apt install chromium-chromedriver
   ```

5. 用文本编辑器打开work.py文件，找到下面两行代码

   ```c++
   username = ''
   password = ''
   ```

   引号内分别填入uis用户名和密码

6. 执行 `python3 work.py`

7. 命令行中`python3 work.py`运行python脚本

8. 不同环境可能会不兼容，我的环境是 Ubuntu 23.10 。如果遇到问题可以尝试方法一

9. 祝大家评教愉快
