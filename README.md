# fedgehundapi

### Setup

1. Clone this repository
2. Create a virtual environment. (Follow tutorial [here](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv))
    ```shell
    virtualenv myenv
    ```
3. Activate the virtual environment
    ```shell
    source myenv/bin/activate
    ```
4. Install all the required packages from `requirements.txt`
   ```shell
   pip install -r requirements.txt
   ```   
5. Install mongodb-community version 4.2.8

   ##### On Mac-
   ```shell
   brew install mongodb-community@4.2
   ```
   ##### On Windows-
   
   Follow this tutorial to install it interactively:
   
   https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/
   
   Follow this to install from the command prompt:
   
   https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows-unattended/

6. Follow this tutorial to run mongodb:

   https://www.youtube.com/watch?v=nJVbTnNdqL0
 
7. You are ready to run the Django app. To run django app follow the django tutoral

### How to make a contribution ?

1. Create a new branch before making any change.
2. Add all new packages to `requirements.txt` (Make sure you are in a virtual environment before doing this)
    ```shell
    pip freeze > requirements.txt
    ```
3. Put up a PR for review.


### Version

- Python 3.7.3
