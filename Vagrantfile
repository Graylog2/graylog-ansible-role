Vagrant.configure("2") do |config|
    config.vm.box = "generic/ubuntu1804"

    config.vm.define 'ubuntu'

    # Vagrant boot needs more time on AppVeyor (see https://help.appveyor.com/discussions/problems/1247-vagrant-not-working-inside-appveyor)
    config.vm.boot_timeout = 1800

    # Prevent SharedFoldersEnableSymlinksCreate errors
    config.vm.synced_folder ".", "/vagrant", disabled: true

    config.vm.provider :virtualbox do |vb|
        vb.name = 'ubuntu'
        vb.memory = 128
        vb.cpus = 1
        # Vagrant needs this config on AppVeyor to spin up correctly (see https://help.appveyor.com/discussions/problems/1247-vagrant-not-working-inside-appveyor)
        vb.customize ["modifyvm", :id, "--nictype1", "Am79C973"]
        vb.customize ['modifyvm', :id, '--cableconnected1', 'on']
    end
end
