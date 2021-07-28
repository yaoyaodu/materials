# Git命令整理

1. 安装好git后，在命令行或终端中使用下面的命令可以设置git自己的名字和电子邮件。这是因为Git是分布式版本控制系统，所以，每个机器都必须自报家门：你的名字和Email地址。（要加引号）

   git config --global user.name "bryan sun"
   git config --global user.email "hitsjt@gmail.com"

   注意：

   `git config`命令的`--global`参数，用了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置，当然也可以对某个仓库指定不同的用户名和Email地址。

   配置好之后可以使用以下命令查看配置。

   git config -l

2. 创建一个版本库：选择一个文件夹，右键选择**Git Bash Here**。不选中文件夹则默认创建在User下面。

   mkdir learngit

   cd learngit
   pwd                                        //Print Working Directory 显示当前目录的路径

   （pwd命令: 其功能是显示当前所在工作目录的全路径。

   主要用在当不确定当前所在位置时，通过pwd来查看当前目录的绝对路径。）

3. 通过`git init`命令把这个目录变成Git可以管理的仓库。

4. 创建SSH Key

   打开Git Bash，执行如下命令，一路回车即可。

   ssh-keygen -t rsa -C "youremail@example.com"

   执行命令后，我们再进入到"`~/.ssh`"目录下，运行"`ls`"命令，可以看到里面有`id_rsa`和`id_rsa.pub`两个文件，这两个就是SSH Key的秘钥对，`id_rsa`是私钥，不能泄露出去，`id_rsa.pub`是公钥，可以放心地告诉任何人。

6. 关联已有仓库
   git remote add origin git@github.com:guoyaohua/learngit.git
   git push -u origin master

7. clone账号中的项目至本地:       

   git clone git@192.168.100.62:<user name>/sw.git 
   cd sw
   添加远端主仓以便于同步主仓中其他人的修改     

   git remote add upstream git@192.168.100.62:doc/sw.git 
   git fetch upstream 

   git merge upstream/master  (与主仓同步) 合并指定分支到当前分支

8. 

9. cd sw

10. git add -A

11. git commit -m “update XXX”

12. git push origin master

13. 无法进行快进式合并，需先在本地进行变基rebase。使用以下命令进行更新并再次推送：

    git fetch upstream 

    git rebase upstream/master 

    git push origin master

14. rebase后push还是报error

    git log

    <img src="https://i.loli.net/2021/07/27/K9MwQ4ACtkO5YRc.png" alt="rebase后报error" style="zoom: 50%;" />

15. 可能你需要用merge  用下面这三条命令再试试
    git fetch upstream
    git merge upstream/master
    git push origin master
    
    第二条命令可能造成冲突
    执行完第二条命令以后，执行一个  git status 发一下结果

16. 执行git pull 然后git push origin master

    <img src="https://i.loli.net/2021/07/27/xPnl16VN8JMRTwB.png" alt="pull后出现一个不知名的页面关掉执行git push origin master" style="zoom:50%;" />

17. 图片链接：

    1. 给图片加 id 属性，注意id必须为英文
    2. 链接指向此id：

    ![图片id](https://i.loli.net/2021/07/27/KeGHD3lryV4dQcL.png)

    ![图片链接](https://i.loli.net/2021/07/27/vAEUB4S3y5u12mX.png)

18. git status

19. 用`git remote -v`查看远程库的详细信息：

    origin  git@github.com:yaoyaodu/materials.git (fetch)
    origin  git@github.com:yaoyaodu/materials.git (push)



