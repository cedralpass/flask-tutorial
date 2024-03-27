# Background Jobs

OpenAI apis are time consuming, for example ChatGPT4 takes ~14 seconds for simple document classification.  We will use a simple background job processor: [python-rq]([https://python-rq.org/])

Background can be found in this great tutorial [Background Jobs](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxii-background-jobs)

This requires redis to be installed.

## Redis Installation on Mac
to install redis, reccomend using homebrew
```brew install redis```

Then you have several ways to start it locally:

### Configure using
```/opt/homebrew/etc/redis.conf```

### As a service: 
```brew services start redis```
### In terminal

```/opt/homebrew/opt/redis/bin/redis-server```

### testing
Run the Flaskr app and execute the /job url
```http://127.0.0.1:5000/job```


