#!/usr/bin/env bash

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo touch /data/web_static/releases/test/index.html
echo "This is a simple test" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ folder to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
nginx_alias="location /hbnb_static { alias /data/web_static/current/; }"
if ! grep -qF "$nginx_alias" "$nginx_config"; then
    sudo sed -i "/server_name _;/a $nginx_alias" "$nginx_config"
fi

# Restart Nginx
sudo service nginx restart
