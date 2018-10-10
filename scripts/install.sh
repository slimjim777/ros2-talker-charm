#!/bin/sh

PROJECT=talker
BIN_DIR=/usr/bin
LIB_DIR=/usr/lib/${PROJECT}
SERVICE=/lib/systemd/system

# Build the application
colcon build

# Make the directories
mkdir -p ${LIB_DIR}

# Install the application
cp -r install ${LIB_DIR}
cp launchers/talker ${BIN_DIR}
cp launchers/talker.service ${SERVICE}/

echo Configure launchers to be used in systemd service
sed -i 's/{{[ ]*libdir[ ]*}}/\/usr\/lib\/talker/g' ${BIN_DIR}/talker

echo Restart the daemon for good measure
systemctl daemon-reload

# Restart the service
systemctl restart talker

exit 0