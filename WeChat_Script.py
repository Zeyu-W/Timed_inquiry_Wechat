# -*- coding: utf-8 -*-
import itchat
import time
import _thread
#global anger
anger = 0
def send_msg2_user(message_content):
    remarkname = 'Lover'
    friends_list = itchat.get_friends()
    for friend in friends_list:
        if friend['RemarkName'] == remarkname:
            for i in range(1):
                friend.send_msg(message_content)


@itchat.msg_register(itchat.content.TEXT)
def reply_fun(msg):
    global end_time
    global anger
    from_user_name = msg.User.RemarkName
    reply_content = msg['Text']
    reply_time = time.time() - (end_time - 2700)

    if reply_content == '泽哥不生气':
        anger_value = str(anger)
        print_content = '当前怒气值为：' + anger_value
        send_msg2_user(print_content)
    else:
        if reply_time < 120:
            if from_user_name == 'Lover':
                send_msg2_user('行，不错，还知道回复，这次原谅你')
                end_time = time.time() + 2700
            else:
                pass
        else:
            if from_user_name == 'Lover':
                send_msg2_user('你已经超过两分钟没有回复你的泽哥，怒气值已加一，回复：泽哥不生气，来查询当前怒气值')
                end_time = time.time() + 2700
                anger = anger + 1
            else:
                pass


itchat.auto_login(hotReload=True)
end_time = time.time() + 2700
_thread.start_new_thread(itchat.run, ())
send_msg2_user('快说你爱不爱我！')
#global end_time

while True:
    while -1<(time.time()-end_time)<1:
        send_msg2_user('快说你爱不爱我！')
        end_time = time.time() + 2700
        anger = anger + 1