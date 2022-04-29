# HappinessTracker

## Setup

The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/sabitrakhl/happiness-tracker.git
$ cd happiness-tracker
```

Create a virtual environment to install dependencies in and activate it:
```sh
$ python -m venv <env_name>
$ source <env_name>/bin/activate
```

Then install the dependencies:
```sh
$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies, execute the following command in the directory where manage.py script exists.
```sh
python manage.py migrate
```
For the simplicity we are using sqlite database for this project.

Then create the superuser:
```sh
python manage.py createsuperuser
```

Now Django will prompt you to enter the details, enter your desired details and hit enter.
```sh
Username (leave blank to use 'admin'): admin
Email address: admin@xyz.com
Password: ********
Password (again): ********
Superuser created successfully.
```

Now that the superuser is created, run the development server.
```sh
$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/admin/` to create the group (team), user and assign the user to group.


## APIs

You can access our APIs, directly through the browser, by going to the URLs.
If you're working through the browser, make sure to login using the control in the top right corner.

### Info Create

Use this API to submit happiness level.

*Parameters*
```sh
{
   "happiness_level": 6
}
```


```sh
POST /api/v1/info/create/
```

### Info Retrieve

Use this API to retrieve happiness level.

```sh
GET /api/v1/info/
```

if an authenticated request is made to this API, it returns the statistics of user's team - the number of people at each level of happiness and the average happiness of the user's team.

if an unauthenticated request is made, return the average happiness across all teams.



## Test

To run the tests, cd into the directory where manage.py is:

```sh
python manage.py test
```
