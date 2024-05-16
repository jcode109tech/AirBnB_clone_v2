#!/usr/bin/env bash
#Sets up a web server for deployment
echo -e "\e[1;35m Checking for nginx... \e[0m"
if command -v nginx &> /dev/null;then
     echo -e "\e[1;33m Nginx is installed.....\e[0m"
else
    sudo apt-get update -y -qq && sudo apt-get install nginx -y
    echo -e "\e[1;33m Installing Nginx...\e[0m"
#update this to update system before installing nginx
    sudo apt-get install nginx
fi
#creating files and folders
! test -d /data/ && sudo mkdir "/data/" && echo -e "\e[1;34m Created folder /data/\e[0m"
! test -d /data/web_static/ && sudo mkdir "/data/web_static/" && echo -e "\e[1;34m Created folder web_static/ in /data/\e[0m"
! test -d /data/web_static/releases/ && sudo mkdir "/data/web_static/releases/" && echo -e "\e[1;34m Created folder releases/ in /data/web_static/\e[0m"
! test -d /data/web_static/shared/ && sudo mkdir "/data/web_static/shared/" && echo -e "\e[1;34m Created folder shared/ in /data/web_static/\e[0m"
! test -d /data/web_static/releases/test/ && sudo mkdir "/data/web_static/releases/test/" && echo -e "\e[1;34m Created folder test/ in /data/web_static/releases/\e[0m"
! test -f /data/web_static/releases/test/index.html && sudo touch "/data/web_static/releases/test/index.html" && echo -e "\e[1;34m Created file index.html in /data/web_static/releases/test/\e[0m"

#Adding content to the index.html file
index_text="Yeah this worked"
echo "$index_text" | sudo dd status=none of=/data/web_static/releases/test/index.html

#creating a symlink
#removing symlinkif it exists
test -L /data/web_static/current && rm "/data/web_static/current"

sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/
#Adding server configuration
echo -e "\e[1;33m Configuring server... \e[0m"
server_config=\
"server {
		listen 80 default_server;
		listen [::]:80 default_server;
		root /var/www/html;
		index index.html index.htm index.nginx-debian.html
		server_name_;
		add_header X-Served-By \$hostname;
		location / {
			try_files \$uri \$uri/ =404;
		}
        	location /hbnb_static {
            		alias /data/web_static/current/;
        	}
		if (\$request_filename ~ redirect_me){
			rewrite ^ https://th3-gr00t.tk/ permanent;
		}
		error_page 404 /error_404.html;
		location = /error_404.html {
			internal;
		}
}"
#shellcheck disable=SC2154
echo "$server_config" | sudo dd status=none of=/etc/nginx/sites-enabled/default

#restart
echo -e "\e[1;33m restarting nginx server... \e[0m"
sudo service nginx restart
