# docsify使用指南

来源：[docsify 全接触 | ９９３５ (hooray.github.io)](https://hooray.github.io/posts/ed9dc49e/)

docsify官网：[docsify](https://docsify.js.org/#/)

## 什么是 docsify

> docsify 是一个动态生成文档网站的工具。不同于 GitBook、Hexo 的地方是它不会生成将 `.md` 转成 `.html` 文件，所有转换工作都是在运行时进行。

官方的介绍其实就已经打动我了，因为 GitBook 和 Hexo ，一个有了解过，一个现在正在使用，它们的“特点”就是都需要编译，相对来说就会比较费时，而运行时编译就方便了很多，而且整个文档目录也不会被 `.html` 文件“污染”，虽然 SEO 会受到影响，但我不在乎！

## 开始使用

### 安装

官方推荐安装 [docsify-cli](https://www.npmjs.com/package/docsify-cli) 工具，可以方便创建及本地预览文档网站。

```
npm i docsify-cli -g
```

### 初始化

建议在项目的 `./docs` 目录里写文档，可以通过下面的方式初始化项目：

```
docsify init ./docs
```

这里我也可以直接创建一个纯文档项目：

```
docsify init ./
```

### 本地预览

在上一步初始化完毕后，会看到 `Initialization succeeded! Please run docsify serve ./` ，那我们接着执行 `docsify serve ./` 就可以运行起一个支持实时预览的本地网站，通过 [http://localhost:3000](http://localhost:3000/) 可以访问。

```
docsify serve ./
```

## 基本操作

[![img](https://i.loli.net/2018/08/08/5b6a82e9cf935.png)](https://i.loli.net/2018/08/08/5b6a82e9cf935.png)

运行好后看到这样的页面就代表运行成功了，在开始写文档之前，先来了解一下初始化好后的这三个文件分别是做什么的。

- `.nojekyll` 用于阻止 GitHub Pages 会忽略掉下划线开头的文件
- `index.html` 入口文件，也可以理解为项目配置文件
- `README.md` 文档默认主页

### 多页文档

现在文档默认只有一篇，也就是 `README.md` ，如果要再增加一篇，也很简单，直接在项目根目录创建一个 `.md` 文件就可以，比如新建一个 `guide.md` 文件，那么对应的路由就是 `/#/guide` 。

假设我们的文件目录结构如下：

```
docsify
├ README.md
├ guide.md
├ zh-cn
│　├ README.md
│　└ guide.md
```

那么对应访问页面的地址就是：

```
docsify/README.md            ==> http://localhost:3000/#/
docsify/guide.md             ==> http://localhost:3000/#/guide
docsify/zh-cn/README.md      ==> http://localhost:3000/#/zh-cn/
docsify/zh-cn/guide.md       ==> http://localhost:3000/#/zh-cn/guide
```

### 侧边栏

现在项目里已经可以创建多篇文档了，但发现有个问题，因为现在是通过手动在浏览器地址栏里输入文档地址访问，这种方式肯定不够优雅。

好在 docsify 提供了侧边栏的功能，我们打开 `index.html` 文件配置 `loadSidebar` 选项：

```
window.$docsify = {
    loadSidebar: true
}
```

接着在根目录下创建 `_sidebar.md` 文件，内容如下：

```
* [首页](/)
* [指南](guide)
* [中文首页](zh-cn/)
* [中文指南](zh-cn/guide)
```

需要注意的是，`_sidebar.md` 的加载逻辑是从每层目录下获取文件，如果当前目录不存在该文件则回退到上一级目录。例如当前路径为 `/zh-cn/guide` 则从 `/zh-cn/_sidebar.md` 获取文件，如果不存在则从 `/_sidebar.md` 获取。当然你也可以配置 `alias` 避免不必要的回退过程。

```
window.$docsify = {
    loadSidebar: true,
    alias: {
        '/.*/_sidebar.md': '/_sidebar.md'
    }
}
```

### 文档目录

侧边栏开启的同时，通过设置 `subMaxLevel` 选项也可以开启文档目录功能。

```
window.$docsify = {
    loadSidebar: true,
    subMaxLevel: 2
}
```

这会我们打开 `README.md` 文件，随便写几个标题，保存一下看看效果。

```
## 标题1

### 标题1-1

### 标题1-2

## 标题2

## 标题3
```

[![img](https://i.loli.net/2018/08/08/5b6a9ab29079d.png)](https://i.loli.net/2018/08/08/5b6a9ab29079d.png)

可以看到`标题1`下面的`标题1-1`和`标题1-2`并没有显示出来，因为我们设置了 `subMaxLevel` 为 2 ，如果需要显示，则修改为 3 即可。

侧边栏一级为页面，从二级开始才是目录，所以 `subMaxLevel: 2` 只显示了一级目录，如果要显示二级目录，则应该设置为 `subMaxLevel: 3` 。如果还是不理解，那就动手多试几遍，就明白了。

如果文档里有特定的标题不想展示到目录中，可以添加 `{docsify-ignore}` 或 `{docsify-ignore-all}` 。

```
## 标题1

### 标题1-1 {docsify-ignore}

### 标题1-2

## 标题2 {docsify-ignore-all}

### 标题2-1

## 标题3
```

### 导航栏

打开 `index.html` 文件配置 `loadNavbar` 选项：

```
window.$docsify = {
    loadNavbar: true
}
```

接着在根目录下创建 `_navbar.md` 文件，内容如下：

```
* [En](/)
* [中文](/zh-cn/)
```

如果导航内容很多，也可以使用嵌套的方式：

```
* En
  * [Index](/)
  * [Guide](guide)
* 中文
  * [首页](/zh-cn/)
  * [指南](/zh-cn/guide)
```

- 导航嵌套支持多层，但官方的样式处理上似乎有点 bug ，多层嵌套展示不理想，所以建议最多就两层嵌套最好。
- 导航的加载逻辑与侧边栏一致。

### 封面

打开 `index.html` 文件配置 `coverpage` 选项：

```
window.$docsify = {
    coverpage: true
}
```

接着在根目录下创建 `_coverpage.md` 文件，内容就是标准的 markdown 语法，可以参考一下官方的封面：

```
![logo](_media/icon.svg)

# docsify

> A magical documentation site generator.

* Simple and lightweight (~12kb gzipped)
* Multiple themes
* Not build static html files

[GitHub](https://github.com/docsifyjs/docsify/)
[Get Started](#quick-start)
```

封面的背景是随机生成的渐变色，我们也可以指定一个背景色或者背景图，只要放在文档末尾就可以，同时设定只生效第一个。

```
<!-- 自定义背景色 -->
![color](#f0f0f0)

<!-- 自定义背景图 -->
![](background_image.png)
```

如果我们的文档是多语言的，那可不可以设置多个封面？当然也是可以的。首先确定文档目录结构如下：

```
docsify
├ README.md
├ guide.md
├ _coverpage.md
├ zh-cn
│　├ README.md
│　├ guide.md
│　└ _coverpage.md
```

然后修改 `coverpage` 选项：

```
window.$docsify = {
    coverpage: ['/', '/zh-cn/']
}

// 或者具体指明文件名
window.$docsify = {
    coverpage: {
        '/': '_coverpage.md',
        '/zh-cn/': '_coverpage.md'
    }
}
```

## 个性定制

### 配置项

在上面已经介绍了一些配置项，比如侧边栏 `loadSidebar` 、导航栏 `loadNavbar` 、封面 `coverpage` ，关于 `window.$docsify` 完整配置说明，可以查看[官方配置项文档](https://docsify.js.org/#/zh-cn/configuration)参考。

### 主题

直接打开 index.html 修改替换 css 地址即可切换主题，官方目前提供了 4 套主题，分别是：

```
<link rel="stylesheet" href="//unpkg.com/docsify/themes/vue.css">
<link rel="stylesheet" href="//unpkg.com/docsify/themes/buble.css">
<link rel="stylesheet" href="//unpkg.com/docsify/themes/dark.css">
<link rel="stylesheet" href="//unpkg.com/docsify/themes/pure.css">

<!-- 压缩文件位于 /lib/themes/ -->
<link rel="stylesheet" href="//unpkg.com/docsify/lib/themes/vue.css">
<link rel="stylesheet" href="//unpkg.com/docsify/lib/themes/buble.css">
<link rel="stylesheet" href="//unpkg.com/docsify/lib/themes/dark.css">
<link rel="stylesheet" href="//unpkg.com/docsify/lib/themes/pure.css">
```

### 插件

插件配置很简单，基本大部分插件只要复制对应的 js 引用代码复制到 index.html 页面里就可以。以下介绍几个我在测试中用到感觉还不错的插件，更[完整的插件列表](https://docsify.js.org/#/zh-cn/plugins)还请查看官方文档。

#### emoji

docsify 默认是支持 emoji 表情的，但它不够精准，因为没有处理非 emoji 的字符串。如果你需要正确解析 emoji 字符串，可以引入这个插件。

```
<script src="//unpkg.com/docsify/lib/plugins/emoji.js"></script>
```

这里我还找到一份 github 的完整 emoji 表情代码：[去看看](https://gist.github.com/rxaviers/7360908)

#### 复制代码

在用 markdown 展示代码片段的时候，可能需要一键复制代码到本地运行，这时候就可以引入这个插件。

```
<script src="//unpkg.com/docsify-copy-code"></script>
```

#### 分页

在文档底部出现上一页和下一页按钮。

```
<script src="//unpkg.com/docsify-pagination/dist/docsify-pagination.min.js"></script>
```

#### 代码高亮

docsify 内置的代码高亮工具是 Prism ，默认支持 CSS 、JavaScript 和 HTML 。如果需要其它语言，可以手动引入。

```
<!-- 引入 PHP 代码高亮插件 -->
<script src="//unpkg.com/prismjs/components/prism-php.js"></script>
```

其它语言高亮插件可以查看 [Prims](https://github.com/PrismJS/prism/tree/gh-pages/components) 仓库。

## 文档助手

docsify 扩展了一些 markdown 的语法，但由于这篇文章是在 Hexo 里编写，无法通过 Hexo 直接展示出效果，建议查看[官方文档](https://docsify.js.org/#/zh-cn/helpers)了解详情。

## 最后

最后把整个项目上传到 GitHub Pages 上，一份在线文档就大功告成了。

整体使用下来还是挺顺畅的，基本和原来写文档的流程一样，如果不会用到 docsify 提供的 markdown 扩展语法，那就可以继续使用原有的 markdown 编辑器进行编写，加上现在大部分 markdown 编辑器都会提供同步预览，所以也不一定非得使用 docsify 提供的本地预览方案。

关于离线模式（PWA）和服务端渲染（SSR），因为目前用不上，所以就没有尝试。