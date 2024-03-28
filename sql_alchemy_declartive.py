# SQL Alchemy Declarative way

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URL ='mysql://root:root@localhost:3306/pdbc'

ENG = create_engine(DB_URL)

Base = declarative_base()

class Post(Base):
    __tablename__ = 'mypost'
    id = Column(Integer, primary_key = True)
    title = Column(String(20))
    blog = Column(String(255))
    likes = Column(Integer)


Base.metadata.create_all(ENG)
print('table created')


Session = sessionmaker(bind=ENG)
sess = Session()

p1 = Post(id=101,title="title1",blog="body 1",likes=10)
sess.add(p1)
sess.commit()
#sess.close()















