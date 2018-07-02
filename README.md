# LOCAL LIBRARY WEBSITE TUTORIAL - MDN WEB DOCS

Source: [Local Library Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)

## **QUICK GUIDE**
###### Disclaimer: This guide actual purpose is to guide me or as a reminder for me how to do it. I'm not responsible for anything bad happen to your machine and you if you decide to follow this
###### At this time of writing this I'm using Python 3.7 and macOS High Sierra version 10.13.4
###### Source of guide from [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment) and few things added by me

1. Python3 installation along with Pip
    - Download from [Python](https://www.python.org/downloads/) and install it
    - After installation open Terminal and type `python3 --version` and it will print out the version (installation successful)
    - Type `pip3 --version` and it should print out pip version and it's directory e.g `pip 10.0.1 from /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pip (python 3.7)`
    - We'll be using pip to set up virtual environment and install Django

2. Install virtualenvwrapper
    - open Terminal and type `sudo pip3 install virtualenvwrapper`
    - After installation type `virtualenv --version` and it should print out the version (installation successful)
    - Then go to your home folder in Terminal (usually `/Users/<yourname>`) and type `sudo nano .bash_profile`
    - Add the following line
    ```
    export WORKON_HOME=$HOME/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
    export PROJECT_HOME=$HOME/Devel
    source /Library/Frameworks/Python.framework/Versions/3.7/bin/virtualenvwrapper.sh
    ```
    - Exit and save nano then type `source ~/.bash_profile` and few scripts will run
    - Quit Terminal and open it again (just to make sure Terminal already load the updated .bash_profile)

3.  Creating a virtual environment (virtualenv)
    - Open terminal and type `mkvirtualenv django_virtualenv`
    - It will set things up and then put you in the virtualenv e.g `(django_virtualenv) YourComputer:~ yourName$`

4. Installing Django
    - In case you quit your terminal, open it again and type `workon`. It will print out list of virtualenv
    - Let's use the existing that has been created above. In terminal type `workon django_virtualenv`
    - After entering the virtualenv, type `pip3 install django` to install Django
    - Then type `python3 -m django --version` to print out django version (installation successful)
    - Note: if you try to check django version OUTSIDE of virtualenv or inside another virtualenv you'll get `No module named django` instead