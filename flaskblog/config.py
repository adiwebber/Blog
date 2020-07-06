import os
from boto.s3.connection import S3Connection

class Config:
    SECRET_KEY = 'a6d4c206873961514ec69759a9b6b4f7'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = S3Connection(os.environ['EMAIL_USER'])
    MAIL_PASSWORD = S3Connection(os.environ['EMAIL_PASS'])