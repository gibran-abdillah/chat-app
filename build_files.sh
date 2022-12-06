apt-get install libmysqlclient-dev
pip3 install -r requirements.txt
pip3 install mysqlclient
python3 manage.py makemigrations
python3 manage.py migrate
