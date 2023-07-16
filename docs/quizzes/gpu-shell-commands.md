# GPU Shell Commands Quiz

When you use a new GPU server at an AI Racing League event there are
many questions you need to have answered about your GPU server.

Here is a handy quiz you can use to check your knowledge.  The answers to the questions are listed below.

## Questions

**Question 1:** How would you log into the GPU server using the secure shell program?

A) `$ login arl@arl1.local`
B) `$ ssh arl@arl1.local`
C) `$ enter arl@arl1.local`
D) `$ connect arl@arl1.local`

**Question 2:** How would you check the version of Ubuntu on the GPU server?

A) `$ version -a`
B) `$ lsb_release -a`
C) `$ ubuntu_version -all`
D) `$ check_ubuntu -a`

**Question 3:** What information does the `lscpu` command provide?

A) It provides the CPU information.
B) It lists the amount of RAM on the server.
C) It checks the disk space.
D) It shows per-user disk usage.

**Question 4:** Which command is used to check the total RAM on the GPU server?

A) `$ free -m`
B) `$ checkram -m`
C) `$ listram -m`
D) `$ raminfo -m`

**Question 5:** What does the command `df -h /` provide?

A) It lists per user disk usage.
B) It adds a new GPU server user.
C) It checks the disk space.
D) It monitors the NVIDIA GPU.

**Question 6:** How can a new GPU server user be added?

A) `$ adduser <username>`
B) `$ newuser <username>`
C) `$ createuser <username>`
D) `$ useradd <username>`

**Question 7:** How can you give a user "sudo" rights?

A) `$ sudo usermod -aG sudo <username>`
B) `$ sudo addrights -aG sudo <username>`
C) `$ sudo giverights -aG sudo <username>`
D) `$ sudo addrules -aG sudo <username>`

**Question 8:** How can the hostname be changed?

A) `$ sudo vi hostname`
B) `$ sudo edit hostname`
C) `$ sudo change hostname`
D) `$ sudo alter hostname`

**Question 9:** What does the command `watch -d -n 0.5 nvidia-smi` do?

A) It adds a new GPU server user.
B) It runs similar to the UNIX top command, but for the GPU.
C) It checks the version of Ubuntu.
D) It lists the CPU information.

**Question 10:** How would you check the NVIDIA GPU utilization?

A) `$ checkgpu`
B) `$ nvidia-smi`
C) `$ gpu-utilization`
D) `$ utilization nvidia`

## Answers

1. B) `$ ssh arl@arl1.local`
2. B) `$ lsb_release -a`
3. A) It provides the CPU information.
4. A) `$ free -m`
5. C) It checks the disk space.
6. A) `$ adduser <username>`
7. A) `$ sudo usermod -aG sudo <username>`
8. A) `$ sudo vi hostname`
9. B) It runs similar to the UNIX top command, but for the GPU.
10. B) `$ nvidia-smi`
