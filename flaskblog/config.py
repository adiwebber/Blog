import os
host = os.environ['HOST']
password = os.environ['DATABASE_PASS']
user = "fjodxbqagzmizc"
port = 5432
database = "dfs23g430okcdn"
class Config:
    SECRET_KEY = 'a6d4c206873961514ec69759a9b6b4f7'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ['EMAIL_USER']
    MAIL_PASSWORD = os.environ['EMAIL_PASS']
    