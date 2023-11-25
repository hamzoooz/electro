# after create instance or server 
# Step one 
sudo apt-get update & sudo apt-get upgrade -y 
sudo adduser hamzoooz 
sudo usermod -aG sudo hamzoooz
sudo visudo # to don't ask for passowrd always 
# in file add the folloing line
hamzoooz  ALL=(ALL) NOPASSWD:ALL


## create djanog on home
sudo mkdir themezoz
sudo chown hamzoooz:hamzoooz -R themezoz 
# To check the Check the woner for dir must be for new user  

# Step tow 
su - hamzoooz # login to your account 
install python3-venv python3-pip supervisor -y  # gunicorn 
sudo apt-get install python3-venv python3-pip supervisor -y  # gunicorn 
# create env and active and 
# and clone your project and install requerment filse 
python3 -m venv env 
source  env/bin/activate

git clone djanog 
git clone git@github.com:hamzoooz/themezoz.git
pip install -r requerment.txt 
sudo pip3 install gunicorn 
sudo apt-get install supervisor 
sudo apt-get install nginx 

pip install gunicorn 
## to check every thing it work good or no 
### you must be allow setup djanog and server to allow run in this port 


python manage.py runserver 0.0.0.0:8000

# Step Three Supervisor and gunicorn 
cd /etc/supervisor/conf.d/
sudo nano gunicorn.conf

~~~bach

[program:gunicorn]
directory=/home/ubuntu/themezoz
command=/home/ubuntu/env/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/themezoz/app.sock themezoz.wsgi:application
autostart=true
autorestart=true
stderr_logfile=/var/log/gunicorn/gunicorn.err.log
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

sudo nano /etc/nginx/nginx.conf


#Step Four NGINX 
sudo apt install nginx
cd /etc/nginx/sites-available/djanog.conf

 
server {
        listen 80;
        server_name themezoz.com www.themezoz.com 18.232.91.199 ;
        location / {
                include proxy_params;
                proxy_pass http://unix:/home/ubuntu/themezoz/app.sock;
        }
        location /static/ {
                autoindex on;
                alias /home/ubuntu/themezoz/staticfile/;
        }
}

 
sudo ln djanog.conf  /etc/nginx/sites-enabled/

sudo service nginx restart
sudo nginx -t 

python manage.py  collectstatic
# Step Five in install Free SSL with certbot 
=======
```
sudo nginx -t
sudo service nginx restart

python manage.py collectstatic
 
sudo apt install certbot python3-certbot-nginx -y 
sudo certbot 

server {
    listen 80;
    server_name themezoz.com www.themezoz.com ;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/themezoz/themezoz/staticfile/;
    }
    location /media/ {
        root /home/themezoz/themezoz//media;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/themezoz/env/bin/gunicorn.sock;
    }
}


sudo ln -s /etc/nginx/sites-available/djanog.conf /etc/nginx/sites-enabled/
