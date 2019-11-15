import time
import sys
import stomp

topic_name = '/topic/queue.fe.alertor.in'


conn = stomp.Connection10([('10.2.3.5', 61613)])
conn.start()
conn.connect()
conn.send(topic_name, 'I am zc')
time.sleep(2)
conn.disconnect()
