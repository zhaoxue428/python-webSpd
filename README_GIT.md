## 常用 git 命令 --mac

查看指定文件夹下所有文件和文件夹的大小
-- `du -sh {.,}* | sort -h`查看包含隐藏文件的
-- `du -sh /path/to/directory/* | sort -h`
-- `du -sh * | sort -h`--

要更好地理解 .git 文件夹中哪些东西占用了空间
git count-objects -vH

动垃圾回收和优化来尝试压缩你的 Git 仓库并清理无用的对象：
git gc --prune=now --aggressive

使用 Git 自带命令查找大文件(.git)
`git rev-list --objects --all | 
git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |`

看 git log; 退出 git log
`git log`
`q`
