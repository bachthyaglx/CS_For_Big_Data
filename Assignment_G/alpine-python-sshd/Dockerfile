#######################################################################
# Dockerfile to build image for Python-Alpine container that also has
# ssh access.
#
# Use python:alpine image and install needed packages for ssh:
#  - openrc, system services control system
#  - openssh, client- and server side ssh
#  - sudo, utility to enable root rights to users
#
FROM python:3.9-alpine3.19

RUN apk update
RUN apk add --no-cache openrc
RUN apk add --update --no-cache openssh
RUN apk add --no-cache sudo

# adjust sshd configuration
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
RUN echo 'PermitEmptyPasswords yes' >> /etc/ssh/sshd_config
RUN echo 'IgnoreUserKnownHosts yes' >> /etc/ssh/sshd_config

# add user larry with empty password
RUN adduser -h /home/larry -s /bin/sh -D larry
RUN echo -n 'larry:' | chpasswd

# add larry to sudo'ers list
RUN mkdir -p /etc/sudoers.d
RUN echo '%wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers.d/wheel
RUN adduser larry wheel

# generate host key
RUN ssh-keygen -A

# add sshd as service, start on boot [default], touch file to prevent error:
# "You are attempting to run an openrc service on a system which openrc did not boot."
RUN rc-update add sshd default
RUN mkdir -p /run/openrc
RUN touch /run/openrc/softlevel

# start sshd - ssh larry@localhost now working
# /etc/init.d/sshd start
# service sshd start
# ---- exec prevents shell as parent process
# exec /usr/sbin/sshd -D -e &
RUN exec /usr/sbin/sshd &

# Copy the Python script into the user's home directory
COPY print_sys.py /home/larry/print_sys.py

# sshd is started in /entrypoint.sh
#
#######################################################################

ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 22
COPY entrypoint.sh /
