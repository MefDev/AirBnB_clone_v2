#!/usr/bin/env bash
#setup a web static in the two servers
USER='ubuntu'
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
sudo chown -R "$USER:$USER" '/data/'
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Hello Holberton" > /data/web_static/releases/test/index.html      
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sed -i "12alocation /hbnb_static {\n\talias /data/web_static/current;\n\tautoindex off;\n}" "/etc/nginx/sites-available/default"
sudo service nginx restart
