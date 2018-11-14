# PaChong-note
笔记整理

Take-notes-01 

笔记整理 git clone

修改后进行更新，需要向下拉去：git pull


提交当前的修改 git add .

git commit –m “对于修改的注释，之后查看历史方便”

git push origin default:default

(git push origin modifyurl:modifyurl)

echo "# PaChong-note" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/Smpidus-TDT/PaChong-note.git
git push -u origin master

…or push an existing repository from the command line
git remote add origin https://github.com/Smpidus-TDT/PaChong-note.git
git push -u origin master
------------------------------------------------------------------
The local repository is out of date.Make sure all changes have been pulled from the remote repository and try again.

字面意思很好理解, "确保所有东西都从远程拉下来" .
是因为你再github新建的项目中有文件在本地没有造成的，需要将它pull到终端，先cd到你项目目录
git pull命令的作用是，取回远程主机某个分支的更新，再与本地的指定分支合并
------------------------------------------------------------------
