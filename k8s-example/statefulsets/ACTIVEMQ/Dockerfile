FROM openjdk:8
MAINTAINER wang.t "wang.t.nice.gmail.com"
COPY activemq /opt/activemq
RUN chmod +x /opt/activemq/bin/activemq
# Expose all port
EXPOSE 8161
EXPOSE 61616
EXPOSE 61619
WORKDIR /opt/activemq

CMD ["/bin/sh", "-c", "/opt/activemq/bin/activemq console"]
