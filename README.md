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

For the simplicity we have been using sqlite database 