# saltbox

### RAMCO API Explorer

dockerized flask app base with nginx proxy, login, automated SSL, & bootstrap

you need your domain's A records correctly pointed at the docker host IP.

Tested on Ubuntu 18.04 with Docker and Docker-Compose installed using the instructions at: 

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04
https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04


Installation:
```
# git to home directory and enter
git clone https://github.com/mansard/saltbox.git
cd saltbox

# make ssl setup script executable
sudo chmod +x cert.sh

# get inital SSL certs from letsencrypt
sudo ./cert.sh

# bring up service
sudo docker-compose up --build

# run detached
sudo docker-compose up -d
```

Destroy it: 
```
# get into the directory
cd saltbox
docker-compose down

# RESET DOCKER KILL ALL IMAGES, CONTAINERS, VOLUMES CAREFUL!
docker rmi $(docker images -a -q)
docker volume rm $(docker volume ls -q)
docker system prune -a

# delete the directory 
cd
sudo rm -rf saltbox
```

