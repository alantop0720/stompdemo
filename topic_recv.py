import time
import sys
import stomp

topic_name = '/topic/queue.fe.alertor.in'

class MyListener(object):
    def on_error(self, headers, message):
        print('received an error %s' % message)

    def on_message(self, headers, message):
        print('received a message %s' % message)


# 官方示例的连接代码也落后了，现在分协议版本
conn = stomp.Connection10([('10.2.3.5', 61613)])
conn.set_listener('', MyListener())
conn.start()
conn.connect()
conn.subscribe(topic_name)
while 1:
    time.sleep(3)  # secs
conn.disconnect()
