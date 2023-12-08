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

if [ ! -d '/data/' ]; then
    sudo mkdir -p '/data/'
    echo "The data folder was created successfully"
    sudo chown -R "$USER:$USER" '/data/'
    echo "The ownership was given to $USER"
else
    echo "The date folder is already exist"
    rm -r "/data/"
fi

if [ ! -d "/data/$folder_web_static" ]; then
    sudo mkdir -p "/data/$folder_web_static"
    echo "$folder_web_static was created successfully"
    
    
    if [ ! -d "/data/$folder_web_static/$folder_release" ]; then
        sudo mkdir -p "/data/$folder_web_static/$folder_release"
        echo "The release folder was created successfully"
        
        if [ ! -d "/data/$folder_web_static/$folder_release/$folder_test" ]; then 
            sudo mkdir "/data/$folder_web_static/$folder_release/$folder_test"
            echo "The folder test was created successfully"
            echo "Hello Holberton" > "/data/$folder_web_static/$folder_release/$folder_test/index.html"       
            echo "The file index.html was created in the test folder"
        else
            echo "Test folder already exists"
        fi
    else
        echo "The folder release already exists"
    fi

    if [ ! -d "/data/$folder_web_static/$folder_shared" ]; then
        sudo mkdir "/data/$folder_web_static/$folder_shared"
        echo "The shared folder was created successfully"
    else
        echo "The shared folder already exists"
    fi

    if [ ! -L "$current" ]; then
        sudo ln -s "/data/web_static/releases/test/" "$current"
        echo "The current has a symbolic link to test folder"
    else
        echo "The 'current' file already exists"
        sudo rm "$current"
        echo "The previous 'current' was removed"
    fi

else
    echo "The folder web_static already exists"
fi

# Modify Nginx configuration using sed
sed -i "12alocation /hbnb_static {\n\talias /data/web_static/current;\n\tautoindex off;\n}" "/etc/nginx/sites-available/default"

# Restart the service
sudo service nginx restart
