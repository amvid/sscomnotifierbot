# ss.com notifier bot

### Installation

1. git clone https://github.com/vfilipovsky/sscomnotifierbot.git && cd sscomnotifierbot
2. cp .env.dist .env
3. put [telegram bot token](https://core.telegram.org/bots) to .env


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