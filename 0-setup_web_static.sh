#!/usr/bin/env bash
# Sets up my web server for deployment of web_static.

# Update package list and install Nginx
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Create the required directories if they do not exist
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a test HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link, first remove if it already exists
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ directory to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root   /etc/nginx/html;
    index  index.html index.htm;
    add_header X-Served-By $HOSTNAME;

    location /redirect_me {
        return 301 https://github.com/aiugreb;
    }

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    error_page 404 /404.html;
    location /404 {
      root /etc/nginx/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
sudo service nginx restart

# Ensure the script exits successfully
exit 0

