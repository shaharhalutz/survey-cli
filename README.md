# Survey - CLI


### Requirements

* Python 2.7+ or 3.0+   (https://www.python.org)
* Pip   (https://pip.pypa.io/en/stable/installing/)

> If you're having any troubles with installation, this guide may help you: https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation

### Install

```
pip install -r requirements.txt
```

### Config 

> see config.example.json

> Note: for convenience save your config files under 'config/' directory. 

> To add your credentials, replace the values for `MY_AWS_ACCESS_KEY_ID` and `MY_AWS_SECRET_ACCESS_KEY` in your config file.


### Run 

- To Push Notifications to all Users:

```
python survey-cli.py --push  ./config/config.json
```

- Help:
```
python ./survey-cli.py -h 
```