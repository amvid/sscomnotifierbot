# ss.com notifier bot

### Installation

1. git clone https://github.com/vfilipovsky/sscomnotifierbot.git && cd sscomnotifierbot
2. cp .env.dist .env
3. put [telegram bot token](https://core.telegram.org/bots) to .env
4. put interval to .env (in seconds)
5. docker-compose up

### Docker image

```bash
TELEGRAM_TOKEN=your-token APP_ENV=prod INTERVAL=5 docker run -d --name=sscomnotifierbot -v sscomnotifierbot_vol:/usr/src/app vfilipovsky/sscomnotifierbot
```

### Usage

Add valid link:

```/add name=a4 uri=/lv/transport/cars/audi/a4/```

Delete link:

```/del a4```

List of your added links:

```/links```


### Or just add my current bot in telegram
```@sscomnotifierbot``` it will send you updates every 5 min

### TODO:
- [x] use sqlite instead of memory
- [x] run_repeating(callback, interval) from [telegram.ext.JobQueue](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.jobqueue.html)
- support multiple pages if last_ad_id not on first page
- filters