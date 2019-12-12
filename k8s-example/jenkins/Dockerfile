FROM  jenkins/jnlp-slave:latest
USER root
RUN echo "${TIMEZONE}" > /etc/timezone \
    && echo "$LANG UTF-8" > /etc/locale.gen \
    && apt-get update -q \
    && ln -sf /usr/share/zoneinfo/${TIMEZONE} /etc/localtime 

COPY kubectl /usr/bin/kubectl
COPY docker /usr/bin/docker
RUN  DEBIAN_FRONTEND=noninteractive apt-get install -yq curl apt-utils dialog locales  apt-transport-https build-essential bzip2 ca-certificates  sudo jq unzip zip gnupg2 software-properties-common \
     && update-locale LANG=$LANG \
     && locale-gen $LANG \
     && DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales \
     &&curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg |apt-key add - \
     && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable" \
     && apt-get update -y \
     && apt-get install -y docker-ce=17.09.1~ce-0~debian \
     && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
     && usermod -a -G docker jenkins \
     && sed -i '/^root/a\jenkins    ALL=(ALL:ALL) NOPASSWD:ALL' /etc/sudoers
ENTRYPOINT ["jenkins-slave"]
