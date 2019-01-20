Features
========
1. Ready-to-go django blog


Environment setup
=================
1 . Installation
 ```
sudo apt-get install python3

sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```
2 . Installing, creating and running virtualenv
 ```
sudo apt install virtualenv

virtualenv -p python3 venv_blog

source venv_blog/bin/activate
```
3 . Setting up project requirements
 ```
pip3 install django

pip3 install pillow
```
4 . Installing + Cloning Git repository
 ```
sudo apt-get install git

git clone https://github.com/NoSayMe/Blog.git
```
5 . Running our project
 ```
python3 manage.py runserver 0.0.0.0:8000
```
or
 ```
nohub python3 manage.py runserver 0.0.0.0:8000 &
```
