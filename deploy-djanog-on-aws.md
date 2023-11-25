<!-- for themezoz -->
ssh -i "themezoz.com.pem" ubuntu@ec2-54-175-227-249.compute-1.amazonaws.com


<!-- for shopyblack -->
ssh -i "themezoz.com.pem" ubuntu@ec2-54-159-9-249.compute-1.amazonaws.com


# after create instance or server 
# Step one 
sudo apt-get update & sudo apt-get upgrade -y 
sudo adduser hamzoooz 
sudo usermod -aG sudo hamzoooz
sudo visudo # to don't ask for passowrd always 
# in file add the folloing line
hamzoooz  ALL=(ALL) NOPASSWD:ALL


sudo apt-get install postgresql postgresql-contrib
sudo -u postgres psql


CREATE DATABASE themezoz;
CREATE USER themezoz WITH PASSWORD 'Hamzoooz&0784512346#themezoz.com';
ALTER ROLE themezoz SET client_encoding TO 'utf8';
ALTER ROLE themezoz SET default_transaction_isolation TO 'read committed';
ALTER ROLE themezoz SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE themezoz TO themezoz;
\q

sudo nano /etc/postgresql/<version>/main/postgresql.conf
listen_addresses = '*'
sudo systemctl restart postgresql

sudo nano /etc/postgresql/<version>/main/pg_hba.conf
host    replication     all             192.168.1.100/24        md5

sudo -u postgres psql -d template1
\q


<!-- python -c "import sqlparse; print(sqlparse.format(open('data_dump.sql').read(), reindent=True, keyword_case='upper'))" > postgresql_data_dump.sql
psql -U themezoz -d themezoz -f postgresql_data_dump.sql -->


## create djanog on home
sudo mkdir themezoz
sudo chown hamzoooz:hamzoooz -R themezoz 
# To check the Check the woner for dir must be for new user  


# Step tow 
su - hamzoooz # login to your account 
install python3-venv python3-pip supervisor -y  # gunicorn 
sudo apt-get install python3-venv python3-pip supervisor gunicorn  -y  # 
# create env and active and 
# and clone your project and install requerment filse 
python3 -m venv env 
source  env/bin/activate


git clone djanog 
git clone git@github.com:hamzoooz/themezoz.git
pip install -r requirements.txt 
supervisor 
sudo apt-get install supervisor 
sudo apt-get install nginx 

pip install gunicorn 
## to check every thing it work good or no 
### you must be allow setup djanog and server to allow run in this port 

python manage.py runserver 0.0.0.0:8000

gunicorn  --bind 0.0.0.0:8000 themezoz.wsgi:application

# Step Three Supervisor and gunicorn 
sudo nano /etc/supervisor/conf.d/gunicorn.conf
ubuntu
~~~bach

[program:gunicorn]
directory = /home/ubuntu/themezoz
command = /home/ubuntu/env/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/themezoz/app.sock themezoz.wsgi:application
autostart=true
autorestart=true
stderr_logfile= /var/log/gunicorn/gunicorn.err.log
stdout_logfile=/var/log/gunicorn/gunicorn.out.log
[group:guni]
programs:gunicorn

~~~
sudo mkdir /var/log/gunicorn

# check it work ? 
sudo supervisorctl reread
>> guni: available
sudo supervisorctl update
>> guni: added process group
sudo supervisorctl status 

<!-- cange the user  -->
sudo nano /etc/nginx/nginx.conf
sudo chown hamzoooz:hamzoooz -R /etc/nginx/nginx.conf


#Step Four NGINX 
sudo apt install nginx
sudo nano /etc/nginx/sites-available/djanog.conf

server {
    listen 80;
    server_name themezoz.com www.themezoz.com book-hope.com www.book-hope.com ;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
	autoindex on;
        alias /home/ubuntu/themezoz/staticfiles/;
    }
    location /media/ {
        alias /home/ubuntu/themezoz/media/;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/themezoz/app.sock;
    }
}

cd /etc/nginx/sites-available/
sudo chown hamzoooz:hamzoooz -R djanog.conf 
sudo ln /etc/nginx/sites-available/djanog.conf  /etc/nginx/sites-enabled/
sudo service nginx restart
sudo nginx -t 

<!-- go to project dir  -->
<!-- cd /home/hamzoooz/themezoz -->
python manage.py  collectstatic
# Step Five in install Free SSL with certbot 
=======
```



sudo nginx -t
sudo service nginx restart

python manage.py collectstatic
 
sudo apt install certbot python3-certbot-nginx -y 
sudo certbot `                      `




sudo ln -s /etc/nginx/sites-available/djanog.conf /etc/nginx/sites-enabled/
