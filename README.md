1. 安装python3

2. 命令行下`pip3 install selenium`安装selenium

3. 下载对应浏览器的webdriver

   以下是chrome的浏览器web driver下载地址，选择和自己chrome对应版本的chromedriver（可以再chrome浏览器网址栏中输入`chrome://version`查看，下载好了把里面的东西解压出来：

   * mac系统： 放在和work.py同一文件夹下
   * linux系统：在终端中进入解压出来的东西所在文件夹下，执行命令`sudo mv chromedriver /usr/local/chromedriver`
   * win系统：https://www.jianshu.com/p/28c0d1ed62f8

   [Chrome web driver](http://chromedriver.storage.googleapis.com/index.html)

4. 将work.py中

   ```c++
   usr.send_keys('')
   pwd.send_keys('')
   ```

   引号内分别填入uis用户名和密码

5. 命令行中`python3 work.py`运行python脚本

6. 不同环境可能会不兼容，我的环境是mac+chrome。如果遇到问题可以发邮件到`llsun18@fudan.edu.cn`

7. 祝大家评教愉快