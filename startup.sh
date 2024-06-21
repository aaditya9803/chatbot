#!/bin/bash

# Update package list and install Python
apt-get update
apt-get install -y python3

# Navigate to the app directory (if necessary)
cd /home/site/wwwroot

# Start the Node.js server
npm start
