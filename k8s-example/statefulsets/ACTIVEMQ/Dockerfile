FROM openjdk:8
MAINTAINER wang.t "wang.t.nice.google.com"


COPY activemq /opt/activemq
RUN chmod +x /opt/activemq/bin/activemq
# Expose all port
EXPOSE 8161
EXPOSE 61616
EXPOSE 5672
EXPOSE 61613
EXPOSE 1883
EXPOSE 61614
WORKDIR /opt/activemq

CMD ["/bin/sh", "-c", "/opt/activemq/bin/activemq console"]
