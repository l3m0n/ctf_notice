#!/usr/bin/python
# coding: utf-8

import urllib,urllib2
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def gettoken(corpid,corpsecret):
    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
    try:
        token_file = urllib2.urlopen(gettoken_url)
    except urllib2.HTTPError as e:
        print e.code
        print e.read().decode("utf8")
        sys.exit()
    token_data = token_file.read().decode('utf-8')
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    return token
 
def senddata(access_token,toparty,content):
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
    send_values = {
        "toparty":toparty,
        "msgtype":"text",
        "agentid":"1",
        "text":{
            "content":content
           },
        "safe":"0"
        }
    send_data = json.dumps(send_values, ensure_ascii=False)
    send_request = urllib2.Request(send_url, send_data)
    response = json.loads(urllib2.urlopen(send_request).read())
    print str(response)
 
def send(content):
    toparty = 2
    content = content.decode("utf-8")
    corpid = "xxxx"
    corpsecret = "xxxx"
    accesstoken = gettoken(corpid,corpsecret)
    senddata(accesstoken,toparty,content)