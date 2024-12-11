import pika
import sys
import json

def send_message(sender_id, receiver_id, message):
    """
    Sends a message to the specified receiver via RabbitMQ.

    Args:
        sender_id: Unique identifier for the sender.
        receiver_id: Unique identifier for the receiver.
        message: The message content to send.
    """
    # RabbitMQ connection parameters
    credentials = pika.PlainCredentials("guest", "guest")
    conn_params = pika.ConnectionParameters("rabbitmq", credentials=credentials)

    # Establish connection and channel
    with pika.BlockingConnection(conn_params) as connection:
        channel = connection.channel()

        # Declare exchange for chat messages
        channel.exchange_declare(
            exchange="chat-exchange",
            exchange_type="direct",
            durable=True
        )

        # Prepare the message with sender and receiver details
        msg_payload = json.dumps({
            "sender_id": sender_id,
            "message": message
        })

        # Publish the message to the receiver's queue via their routing key
        channel.basic_publish(
            exchange="chat-exchange",
            routing_key=receiver_id,  # Direct message to the receiver
            body=msg_payload,
            properties=pika.BasicProperties(content_type="application/json")
        )

        print(f"Message sent from {sender_id} to {receiver_id}: {message}")

def main():
    """
    Main entry point for the producer script.
    """
    if len(sys.argv) < 4:
        print("Usage: python producer.py <sender_id> <receiver_id> <message>")
        sys.exit(1)

    sender_id = sys.argv[1]  # Sender's unique identifier
    receiver_id = sys.argv[2]  # Receiver's unique identifier
    message = sys.argv[3]  # Message to be sent

    try:
        send_message(sender_id, receiver_id, message)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
