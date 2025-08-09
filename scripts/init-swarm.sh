#!/bin/bash
docker swarm init --advertise-addr $(hostname -I | awk '{print $2}')
docker swarm join-token -q worker > /vagrant/worker-token
