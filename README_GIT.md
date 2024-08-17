## 常用 git 命令 --mac

#### 查看指定文件夹下所有文件和文件夹的大小

-- `du -sh {.,}* | sort -h`查看包含隐藏文件的
-- `du -sh /path/to/directory/* | sort -h`
-- `du -sh * | sort -h`--

#### 要更好地理解 .git 文件夹中哪些东西占用了空间

`git count-objects -vH`

#### 垃圾回收和优化来尝试压缩你的 Git 仓库并清理无用的对象：

`git gc --prune=now --aggressive`

#### 使用 Git 自带命令查找大文件(.git)

`git rev-list --objects --all | 
git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |`

#### 看 git log; 退出 git log

`git log`
`q`

#### 移除大的文件：

`git filter-branch --force --index-filter "git rm --cached --ignore-unmatch chrome-mac-arm64" --prune-empty --tag-name-filter cat -- --all`

#### 可以使用下面的命令来列出仓库中所有对象（包括文件）的大小，然后按大小排序：

`git rev-list --objects --all |
git cat-file --batch-check='%(objecttype) %(objectsize) %(rest)' |
sort -nk2 | tail -10`

#### 通过 git log 来检索某文件的记录:

`git log --all -- chrome-mac-arm64`

#### 更好的移除工具来移除文件：`git filter-repo`

`pip3 install git-filter-repo`
`brew install git-filter-repo`
`git filter-repo --invert-paths --path-glob 'chrome-mac-arm64/**'`

#### 从远程仓库 clone 到本地仓库，并命名:

`git clone https://github.com/zhaoxue428/python-webSpd.git python-webSpd-new`
`cd python-webSpd-new `

#### 移除某文件:

`git filter-repo --invert-paths --path-glob 'chrome-mac-arm64/**' --force`

#### 本地新创建的仓库，确定远程仓库设置:

`git remote -v`

- 如果没有远程仓库，添加它 :

`git remote add origin https://github.com/zhaoxue428/python-webSpd.git`

- 如果远程仓库地址错误，先删除后重新添加 :

`git remote remove origin `
`git remote add origin https://github.com/zhaoxue428/python-webSpd.git `

#### origin 和 main 的区别:

`git push origin main`
— origin 是远程仓库的名称
— main 是分支名称

#### `fetch` and `pull`区别:

code：
origin https://github.com/username/python-webSpd.git (fetch)
origin https://github.com/username/python-webSpd.git (push)

Q1: 为什么 git remote -v 显示 fetch 而非 pull
A1:Fetch 和 Push 是基本操作，Pull 是复合操作（fetch and merge）

#### 强制推送到 github：

`git push origin main --force`
