#!/usr/bin/python
# coding: utf-8

import requests
import time
import json
import datetime
import weixin

def time2stamp(time_):
  return int(time.mktime(time.strptime(time_, "%Y-%m-%d %H:%M:%S")))

def timeup(time_, day=0):
  timeup = time_ + datetime.timedelta(days=day)
  last_time = '{Y}-{m}-{d} 00:00:00'.format(Y=timeup.year,m=timeup.month,d=timeup.day)
  return last_time

def get_data(start, finish, now_time):
  weixin_data = ""
  url = "https://ctftime.org/api/v1/events/?limit=10&start={start}&finish={finish}".format(start=start,finish=finish)
  print url
  r = requests.get(url)
  data = json.loads(r.content)
  for line in data:
    d = line['start'].split('T')[0].split('-')
    game_time = datetime.date(int(d[0]),int(d[1]),int(d[2]))
    today_time = datetime.date(now_time.year,now_time.month,now_time.day)
    day = (game_time-today_time).days
    if line['format'] == 'Jeopardy':
      if day == 1:
        add_content = "[!] One days to start..."
      if day == 3:
        add_content = "[*] Three days to start..."
      if day == 3 or day == 1:
        weixin_data += """
{add_content}
--------------
name: {name}
time: {start_time} - {end_time}
spend: {day} days {hours} hours
format: {format}
url: {url}
ctftime: {ctftime_url}
--------------
        """.format(
          add_content=add_content,
          name=line['title'],
          start_time=line['start'],
          end_time=line['finish'],
          day=line['duration']['days'],
          hours=line['duration']['hours'],
          format=line['format'],
          url=line['url'],
          ctftime_url=line['ctftime_url'])
  return weixin_data

def main():
  now_time = datetime.datetime.now()
  start = time2stamp(timeup(now_time))
  finish = time2stamp(timeup(now_time,100))
  data = get_data(start,finish,now_time)
  weixin.send(data)

if __name__ == '__main__':
  main()

