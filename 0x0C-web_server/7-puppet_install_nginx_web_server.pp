#!/usr/bin/env bash
# Configure your Nginx server to have a custom 404 page

apt-get update
apt-get install -y nginx

mkdir /etc/nginx/html
touch /etc/nginx/html/index.html
echo "Hello World!" > /etc/nginx/html/index.html
printf %s "server {
     listen      80 default_server;
     listen      [::]:80 default_server;
     root        /etc/nginx/html;
     index       index.html index.htm;
}
" > /etc/nginx/sites-available/default

touch /etc/nginx/html/404.html

echo "Ceci n'est pas une page" | sudo tee /etc/nginx/html/404.html

echo "Nginx installation and configuration completed."

echo "server {
    listen      80;
    listen      [::]:80;
    root        /etc/nginx/html;
    index       index.html index.htm;
    
    index index.html index.htm index.nginx-debian.html;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location /404 {
      root /etc/nginx/html;
      internal;
    }

}" | sudo tee /etc/nginx/sites-available/default

sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Test nginx configuration and reload
sudo nginx -t
sudo service nginx reload

