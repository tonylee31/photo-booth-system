# For Java 8, try this
FROM openjdk:8-jdk-alpine
# For Java 11, try this
#FROM adoptopenjdk/openjdk11:alpine-jre


MAINTAINER tonylee31@yahoo.com.hk


#WORKDIR /app
#COPY ["./source/springboot/app.jar", "/app/app.jar"]
COPY source/springboot/app.jar app.jar
# java -jar /app/app.jar
ENTRYPOINT ["java","-jar","/app.jar"]


# Expore the port number
EXPOSE 8080


## sudo docker run -p 8080:8080 tonylee31/photo-booth-api:0.0.1