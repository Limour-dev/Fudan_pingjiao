1. 安装python3

2. 命令行下`pip3 install selenium`安装selenium

3. 在clone或者下载本项目获得work.py（python脚本）

4. 下载对应浏览器的webdriver

   以下是chrome的浏览器webdriver下载地址，选择和自己chrome对应版本的chromedriver（可以再chrome浏览器网址栏中输入`chrome://version`查看，下载好了把里面的东西解压出来：

   * mac系统： 放在和work.py同一文件夹下
   * linux系统：在终端中进入解压出来的东西所在文件夹下，执行命令`sudo mv chromedriver /usr/local/chromedriver`
   * win系统：https://www.jianshu.com/p/28c0d1ed62f8

   [Chrome web driver](http://chromedriver.storage.googleapis.com/index.html)

5. 用文本编辑器打开work.py文件（如果是windows就右键-打开方式-记事本），找到下面两行代码

   ```c++
   username = ''
   password = ''
   ```

   引号内分别填入uis用户名和密码

6. 命令行中`python3 work.py`运行python脚本

7. 不同环境可能会不兼容，我的环境是mac，在linux也测试过，目前都只支持chrome浏览器。如果遇到问题可以发邮件到`llsun18@fudan.edu.cn`

8. 祝大家评教愉快