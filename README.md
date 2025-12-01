hosted on PythonAnywhere.  Go to:
https://mickeymouseandgoofey.pythonanywhere.com/login/


Local Machine Setup:

Prerequisites

  Python: Install Python 3.10+ and confirm it’s on your PATH.
  
  Windows: python --version
  
  Mac/Linux: python3 --version

  Git: Install Git and confirm it’s available: git --version
  
  Database:
  PostgreSQL: Install server and client tools.


Setup Instructions (Windows OS):

Clone the Repo:
git clone https://github.com/mickeymouseandgoofey/favlinks.git
cd favlinks

Create and Activate the Virtual Environment (Windows) (Note - must be inside project folder directory cd favlinks):
python -m venv venv
.\venv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt


Install Database Drivers:
pip install psycopg2-binary


Create Django Secret Key:
python -c "import secrets; print(secrets.token_urlsafe(50))"


Setup Postgresql database:
# Open psql
psql -U postgres

-- Inside psql:
CREATE DATABASE favlinks;
CREATE USER favlinks_user WITH PASSWORD 'your_strong_password';
ALTER ROLE favlinks_user SET client_encoding TO 'utf8';
ALTER ROLE favlinks_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE favlinks_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE favlinks TO favlinks_user;
\q


Create .env file and fill in information:
Windows:  in file explorer, go to the root of the project folder (where manage.py lives) and create a file called .env
Open the file in a text editor (recommend Notepad++ and copy/paste and fill in the values below:

SECRET_KEY=paste_your_generated_key_here   #(see step above)
DB_USER='favlinks_user'    #(see step above)
DB_PASSWORD='your_strong_password'    #(see step above)
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost


Apply Migrations:
python manage.py migrate


Create the Django admin user:
python manage.py createsuperuser


Now your all setup!  Let's get this project going:
python manage.py runserver

Go to:
App: http://127.0.0.1:8000
Admin Console: http://127.0.0.1:8000/admin









