# Git基础笔记

这里记录我目前实际使用过的Git指令和遇到的问题。以后遇到新的情况再继续补充，不一次记录所有Git知识。

## commit中的常用前缀

commit信息一般写成：

```text
类型: 本次修改的内容
```

| 前缀 | 含义 |
| --- | --- |
| `feat` | 增加新功能 |
| `fix` | 修复错误 |
| `docs` | 修改文档、README或笔记 |
| `refactor` | 重构代码，但基本不改变功能 |
| `test` | 增加或修改测试 |
| `style` | 修改格式，不改变代码逻辑 |
| `chore` | 仓库维护、配置或忽略规则等 |
| `perf` | 提升运行性能 |
| `build` | 修改构建工具或依赖 |
| `ci` | 修改GitHub Actions等自动化流程 |
| `revert` | 撤销某次提交 |

我目前最常用的是 `docs`、`refactor` 和 `chore`。

## Git的基本流程

```text
工作区
  ↓ git add
暂存区
  ↓ git commit
本地仓库
  ↓ git push
GitHub远程仓库
```

`git add`以后如果又修改了同一个文件，新的修改不会自动进入暂存区，需要再次执行`git add`。

## 目前使用过的指令

| 指令 | 我的理解 |
| --- | --- |
| `git init -b main` | 在当前目录创建Git仓库，并把初始分支命名为main |
| `git status` | 查看当前分支、工作区和暂存区的状态 |
| `git status --short` | 用简短格式显示发生变化的文件 |
| `git diff` | 查看还没有进入暂存区的具体修改 |
| `git add -- "文件路径"` | 把指定文件当前的修改放进暂存区 |
| `git diff --cached` | 查看下一次commit准备提交的内容 |
| `git commit -m "说明"` | 把暂存区内容保存为一次本地提交 |
| `git push` | 把本地提交上传到GitHub |
| `git log --oneline` | 简要查看提交历史 |
| `git show HEAD` | 查看最近一次提交的具体内容 |
| `git remote -v` | 查看本地仓库连接的远程地址 |
| `git mv "旧路径" "新路径"` | 重命名已经被Git跟踪的文件 |
| `git rm -- "文件路径"` | 删除已被Git跟踪的文件，并把删除操作放进暂存区 |

## `git status --short`中的状态

`git status --short`每行开头有两列状态。第一列主要表示暂存区，第二列主要表示工作区。

| 状态 | 含义 |
| --- | --- |
| `??` | 新文件，Git还没有跟踪 |
| `A ` | 新文件已经进入暂存区 |
| `M ` | 文件修改已经进入暂存区 |
| ` M` | 文件在工作区被修改，但还没有暂存 |
| `D ` | 文件删除已经进入暂存区 |
| `R ` | 文件重命名已经进入暂存区 |
| `RM` | 重命名已经暂存，但重命名后的文件又被修改了 |

## 我遇到过的问题

### `git status -short`报错

`short`是完整选项，需要使用两个短横线：

```powershell
git status --short
```

### `pathspec did not match any files`

通常是文件名或相对路径写错了。执行`git add`时，路径要从当前所在目录开始计算。

### `bad source`

源文件已经不存在。例如文件已经完成重命名，再次使用原文件名执行`git mv`就会报错。

### `nothing added to commit`

说明修改还没有进入暂存区。需要先检查文件，再执行`git add`。

### `ahead of 'origin/main' by 1 commit`

表示本地已经有一次新提交，但这次提交还没有通过`git push`上传到GitHub。

### `LF will be replaced by CRLF`

这是Windows和其他系统使用不同换行格式产生的提示，一般不是提交失败。

## 我目前的理解

Git不会自动把所有修改上传到GitHub。每次应该先用`git status`查看状态，用`git add`选择要提交的文件，再用`git diff --cached`检查，之后执行`git commit`保存到本地，最后使用`git push`上传。

Git不会跟踪空文件夹，只会跟踪文件。删除已经提交的文件时，也会产生一次新的删除记录，旧提交中的文件仍然可以找到。
