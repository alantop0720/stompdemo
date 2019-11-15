# -*-coding:utf-8-*-
import stomp
import time

queue_name = '/queue/SampleQueue'
topic_name = '/topic/SampleTopic'
listener_name = 'SampleListener'


class SampleListener(object):
    def on_message(self, headers, message):
        print('headers: %s' % headers)
        print('message: %s' % message)



# 推送到队列queue
def send_to_queue(msg):
    conn = stomp.Connection10([('10.2.3.5', 61613)])
    conn.start()
    conn.connect()
    conn.send(queue_name, msg)
    conn.disconnect()

    conn = stomp.Connection10([('10.2.3.5', 61613)])
    conn.set_listener('', MyListener())
    conn.start()
    conn.connect()

    conn.subscribe(destination='/queue/test', id=1, ack='auto')
    # 注意，官方示例这样发送消息是有问题的
    # conn.send(body='hello,garfield! this is '.join(sys.argv[1:]), destination='/queue/test')
    conn.send(body='hello,garfield!', destination='/queue/test')

    time.sleep(2)
    conn.disconnect()


# 推送到主题
def send_to_topic(msg):
    conn = stomp.Connection10([('10.2.3.5', 61613)])
    conn.start()
    conn.connect()
    conn.send(topic_name, msg)
    conn.disconnect()


##从队列接收消息
def receive_from_queue():
    conn = stomp.Connection10([('10.2.3.5', 61613)])
    conn.set_listener(listener_name, SampleListener())
    conn.start()
    conn.connect()
    conn.subscribe(queue_name)
    time.sleep(1)  # secs
    conn.disconnect()


def receive_from_topic():
    conn = stomp.Connection10([('10.2.3.5', 61613)])
    conn.set_listener(listener_name, SampleListener())
    conn.start()
    conn.connect()
    conn.subscribe(topic_name)
    while 1:
        send_to_topic('topic')
        time.sleep(3)  # secs

    conn.disconnect()


if __name__ == '__main__':
    #send_to_queue('len 123')

    send_to_queue('hello')
    #receive_from_queue()

    #receive_from_topic()
