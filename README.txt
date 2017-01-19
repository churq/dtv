
******************
install dependency
******************
please install all the dependencies
> pip install -r requirements.txt

if there is connection error, try:
>pip install --index-url=http://pypi.python.org/simple/ --trusted-host pypi.python.org  -r requirements

******************
set up database
******************

> python db_setup.py

******************
execution
******************

> python main.py


Sorry I didn't write enough unit tests because I don't have enough time