#!/bin/bash

# Set up web_static for deployment

sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

echo -e "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '42i\    location /hbnb_static {\n        alias /data/web_static/current/;\n    }\n' /etc/nginx/sites-available/default

sudo service nginx restart
