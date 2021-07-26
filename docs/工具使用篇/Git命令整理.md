# Git命令整理

1. 安装好git后，在命令行或终端中使用下面的命令可以设置git自己的名字和电子邮件。这是因为Git是分布式版本控制系统，所以，每个机器都必须自报家门：你的名字和Email地址。（要加引号）

   git config --global user.name "bryan sun"
   git config --global user.email "hitsjt@gmail.com"

   注意：

   `git config`命令的`--global`参数，用了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置，当然也可以对某个仓库指定不同的用户名和Email地址。

2. 配置好之后可以使用以下命令查看配置。

   git config -l

3. 创建一个版本库：选择一个文件夹，右键选择**Git Bash Here**。不选中文件夹则默认创建在User下面。

   mkdir learngit

   cd learngit
   pwd

4. pwd命令

   pwd是Print Working Directory的缩写，其功能是显示当前所在工作目录的全路径。主要用在当不确定当前所在位置时，通过pwd来查看当前目录的绝对路径。

5. 创建SSH Key

   打开Git Bash，执行如下命令，一路回车即可。

   ssh-keygen -t rsa -C "youremail@example.com"

   执行命令后，我们再进入到"`~/.ssh`"目录下，运行"`ls`"命令，可以看到里面有`id_rsa`和`id_rsa.pub`两个文件，这两个就是SSH Key的秘钥对，`id_rsa`是私钥，不能泄露出去，`id_rsa.pub`是公钥，可以放心地告诉任何人。

   

