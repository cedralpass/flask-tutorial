# recap

#setup
## Init DB
Run the following command to init DB
```bash
flask --app flaskr init-db   
```

## Init dev webserver
Run the following command to run the development, builtin webserver
```bash
flask --app flaskr run --debug  
```

Run the API
```bash
flask --app flaskrapi run --debug  --port 8008
```

# Produciton
## Run the produciton gunicorn web server
Run the following command to run in produciton
```bash
gunicorn -w 4 'flaskr:create_app()' -b 127.0.0.1:8080 --access-logfile=gunicorn.http.log --error-logfile=gunicorn.error.log
```
[gunicorn settings](https://docs.gunicorn.org/en/stable/settings.html)
