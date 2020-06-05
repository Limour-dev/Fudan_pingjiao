1. 安装python3

2. 命令行下`pip3 install selenium`安装selenium

3. 下载对应浏览器的webdriver

   以下是常用的浏览器web driver下载地址，下载好了解压出来放在和work.py同一文件夹下

   [Firefox web driver](https://github.com/mozilla/geckodriver/releases)
   [Chrome web driver](http://chromedriver.storage.googleapis.com/index.html?path=2.0/)

4. 将work.py中

   ```c++
   usr.send_keys('')
   pwd.send_keys('')
   ```

   引号内分别填入uis用户名和密码

5. 命令行中`python3 work.py`运行python脚本

6. 不同环境可能会不兼容，我的环境是mac+chrome。如果遇到问题可以发邮件到`llsun18@fudan.edu.cn`

7. 祝大家评教愉快