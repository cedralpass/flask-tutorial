from werkzeug.serving import run_simple # werkzeug development server
import flaskrapi

#use to launch merged app for debugging.  Uses werkzeug webserver.  good for debugging only.
# simply execute python script as python run.py

print("launching werkzeug webserver with merged apps: recap+aiapi")
if __name__ == '__main__':
    run_simple('0.0.0.0', 8000, flaskrapi.create_app(), use_reloader=True, use_debugger=True, use_evalex=True)