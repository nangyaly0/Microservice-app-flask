Vagrant.configure("2") do |config|
  (1..2).each do |i|
    config.vm.define "vm#{i}" do |node|
      # Use the official Ubuntu 20.04 LTS box
      node.vm.box = "bento/ubuntu-20.04"
    
      # Uncomment the line below if you want to use DHCP for private network
      node.vm.network "private_network", type: "dhcp"

      # Use a public network with a specific bridge adapter
      #node.vm.network "public_network", bridge: "en0"

      # Forward ports for accessing services
      node.vm.network "forwarded_port", guest: 80, host: 8080 + i
      node.vm.network "forwarded_port", guest: 2377, host: 2377 + i
      node.vm.network "forwarded_port", guest: 7946, host: 7946 + i
      node.vm.network "forwarded_port", guest: 4789, host: 4789 + i
    
      # Configure provider-specific settings
      node.vm.provider "virtualbox" do |vb|
        # Customize the VM settings
        vb.memory = "1024"
        vb.cpus = 1
      end
    
      # Provisioning script (optional)
      node.vm.provision "shell", path: "provision.sh"
    end
  end
end


  