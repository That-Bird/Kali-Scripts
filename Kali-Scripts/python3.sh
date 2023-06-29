#!/bin/bash

#code body

echo "install will now begin"
sleep 3
echo "."
sleep 1
echo "."
sleep 1

echo "<><>"
echo "getting kali update..."
sleep 3
echo "."
sleep 1
echo "."
sleep 1
sudo apt-get update -y

echo "<><>"
echo "upgrading kali..."
sleep 3
echo "."
sleep 1
echo "."
sleep 1
sudo apt-get upgrade -y

echo "<><>"
echo "installing python3..."
sleep 3
echo "."
sleep 1
echo "."
sleep 1
sudo apt install python3 -y

echo "<><>"
echo "adding pip to python3..."
sleep 3
echo "."
sleep 1
echo "."
sleep 1
sudo apt install python3-pip -y

echo "<><>"
echo "adding psutil library for python3"
sleep 3
echo "."
sleep 1
echo "."
sleep 1
sudo apt-get install python3-psutil -y

echo "<>success<>"
echo "python and all dependencies now installed"
sleep 5

#end code
