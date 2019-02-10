FROM debian:stable
RUN apt-get update -y 
RUN apt-get install -y openssh-server
RUN echo "PasswordAuthentication no" >> /etc/ssh/sshd_config
RUN useradd falken -d /home/falken -s /bin/bash -m 
RUN mkdir /home/falken/.ssh
COPY authorized_keys /home/falken/.ssh/authorized_keys
COPY flag /home/falken/flag
RUN mkdir -p /run/sshd
CMD ["/usr/sbin/sshd", "-D"]
