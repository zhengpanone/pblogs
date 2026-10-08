=====================
Jenkins离线安装
=====================


Linux 离线安装 Jenkins
=====================

适用环境
--------
- 操作系统：CentOS 7 / CentOS 8
- 架构：x86_64
- 网络环境：无外网连接
- 安装方式：Jenkins WAR 包 + systemd

前置依赖
--------
Jenkins 是 Java 程序，离线环境必须先解决 JDK：

- Jenkins 2.426+ ：要求 JDK 17 或 21
- Jenkins 2.346 LTS ：JDK 11 可运行
- 推荐离线下载 OpenJDK 17（Temurin / Adoptium）

字体依赖（无图形界面服务器建议装）：
- fontconfig

在有网机器上下载
----------------
1. 下载 JDK 17（tar.gz 或 rpm）
   https://adoptium.net/

2. 下载 Jenkins 稳定版 WAR 包
   https://get.jenkins.io/war-stable/
   例如：
   jenkins.war

3. 通过 U 盘 / FTP / scp 传到目标服务器，例如：
   /opt/jenkins/

安装 JDK
--------
tar.gz 方式示例：

.. code-block:: bash

    mkdir -p /usr/lib/jvm
    tar -zxvf jdk-17*.tar.gz -C /usr/lib/jvm
    cat > /etc/profile.d/java.sh <<'EOF'
    export JAVA_HOME=/usr/lib/jvm/jdk-17
    export PATH=$JAVA_HOME/bin:$PATH
    EOF
    source /etc/profile.d/java.sh
    java -version

rpm 方式示例：

.. code-block:: bash

    rpm -ivh jdk-17*.rpm
    java -version

安装 Jenkins
------------
.. code-block:: bash

    mkdir -p /opt/jenkins
    cp jenkins.war /opt/jenkins/
    mkdir -p /var/lib/jenkins
    useradd -r -m -s /bin/bash jenkins
    chown -R jenkins:jenkins /opt/jenkins /var/lib/jenkins

创建 systemd 服务
----------------
编辑 /etc/systemd/system/jenkins.service：

.. code-block:: ini

    [Unit]
    Description=Jenkins CI Server
    After=network.target

    [Service]
    Type=simple
    User=jenkins
    Environment="JENKINS_HOME=/var/lib/jenkins"
    Environment="JAVA_HOME=/usr/lib/jvm/jdk-17"
    ExecStart=/usr/lib/jvm/jdk-17/bin/java \
        -Djava.awt.headless=true \
        -jar /opt/jenkins/jenkins.war \
        --httpPort=8080
    WorkingDirectory=/var/lib/jenkins
    Restart=on-failure
    RestartSec=10

    [Install]
    WantedBy=multi-user.target

启动与验证
----------
.. code-block:: bash

    systemctl daemon-reload
    systemctl enable jenkins
    systemctl start jenkins
    systemctl status jenkins

查看初始管理员密码：

.. code-block:: bash

    cat /var/lib/jenkins/secrets/initialAdminPassword

浏览器访问：

.. code-block:: text

    http://<服务器IP>:8080

离线插件安装
------------
离线环境不要在初始化向导中选“安装推荐插件”，选“无”。

后续离线装插件两种方式：

1. 单插件上传
   在联网机下载 .hpi：
   https://plugins.jenkins.io/
   管理界面：
   Manage Jenkins -> Plugins -> Advanced settings -> Deploy Plugin

2. 同版本 Jenkins 整体拷贝（推荐）
   在联网机装好同版本 Jenkins 和所需插件，
   拷贝以下目录到离线机：

.. code-block:: bash

    /var/lib/jenkins/plugins/

然后重启：

.. code-block:: bash

    systemctl restart jenkins

常见问题
--------
- 启动报 Fontconfig head is null
  安装 fontconfig 或拷贝 JDK 8 的 fontconfig.bfc 到 JDK lib 目录

- 页面打不开
  检查防火墙：
  firewall-cmd --add-port=8080/tcp --permanent
  firewall-cmd --reload

- 构建节点要用 Docker
  把 jenkins 用户加入 docker 组：
  usermod -aG docker jenkins
  systemctl restart jenkins

- 插件缺依赖
  离线插件有依赖链，优先用“同版本 Jenkins 插件目录整体拷贝”