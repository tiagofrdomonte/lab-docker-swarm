#!/bin/bash
apt-get update
apt-get install -y docker.io
usermod -aG docker vagrant
systemctl enable docker
systemctl start docker
