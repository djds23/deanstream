This is DeanStream! come here to watch different 'streams' of Dean sleeping!
============================================================================

This project is primarially built on Python 2.7, Flask, SQLAlchemy, jQuery and a bit of Twitter Bootstrap

##[Watch Deanstream here!](http://test.deanstream.com/)

Now with 0.1 less SQLALCHEMY! here comes the database mess! make sure
to use sqlalchemy 0.7.10! there is an error with .8!

Be aware the "requirements.txt" file is rather bloated, but you do need gunicorn, sqlalchemy, flask-sqlalchemy, whooshalcmey, sqlalchemy-migrate and sqlite3 to update the database.

All of these dependencies can be installed using pip and run in a virtualenv.
Don't have pip? instructions here: [pip!](http://www.pip-installer.org/en/latest/)

Then:
```bash
    sudo pip install virtualenv
```

After that try to never use pip outside of  virtualenvs, keep your local install of python as clean as possible. 

At this point you can make a directory for your instance of deanstream and do a git pull of the master, but be advised this is updated rather frequently and may not always work.

Now we can create an env for your instance. The '''virtualenv <my environment name here>''' command will make a directory with its own bin and python installation.

I like to keep envs out of the dir for the app, this will keep things cleaner if you do a push, less to add to the .gitignore. For example on my dev environment I have two folders in my documents:

```bash
dsDev/my app stuff here
dsEnv/bin and python here
```
To get this I would go to my documents and perform the command: 

```bash
virtualenv dsEnv
```

This creates my directory and installs python, even installs it's own pip!

To enter this evn perform the command:
```bash
source dsEnv/bin/activate
```

To leave the env, at anytime perform the command:
```bash
deactivate
```

Then pip install whatever packages from the requirements.txt, again it's sort of bloated due to some silly ideas I had. The master should run off flask alone, but the multi totally requires SQLalchemy, SQLalchemy-flask, SQLalchemy-migrate and all that jazz. Make sure you use the SQLalchemy version I specify, 0.7 I believe, new ones won't work (learned that the hard way). 

Once your all set up, run with this command:
```bash
gunicorn run:app
```

It will be sent to localhost port 8000

To run in debug, add this line to the bottom of 'run.py'

```python
app.run(debug=True)
```

deanstream will run on localhost port 5000

