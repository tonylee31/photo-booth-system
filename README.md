### ********** For Development : Begin ********** ###

# Deploy Rabbit MQ
- Docker Build (RabbitMQ)<br />
docker build -t tonylee31/photo-booth-rabbit-mq-server:0.0.1 .

- Push Image to Docker Hub (RabbitMQ)<br />
docker push tonylee31/photo-booth-rabbit-mq-server:0.0.1

- Run the Docker (RabbitMQ)<br />
docker run --name photo-booth-mq -p 15672:15672 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=Abcd#1234 -d tonylee31/photo-booth-rabbit-mq-server:0.0.1 

# Deploy CUPS Server
- Docker Build (CUPS)<br />
docker build -t tonylee31/photo-booth-cups-server:0.0.1 .

- Push Image to Docker Hub (CUPS)<br />
docker push tonylee31/photo-booth-cups-server:0.0.1

- Run the Docker (CUPS)<br />
docker run --name photo-booth-cups -p 631:631 -d tonylee31/photo-booth-cups-server:0.0.1

# Deploy Springboot API
- Docker Build (Springboot API)<br />
docker build -t tonylee31/photo-booth-api:0.0.1 .

- Push Image to Docker Hub (Springboot API)<br />
docker push tonylee31/photo-booth-api:0.0.1

- Run the Docker (Springboot API)<br />
docker run --name photo-booth-api -p 8080:8080 -d tonylee31/photo-booth-api:0.0.1

### ********** For Development : End ********** ### 





### ********** For Operation : Begin ********** ### 

- Start containers<br />
docker-compose up -d

- Stop containers<br />
docker-compose stop

- Link<br />
Springboot : http://localhost:8080/<br />
RabbitMQ : http://localhost:15672/ (admin / 123456)<br />
CUPS : http://localhost:631/ (admin / 123456)<br />

- Test MQ<br />
Trigger Event to MQ: py _program/mq_producer.py<br />
Receive Event from MQ: py _program/mq_consumer.py<br />

### ********** For Operation : End ********** ### 


