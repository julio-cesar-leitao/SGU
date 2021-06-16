#################
##  (1) npm    ##
#################

We’ll use npm to install http-server and json-server. The easiest way to install npm is install node.js, that comes with npm. <https://nodejs.org/en/>


#####################
## (2) JSON-Server ##
#####################

# Install json-server
npm install -g json-server

# Find your IP (like 192.168.0.14) and inside /public folder run:
json-server --host 192.168.0.XX sguData.json
# This will start a json server that can receive raspberry pi data via http (post, put, etc.)

#####################
## (3) http-server ##
#####################

# Install http-server
npm install –g http-server

# Inside /public folder run:
http-server

# If you’re on Windows, you must first unlock execution of scripts with the command “Set-ExecutionPolicy RemoteSigned” on powershell as administrator