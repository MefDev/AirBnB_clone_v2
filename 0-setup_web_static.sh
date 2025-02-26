#!/usr/bin/env bash
# setup a web static in the two servers

USER='ubuntu'
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Hello Holberton" > /data/web_static/releases/test/index.html      
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R "$USER:$USER" '/data/'

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm, index.nginx-debian.html;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm index.nginx-debian.html;
    }

    location /redirect_me {
        return 301 http://hbnbairbnb.com;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default
sudo service nginx restart
