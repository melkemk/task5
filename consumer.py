import pika
import json
import sys

def on_message(ch, method, properties, body):
    """
    Callback function to handle incoming messages.
    
    Args:
        ch: Channel object.
        method: Method frame with delivery details.
        properties: Properties of the message.
        body: Message body (bytes).
    """
    try:
        msg_data = json.loads(body)
        sender_id = msg_data.get("sender_id", "Unknown")
        msg = msg_data.get("message", "(No message content)")
        print(f"New message from {sender_id}: {msg}")
    except json.JSONDecodeError:
        print("Failed to decode message. Invalid JSON.")

def setup_rabbitmq_connection(user_id):
    """
    Sets up RabbitMQ connection, declares exchange, queue, and starts consuming messages.
    
    Args:
        user_id: Unique identifier for the user.
    """
    # RabbitMQ connection parameters
    credentials = pika.PlainCredentials("guest", "guest")
    conn_params = pika.ConnectionParameters(host="rabbitmq", credentials=credentials)

    # Establish connection and channel
    connection = pika.BlockingConnection(conn_params)
    channel = connection.channel()

    # Declare exchange
    channel.exchange_declare(
        exchange="chat-exchange",
        exchange_type="direct",
        durable=True
    )

    # Declare queue for the user
    queue_name = f"user-queue-{user_id}"
    channel.queue_declare(queue=queue_name, durable=True)

    # Bind the queue to the exchange with the user's routing key
    channel.queue_bind(exchange="chat-exchange", queue=queue_name, routing_key=user_id)

    print(f"Waiting for messages for user {user_id}. To exit press CTRL+C")

    # Start consuming messages
    channel.basic_consume(queue=queue_name, on_message_callback=on_message, auto_ack=True)
    channel.start_consuming()

def main():
    """
    Main entry point for the consumer script.
    """
    if len(sys.argv) < 2:
        print("Usage: python consumer.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        setup_rabbitmq_connection(user_id)
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
