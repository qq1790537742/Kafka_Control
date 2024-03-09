from Common.communication.CommunicaitonManagement import CommunicationManagement
from Common.event.EventManager import EventManager
# 模块一
send_topic = "Module1"
receive_topic = "Module2"


class contest:
    def __init__(self):
        self.event_manager = EventManager()
        self.conManagement = CommunicationManagement(self.event_manager, "Module2", "Module1")



    def run(self):
        self.conManagement.receive_exchange_message_thread.start()
        self.conManagement.operator_exchange_message_thread.start()
