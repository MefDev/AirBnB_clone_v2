#!/usr/bin/env bash
# setup a web static in the two servers

folder_web_static='/web_static'
folder_release='releases/'
folder_shared='shared/'
folder_test='test/'
current='/data/web_static/current'
USER='ubuntu'

# update and install nginx
sudo apt-get update
sudo apt-get install nginx -y

sudo mkdir -p '/data/'
sudo chown -R "$USER:$USER" '/data/'
sudo mkdir "/data/$folder_web_static/$folder_shared"
sudo mkdir -p "/data/$folder_web_static/$folder_release"
sudo mkdir "/data/$folder_web_static/$folder_release/$folder_test"
echo "Hello Holberton" > "/data/$folder_web_static/$folder_release/$folder_test/index.html"       
sudo ln -s "/data/web_static/releases/test/" "$current"
# Modify Nginx configuration using sed
sed -i "12alocation /hbnb_static {\n\talias /data/web_static/current;\n\tautoindex off;\n}" "/etc/nginx/sites-available/default"

# Restart the service
sudo service nginx restart
