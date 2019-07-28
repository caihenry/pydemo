# encoding=utf-8
import traceback
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

# https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/#SQLAlchemy-Introduction

engine = create_engine('mysql+mysqldb://test:123456@localhost:3306/test')

connection = engine.connect()

Session = sessionmaker(bind=engine)

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


def add(session):
    ronaldo = Person('Ronaldo')
    beckham = Person('Beckham')
    try:
        session.add(ronaldo)
        session.add(beckham)
        session.commit()
    except:
        print traceback.format_exc()
        session.rollback()


def update(session, old_name, new_name):
    try:
        query = session.query(Person)
        query.filter(Person.name == old_name).update({Person.name: new_name})
        session.commit()
    except:
        session.rollback()
        print traceback.format_exc()


def delete(session, name):
    try:
        person = session.query(Person).filter(Person.name == name).one()
        session.delete(person)
        session.commit()
    except:
        session.rollback()
        print traceback.format_exc()


def query(session, name):
    try:
        person = session.query(Person).filter(Person.name == name).one()
        print ('id: {}, name: {}.'.format(person.id, person.name))
        return person
    except:
        print traceback.format_exc()


def query_all(session):
    try:
        persons = session.query(Person).all()
        for person in persons:
            print('id: {}, name: {}.'.format(person.id, person.name))
    except:
        print traceback.format_exc()


if __name__ == '__main__':
    session = Session()
    # add(session)
    # query(session, 'Ronaldo')
    # query(session, 'Henry')
    # update(session, 'Ronaldo', 'New Ronaldo')
    # update(session, 'Henry', 'New Henry')
    delete(session, 'New Ronaldo')
    query_all(session)
    session.close()
