# clone the application 
    git clone git@github.com:justo340/e-notes.git

# create a virtual environment
    apt install python3.11-venv
    python3 -m venv <virtual environment name>
# activate the virtual environment
    source <my_env_name>/bin/activate
# install requirements
    pip install -r requirements.txt
# migrate database
    python manage.py makemigrations
    python manage.py migrate

# run application
    python manage.py runserver

