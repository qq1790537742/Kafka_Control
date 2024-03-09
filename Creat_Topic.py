import os
from EEGPlatformCommunicationModule4py.communicationModuleImplement.CommunicationInitial import CommunicationInitial
from Common.kafka.implement.KafkaInitial import KafkaInitial
from loguru import logger

producer_config_path = r"./Common/kafka/configuration/producer-config.json"

if __name__ == '__main__':
    topic_list = [
        "Module1",
        "Module2",
        "NeuracleEEG",
        "Algorithm2Stimulation"
    ]
    for topic in topic_list:
        topicCreateResult = KafkaInitial.topicCreate(topic, producer_config_path)
        logger.info("topic创建成功")

