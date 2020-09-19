# Server Setup

[TOC]

---

## Add User

### 添加非root用户

```bash
$ useradd {username}
```

### 设置普通用户sudo密码

```bash
$ passwd {username} # set sudo password for this user
```

### 修改sudo文件，为普通用户添加权限

```bash
$ visudo

# Find this line and
root	ALL=(ALL)	ALL
{username}	ALL=(ALL)	ALL # add this command
```

![visudo](https://tva1.sinaimg.cn/large/007S8ZIlgy1giwdliazj5j30va05wk0d.jpg)

### 切换用户

```bash
$ su {username}

# use sudo
$ sudo {your_command}
```







## Tmux







## Tree

### Step1: Download Tree Package

* Tree URL
    *  http://mama.indstate.edu/users/ice/tree/src/

```bash
$ wget  http://mama.indstate.edu/users/ice/tree/src/tree-1.8.0.tgz
```

```bash
$ tar -zxvf tree-1.8.0.tgz
$ cd tree-1.8.0
$ sudo make install
```




## Warnings
* <font color=orange>Warning: -bash warning: setlocale: LC_CTYPE: cannot change locale (UTF-8): No such file or directory</font>
```bash
$ vi /etc/environment

# add these two lines
LANG=en_US.utf-8
LC_ALL=en_US.utf-8
```