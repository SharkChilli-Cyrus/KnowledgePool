# SSH

[TOC]

## Generate SSH Public Key & Private Key

```bash
$ ssh-keygen -t [rsa|dsa] -C "your_comment_here"

# Generating public/private rsa key pair.
# Enter file in which to save the key (/Users/xu.zhu/.ssh/id_rsa): /Users/xu.zhu/.ssh/{filename_rsa}
# Enter passphrase (empty for no passphrase): 
# Enter same passphrase again: 

# Your identification has been saved in /Users/xu.zhu/.ssh/{filename}_rsa.
# Your public key has been saved in /Users/xu.zhu/.ssh/{filename}_rsa.pub.
```

You can find your **private & public keys** in this path: **(default)** `/Users/xx/.ssh/` 

* Private key: `{filename}_rsa`
* Public Key: `{filename}_rsa.pub`

In you default ssh path `/Users/xx/.ssh/` there is a **config file** `config`

![截屏2020-09-19 下午3.49.21](https://tva1.sinaimg.cn/large/007S8ZIlgy1giw0de706vj30wu0bwq7h.jpg)

## Example: Alibaba Cloud

### Set Root User SSH Keys

* IP address: <font color=blue>100.100.10.100</font>
* User: <font color=blue>root</font>





