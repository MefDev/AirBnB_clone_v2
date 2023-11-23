from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ
from models.base_model import Base




class DBStorage:
    """Create the mysql db engine"""
    __engine = None
    __session = None

    def __init__(self):
        """init dataabases"""
        dialect = 'mysql'
        driver = 'mysqldb'
        
        # get environment variables
        user = environ.get('HBNB_MYSQL_USER')
        password = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST')
        db = environ.get('HBNB_MYSQL_DB')
        env = environ.get('HBNB_ENV')

        # create the engine
        self.__engine = create_engine(
            f'{dialect}+{driver}://{user}:\
                {password}@{host}/{db}', pool_pre_ping=True)

        # drop all the table when the environment varieble of HBNB_ENV is test
        if (env == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retreive all the data"""

        if cls is None:
            objs = self.__session.query().all()
        else:
            if type(cls) is str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}


    def new(self, obj):
        """Add the the obj to the db"""
        self.__session.add(obj)

    def save(self):
        """Save the changes"""
        self.__session.commit()

    def delete(self, obj):
        """Delete the object"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create the session and tables"""
        Base.metadata.create_all(self.__engine)

        # create a session
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

