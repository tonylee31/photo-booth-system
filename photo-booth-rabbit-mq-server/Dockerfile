FROM rabbitmq:3.13


MAINTAINER tonylee31@yahoo.com.hk


COPY source/rabbit_mq/rabbitmq.conf /etc/rabbitmq
COPY source/rabbit_mq/definitions.json /etc/rabbitmq
RUN cat /etc/rabbitmq/rabbitmq.conf


RUN set eux; \
	rabbitmq-plugins enable --offline rabbitmq_management; \
# make sure the metrics collector is re-enabled (disabled in the base image for Prometheus-style metrics by default)
	rm -f /etc/rabbitmq/conf.d/20-management_agent.disable_metrics_collector.conf; \
# grab "rabbitmqadmin" from inside the "rabbitmq_management-X.Y.Z" plugin folder
# see https://github.com/docker-library/rabbitmq/issues/207
	cp /plugins/rabbitmq_management-*/priv/www/cli/rabbitmqadmin /usr/local/bin/rabbitmqadmin; \
	[ -s /usr/local/bin/rabbitmqadmin ]; \
	chmod +x /usr/local/bin/rabbitmqadmin; \
	apt-get update; \
	apt-get install -y --no-install-recommends python3; \
	rm -rf /var/lib/apt/lists/*; \
	rabbitmqadmin --version
	
	
VOLUME /var/lib/rabbitmq


# Expore the port number
EXPOSE 5672
EXPOSE 15672


## docker run --name myrabbitmq -p 15672:15672 -p 5672:5672 -d rabbitmq:management
## docker run --name myrabbitmq -p 15672:15672 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=123 -d rabbitmq:management