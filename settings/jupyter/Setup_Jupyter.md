# Setup - Anaconda (Jupyter)

[TOC]

---

## Anconda

### Step 1: Use wget to install

* Anaconda Installer archive URL
    * https://repo.anaconda.com/archive/

```bash
# wget https://repo.anaconda.com/archive/{filename}
$ wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
```



### Step 2: Check 

```bash
$ conda --version
```

#### Errors
* <font color=red>conda: command not found</font>
```bash
$ echo $PATH
# /home/zx/anaconda3/bin:/home/zx/anaconda3/condabin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/zx/.local/bin:/home/zx/bin

$ export PATH=$PATH:/home/zx/anaconda3/bin
# {/home/zx/anaconda3/} is your anaconda3 folder absolute path
```



### Step 3: Set up server jupyter

#### I. Generate config file

* Path: `'~/.jupyter/jupyter_notebook_config.py'`

```bash
$ jupyter nothbook --generate-config
```

#### II. Generate Password

```bash
$ ipython
```

```python
from notebook.auth import passwd

passwd()
# Enter password: {your_password}
# Verify password: {your_password}

# Output: 'sha1:xxxxxxxxxxxxx' something like this, copy and save it
```

#### III. Update the config file

```bash
$ vi ~/.jupyter/jupyter_notebook_config.py
```

```bash
c.NotebookApp.allow_remote_access = True

c.NotebookApp.ip = '*' # Set the access IP, * means allowing all IP to access
c.NotebookApp.notebook_dir = '/home/xx/xxx' # absolute path
c.NotebookApp.password = u'sha1:xxxxxxxxxxxxx' 
c.NotebookApp.open_browser = False
c.NotebookApp.port = 9527 # {port}
```

* **You need whitelist the port num on your server, you can login the server admin and update the fire wall**

![whitelist the port](https://tva1.sinaimg.cn/large/007S8ZIlgy1giwdbnpzi4j30g10dmaax.jpg)



#### IV. Start jupyter notebook

* The Server Address: xxx.xxx.xx.xxx

```bash
# On your server
# can use tmux
$ jupyter notebook
```

* **Open a browser and enter `http://{your_server_IP}:{port_num}`**

![Jupyter Login](https://tva1.sinaimg.cn/large/007S8ZIlgy1giwd1o938pj30y00r27bl.jpg)

* Enter the password and login, then can use jupyter on your server

![Jupyter](https://tva1.sinaimg.cn/large/007S8ZIlgy1giwd5fy4e6j31aa0e6taf.jpg)

### Step 4. Install extensions

```bash
$ pip install jupyter_contrib_nbextensions

$ jupyter contrib nbextension install --user
```

![Jupyter Extensions](https://tva1.sinaimg.cn/large/007S8ZIlgy1giwep94wq5j30xb0h0adh.jpg)

