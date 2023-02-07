import os

basedir = os.path.abspath(os.path.dirname(__file__)) 

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' #get secret key

    #database config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db') #if database variable defined
    SQLALCHEMY_TRACK_MODIFICATIONS = False #do not send database modification signal

    #elesticsearch config
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')


    #pagination config
    POSTS_PER_PAGE = 15

    #profile uploading director
    PROFILE_FOLDER = basedir + '/app/static/profiles/'