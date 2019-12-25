from sqlalchemy import create_engine, Table, Column,Integer, String,Float, exc,orm, MetaData
from sqlalchemy.ext.declarative import declarative_base

mysql = 'mysql+pymysql://root:123456@127.0.0.1:3306/EmicallDev_system?charset=utf8'

engine = create_engine(mysql, encoding='utf-8')
engine.connect()

metadata  = MetaData(engine)
person = Table('zt_users',metadata, Column('id', Integer, primary_key = True),
                                    Column("name", String(64)),
                                    Column("age",Float))
print(type(person))
print(person)

metadata.create_all(engine)

Session = orm.sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
class User(Base):
    __tablename__ = 'zt_users'   # tablename
    id = 0
    age = 1
    name =1

#insert user

user = User(id=1,name='zt', age=27.1)
session.add(user)
session.commit()  #must call commit  for the changes to take effect.

#get
query = session.query(User).filter(User.name == 'zt')
print(query) # query is iterator

for it in query:
    print(it.name)

#update
user.name  = 'Mike'
session.commit()

#get
query = session.query(User).filter(User.name == 'Mike')
print(query) # query is iterator

for it in query:
    print(it.name)

#delete user

session.delete(user)
session.commit()

session.close()






