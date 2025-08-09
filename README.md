# 🐳 Docker Swarm Cluster com Flask, PostgreSQL e NGINX

Este projeto cria uma infraestrutura **local** de 4 VMs usando **Vagrant** e **Docker Swarm**, com:

- 1 nó master e 3 nós workers
- Docker instalado automaticamente em todas as VMs
- Swarm iniciado e workers ingressando automaticamente
- Deploy de uma aplicação Flask com banco de dados PostgreSQL
- Balanceador de carga NGINX na camada de entrada
- Tudo acessível via `http://app.local` no navegador

---

## 📦 Componentes do Projeto

- **Vagrant** + VirtualBox: para criar as 4 VMs
- **Docker Swarm**: orquestração de containers
- **NGINX**: balanceador de carga
- **Flask**: aplicação web Python
- **PostgreSQL**: banco de dados relacional com volume
- **Gunicorn**: servidor WSGI de produção para Flask

---

## 📁 Estrutura do Projeto

```plaintext
docker-swarm-cluster/
├── Vagrantfile
├── scripts/
│   ├── setup.sh
│   ├── init-swarm.sh
│   └── join-worker.sh
└── app/
    ├── web/
    │   ├── app.py
    │   └── requirements.txt
    ├── db/
    │   └── init.sql
    ├── nginx/
    │   └── nginx.conf
    ├── Dockerfile
    └── docker-compose.yml

```

---

## 🚀 Como usar

### 1. Pré-requisitos

- [Vagrant](https://www.vagrantup.com/downloads)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

> Testado com: Vagrant 2.3+, VirtualBox 7+
