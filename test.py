import subprocess

proc = subprocess.Popen(["cat", "/d/devVMs/vagrant-rails-sqlite/Vagrantfile"], stdout=subprocess.PIPE)
(out, err) = proc.communicate()
print ("program output:", out)