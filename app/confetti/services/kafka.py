import msgpack
from django.conf import settings
from kafka import KafkaProducer
from kafka.errors import KafkaError


class MessageNotSent(Exception):
    pass


class KafkaErrors:
    MessageNotSent = MessageNotSent


class KafkaTopics:
    MAKE_RESUME_PDF = "MAKE_RESUME_PDF"


class KafkaService:
    def __init__(self):
        self.server_url = settings.KAFKA_SERVER_URL
        self.producer = None
        self.errors = KafkaErrors()
        self.topics = KafkaTopics()

    def get_producer(self):
        if not self.producer:
            self.producer = KafkaProducer(retries=3, compression_type="lz4")

        return self.producer

    def send(self, topic: str, message):
        producer = self.get_producer()

        try:
            producer.send(topic, message).get(timeout=5)
        except KafkaError:
            raise MessageNotSent("Could not send message to topic {}".format(topic))

    def send_json(self, topic: str, message: dict):
        serialized_message = msgpack.dumps(message)

        return self.send(topic, serialized_message)

    def send_resume_build_message(self, user_profile):
        pass


kafka = KafkaService()

__all__ = ["kafka"]
