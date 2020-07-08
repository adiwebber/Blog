import os

class Config:
    SECRET_KEY = 'a6d4c206873961514ec69759a9b6b4f7'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI = 'postgres://fjodxbqagzmizc:e084c2485e50ee23c380c8469174c2e0eb68ae032d4d5606b0e8c03b322e79db@ec2-34-224-229-81.compute-1.amazonaws.com:5432/dfs23g430okcdn'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ['EMAIL_USER']
    MAIL_PASSWORD = os.environ['EMAIL_PASS']