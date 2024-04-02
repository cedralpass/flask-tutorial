import os

from flask import Flask, current_app
from environs import Env
from redis import Redis
import rq
from flaskr.config import FlaskrConfig


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    #TODO: figure out better config
    env = Env()
    env.read_env()
    
    app.config.from_mapping(
        SECRET_KEY=FlaskrConfig.SECRET_KEY,
        DATABASE=FlaskrConfig.SQLALCHEMY_DATABASE_URI,
        API_KEY=FlaskrConfig.API_KEY,
        REDIS_URL=FlaskrConfig.REDIS_URL,
    )

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
    
    # a url for showing a job_id
    @app.route('/job/<string:id>/show')
    def job_show(id):
        job = current_app.task_queue.fetch_job(job_id=id)
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

