import factory
# from factory_boy.alchemy import SQLAlchemyOptions
from db.cm_session import cm_session


class CMFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Factory for SQLAlchemy models. """

    # _options_class = SQLAlchemyOptions

    class Meta:
        abstract = True
        sqlalchemy_session = cm_session
