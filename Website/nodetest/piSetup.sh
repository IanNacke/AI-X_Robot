#run this on the raspberry pi - all it does is install necessary packages
#this is a shell file, which means you run it by typing ./shellfiletorun.sh
#shell files just emulate the user typing in commands to the console, like a bash script on windows
#In some cases the shell file needs to have proper permissions, in which case you have to type chmod +x shellfiletoelevate.sh (this makes it turn green :D)

#updates first, kids
sudo apt-get update
sudo apt-get dist-upgrade

#curl is used to download a file from a website. Normally we would only need the apt-get command (next line), but doing so installs a horrifically out of date version of nodejs, so we need to manually install the latest version
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
#this is the default install command for raspbian (debian and ubuntu too)
#the -y makes it so that it automatically agrees to everything (user doesn't need to)
#sudo apt-get remove is how you would remove packages if you wanted (purge is also an option)
sudo apt-get install nodejs -y

#npm is a program that installed with nodejs
npm install socket.io --save
