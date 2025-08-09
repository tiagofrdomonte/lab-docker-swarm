# Vagrantfile
VAGRANTFILE_API_VERSION = "2"

NODES = [
  { name: "master", ip: "192.168.56.10" },
  { name: "node01", ip: "192.168.56.11" },
  { name: "node02", ip: "192.168.56.12" },
  { name: "node03", ip: "192.168.56.13" }
]

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/focal64"

  NODES.each_with_index do |node_info, i|
    config.vm.define node_info[:name] do |node|
      node.vm.hostname = node_info[:name]
      node.vm.network "private_network", ip: node_info[:ip]
      node.vm.provider "virtualbox" do |vb|
        vb.name = node_info[:name]
        vb.memory = 1024
        vb.cpus = 1
      end

      node.vm.provision "shell", path: "scripts/setup.sh"

      if i == 0
        node.vm.provision "shell", path: "scripts/init-swarm.sh"
      else
        node.vm.provision "shell", path: "scripts/join-worker.sh", args: [NODES[0][:ip]]
      end
    end
  end
end
