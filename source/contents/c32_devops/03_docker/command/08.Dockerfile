FROM centos
RUN yum update && yum install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:root123' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

RUN yum install -y vim
# install zsh
RUN apt-get install -y zsh && apt-get install -y wget
RUN apt-get install -y git
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh

RUN mkdir -p ~/work/python/projects
RUN chmod 775 -R ~/work/python/

ADD $PWD/install.sh ~/work/python/
ADD $PWD/code.sh ~/work/python/

## 安装python的apt软件包
RUN chmod a+x ~/work/python/install.sh && ~/work/python/install.sh

## 安装python的工具
RUN chmod a+x ~/work/python/code.sh && ~/work/python/code.sh

## 自定义配置python环境并使之生效
ADD $PWD/.zshrc ~/.zshrc
RUN source ~/.zshrc

## 搭建python2.7 以及 python3.x的开发环境
RUN mkvirtualenv --python=/usr/bin/python2.7 env2.7 && mkvirtualenv --python=/usr/bin/python3.5 env3.5

## 暴露docker容器的端口
EXPOSE 3306 80 22
CMD ["/usr/sbin/sshd", "-D"]