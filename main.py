from paramiko import SSHClient, AutoAddPolicy

#Setting up the SSH client
client = SSHClient()

#Checking the host keys
client.load_system_host_keys()

#Connecting to the host by entering the IP adress, username and password
client.connect('<Enter The IP Adress Here>', username='<Enter The Username Here>', password= "<Enter The Password Here>")

# Running a command to the terminal 
# In this code, I am running the ls command which lists all the files in the directory
stdin, stdout, stderr = client.exec_command('ls')
print(type(stdin))
print(type(stdout))
print(type(stderr))

# Printing the output of the command
print(f'STDOUT: {stdout.read().decode("utf8")}')
print(f'STDERR: {stderr.read().decode("utf8")}')

# Gettig the return code from command message (0 is default for success)
print(f'Return code: {stdout.channel.recv_exit_status()}')

# Because they are file objects, they need to be closed
stdin.close()
stdout.close()
stderr.close()

# Closing the client itself
client.close()

#End of the program :)
