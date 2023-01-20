#!/bin/bash

sudo yum -y update
sudo yum install -y httpd
sudo service httpd start
sudo service httpd enable

sudo echo "Welcome to Wim's AWS Project!" > /var/www/html/index.html