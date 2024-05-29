from datetime import datetime as dt
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declared_attr

class AuditMixin(object):
    """
    Mixin para audit columns
    https://docs.sqlalchemy.org/en/20/orm/declarative_mixins.html#mixing-in-columns
    """
    @declared_attr
    def created_by(cls):
        return Column(Integer, ForeignKey('users.id', onupdate="cascade", ondelete="restrict"))

    @declared_attr
    def updated_by(cls):
        return Column(Integer, ForeignKey('users.id', onupdate="cascade", ondelete="restrict"))
    
    #Audit columns - legacy xD
    created_at = Column(DateTime, nullable=False, default=dt.now())
    updated_at = Column(DateTime, nullable=False, default=dt.now(), onupdate=dt.now())