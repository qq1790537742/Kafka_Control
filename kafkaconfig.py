import json
import Cmd_test

class kafkaConfig_Change:
    def kafka_int_ip(self):
        with open("./Common/kafka/configuration/Initial-config.json", "rb") as f:
            params = json.load(f)
            ip = Cmd_test.extract_ip()
            server = ip+':'+str(60000)
            params["bootstrap.servers"] = server
        return params

    def writekafka_int_ip(self, params):
        with open("./Common/kafka/configuration/Initial-config.json", "w") as r:
            json.dump(params, r)

    def kafka_consumer_ip(self):
        with open("./Common/kafka/configuration/consumer-config.json", "rb") as f:
            params = json.load(f)
            ip = Cmd_test.extract_ip()
            server = ip + ':' + str(60000)
            params["bootstrap.servers"] = server
        return params

    def writekafka_consumer_ip(self, params):
        with open("./Common/kafka/configuration/consumer-config.json", "w") as r:
            json.dump(params, r)

    def kafka_producer_ip(self):
        with open("./Common/kafka/configuration/producer-config.json", "rb") as f:
            params = json.load(f)
            ip = Cmd_test.extract_ip()
            server = ip + ':' + str(60000)
            params["bootstrap.servers"] = server
        return params

    def writekafka_producer_ip(self, params):
        with open("./Common/kafka/configuration/producer-config.json", "w") as r:
            json.dump(params, r)
