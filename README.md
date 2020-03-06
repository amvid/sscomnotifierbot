# ss.com notifier bot

### Installation

1. git clone https://github.com/vfilipovsky/sscomnotifierbot.git && cd sscomnotifierbot
2. cp .env.dist .env
3. cp storage.sqlite.dist storage.sqlite
3. put [telegram bot token](https://core.telegram.org/bots) to .env
4. put interval to .env (in seconds)
5. pip install -r requirements.txt


### Usage
Start bot by running:

```python notifier_bot.py```

Add valid link:

```/add name=a4 uri=/lv/transport/cars/audi/a4/```

Delete link:

```/del a4```

Get updates foreach link you have added:

```/notify```

List of your added links:

```/links```


### Or just add my current bot in telegram
```@sscomnotifierbot```

### TODO:
- [x] use sqlite instead of memory
- run_repeating(callback, interval) from [telegram.ext.JobQueue](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.jobqueue.html) with given interval by user
- support multiple pages if last_ad_id not on first page
- filters