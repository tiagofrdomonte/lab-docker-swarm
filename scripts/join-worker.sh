#!/bin/bash
MASTER_IP=$1
TOKEN=$(cat /vagrant/worker-token)
docker swarm join --token $TOKEN $MASTER_IP:2377
