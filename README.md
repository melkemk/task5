# RabbitMQ Producer-Consumer Example with Docker

This project demonstrates a simple producer-consumer setup using RabbitMQ as the message broker, Python as the language for the producer and consumer scripts, and Docker to containerize the application. The producer sends messages to a specified receiver, and the consumer receives and processes those messages.

## Project Structure

- `docker-compose.yml`: Docker Compose file to orchestrate RabbitMQ, producer, and consumer services.
- `Dockerfile`: Dockerfile for building the Python environment for both producer and consumer.
- `consumer.py`: Python script that consumes messages from RabbitMQ.
- `producer.py`: Python script that produces messages to RabbitMQ.

## Main Functionality

1. **Producer**: 
   - The producer sends messages to a specified receiver.
   - The message is routed to the receiver's queue using RabbitMQ's direct exchange.
   - The producer runs continuously, sending messages with a sleep interval between each message.

2. **Consumer**: 
   - The consumer listens to messages on the queue and processes them as they arrive.
   - The consumer identifies the receiver of the message and prints it on the console.

3. **RabbitMQ**:
   - RabbitMQ is used as a message broker to facilitate communication between the producer and consumer.
   - The RabbitMQ management interface is accessible at `http://localhost:15675`.

## Docker Setup

To get started, you can use Docker and Docker Compose to set up the services. Follow the steps below to run the project in Docker containers.

### Prerequisites

- Docker
- Docker Compose

### Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>
   cd <repository_name>
2. Build and start the Docker containers:
   ```
   docker-compose up --build
   This will start three services:
      - rabbitmq: The RabbitMQ message broker.
      - producer: The Python producer script that sends messages.
      - consumer: The Python consumer script that processes received messages.
3. You can view the logs of the producer and consumer in the terminal where Docker Compose is running. The producer sends messages to user2, and the consumer listens to user2.

4. To access RabbitMQ's management interface, navigate to http://localhost:15675 in your web browser. The default login is guest with the password guest.

 To stop the service 
   - docker-compose down

