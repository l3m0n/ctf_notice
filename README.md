# ctf_notice
ctf赛事通告

需要修改weixin.py中的

```
corpid = "xxxx"
corpsecret = "xxxx"
```

crontab -e

30 19 * * * /usr/bin/python /root/ctf_notice/ctf.py

每天下午7.30进行提醒

效果图：

![](./1.png)