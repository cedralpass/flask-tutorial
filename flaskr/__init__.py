import os

from flask import Flask, current_app
from environs import Env
from redis import Redis
import rq


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    #TODO: figure out better config
    env = Env()
    env.read_env()
    app.config['API_KEY'] = env("API_KEY")
    app.config['REDIS_URL'] = env("REDIS_URL")
    
    
   
    
    
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('flaskr-tasks', connection=app.redis)


    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    # a simple url that enques a RQ job and responds
    @app.route('/job')
    def job():
        job = launch_task(name='example', description='example', seconds=5)
        return 'Job is Executing ' + job.id + ' its status ' + job.get_status(refresh=True)
    
    from . import db
    db.init_app(app) #register the db init code

    from . import auth
    app.register_blueprint(auth.bp) #register the auth blueprint

    from . import blog
    app.register_blueprint(blog.bp) #register the blog blueprint   
    app.add_url_rule('/', endpoint='index') #create index route

    # TODO - understand args and kwargs better for dynamic params 
    def launch_task(name, description, *args, **kwargs):
        rq_job = current_app.task_queue.enqueue('flaskr.tasks.example', description=description, args=args, kwargs=kwargs)
        return rq_job

    return app

