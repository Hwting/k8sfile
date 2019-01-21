FROM cloudbees/java-build-tools
MAINTAINER  wang.t.ince@gmail.com
USER root

ARG JENKINS_REMOTING_VERSION=3.23

# See https://github.com/jenkinsci/docker-slave/blob/master/Dockerfile#L31
LABEL Description="This is a extend image base from jenkins/jnlp-slave which install maven in it."
RUN   rm -rf  /etc/apt/sources.list.d/* \
	&& echo "deb http://mirrors.aliyun.com/ubuntu/ xenial main \n deb-src http://mirrors.aliyun.com/ubuntu/ xenial main" > /etc/apt/sources.list
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/$JENKINS_REMOTING_VERSION/remoting-$JENKINS_REMOTING_VERSION.jar \ 
  && apt-get  update && apt-get install subversion -y \
  && chmod 755 /usr/share/jenkins \
  && chmod 644 /usr/share/jenkins/slave.jar

COPY jenkins-slave /usr/local/bin/jenkins-slave 
COPY   docker /usr/bin/
COPY config /home/jenkins/.kube/
COPY kubectl /usr/bin/
RUN chmod a+rwx /home/jenkins && \
    chmod +x /usr/bin/docker && \
    chmod +x /usr/bin/kubectl
WORKDIR /home/jenkins
USER jenkins

ENTRYPOINT ["/opt/bin/entry_point.sh", "/usr/local/bin/jenkins-slave"]
