# Git Tutorial

[TOC]

## What is Git?

**CVCS (Centralized Version Control Systems)**

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gh4wlfs9z7j30m80fgaae.jpg" alt="Centralized Version Control Systems" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gh4wmh7o36j30m808mq33.jpg" alt="delta-based" style="zoom:70%;" />



**DVCS (Distributed Version Control System)**

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gh4wg0jog9j30ik0m80t6.jpg" alt="Distributed Version Control System" style="zoom:67%;"/>

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gh4wnnf57fj30m808h74k.jpg" alt="snapshots" style="zoom:70%;" />

**Modified --> Staged --> Committed**

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gh4wr4dqv0j30m80c90sy.jpg" alt="modified-staged-committed" style="zoom:60%;" />



**Refer Links:**

1. [git Documentation](https://git-scm.com/book/en/v2)
2. [github website](https://github.com/)

## Install Git (The Command Line)

```bash
$ brew install git

# Check Git Version
$ git --version
```



## Command

### Common Command

```bash
# Clone A Repository to Local
git clone {repository URL} # Clone with SSH

git pull origin master

git pull

git status

git commit -m "{update message}"

git push # Update with SSH, need password
```



<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gh4w67gtn2j30m806bwex.jpg" alt="git fetch and pull" style="zoom:80%;"/>



