# Git中.gitignore文件的用法

来源：[Git - .gitignore文件的用法 - 雨临Lewis - 博客园 (cnblogs.com)](https://www.cnblogs.com/yulinlewis/p/10231035.html)

## `.gitignore`文件的作用

`.gitignore`文件用来忽略被指定的文件或文件夹的改动，被记录在`.gitignore`文件里的文件或文件夹，是无法被git跟踪到的，换句话说，被忽略的文件是不会被放入到远程仓库里的。

也就是说，如果文件已经存在于远程仓库中，是无法通过`.gitignore`文件来忽略的。

`.gitignore`文件存放于git仓库的根目录下。

## `.gitignore`文件的语法

### 注释

`#`表示注释，如下：

```text
# Here is comment.
```

### 忽略文件/文件夹

直接写入文件或文件夹名即可，指定文件夹里的所有文件也会一起被忽略，如下：

```text
# ignore target folder
target/

# ignore Eclipse files
.settings/
build/
.classpath
.project
```

### 不忽略文件/文件夹

`!`表示不忽略指定的文件，如下：

```text
# don't ignore src folder
!src/
```

### 在指定文件夹里不忽略指定的文件

通过`!`可以实现更加有意思的用法，如下：

```text
# ignore scaffolds folder, but don't ignore draft.md under scaffolds folder.
scaffolds/*
!scaffolds/draft.md
```

**注意：这里必须在文件夹后面加上`/*`，否则是无法实现想要的效果的。**

### 使用通配符及其他符号

可以使用通配符及其他符号来指定复杂条件的文件，如下：

```text
*.log
day_1?.txt
hello[0-9].txt
```

- `*`表示匹配任意字符；

- `?`表示匹配一个字符；

- []表示匹配中括号内的单个字符：
  - 可以使用`-`来表示连贯的字符，比如`0-9`，`a-z`，`A-Z`等，`[0-9]`表示匹配从0到9的单个字符。
  - 可以使用`^`来表示除外，比如`[^0-9]`表示除0到9之外的单个字符。

## 参考链接

- [.gitignore 规则写法 - 在已忽略文件夹中不忽略指定文件、文件夹【注意项】](https://my.oschina.net/longyuan/blog/521098)