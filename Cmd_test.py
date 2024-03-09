import socket
import os
import time
import subprocess
import traceback
import tempfile

kafka_path = "kafka_2.12-2.4.0"
# 启动zookeeper
cmd_zookeeper_start = "bin\windows\zookeeper-server-start.bat config\zookeeper.properties"
# 启动kafka
cmd_kafka_start = "bin\windows\kafka-server-start.bat config\server.properties"
# 停止zookeeper
cmd_zookeeper_stop = "bin\windows\kafka-server-stop.bat"
# 停止kafka
cmd_kafka_stop = "bin\windows\zookeeper-server-stop.bat"


def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP


def kafka_start():
    os.chdir(kafka_path)
    print(os.getcwd())
    subprocess.Popen(cmd_zookeeper_start, shell=True)
    time.sleep(3)
    subprocess.Popen(cmd_kafka_start, shell=True)

def kafka_stop():
    os.chdir(kafka_path)
    print(os.getcwd())
    subprocess.Popen(cmd_kafka_stop, shell=True)
    time.sleep(3)
    subprocess.Popen(cmd_zookeeper_stop, shell=True)






