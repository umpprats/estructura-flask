from datetime import datetime as dt
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

class AuditMixin(object):
    """
    Mixin para audit columns
    https://docs.sqlalchemy.org/en/20/orm/declarative_mixins.html#mixing-in-columns
    """

    @declared_attr
    def created_by_id(cls):
        return Column(Integer, ForeignKey('users.id', name='fk_%s_created_by_id' % cls.__name__, use_alter=True), nullable=True)
    
    @declared_attr
    def created_by(cls):
        return relationship('User', primaryjoin='User.id == %s.created_by_id' % cls.__name__, remote_side='User.id')
    
    @declared_attr
    def updated_by_id(cls):
        return Column(Integer, ForeignKey('users.id', name='fk_%s_updated_by_id' % cls.__name__, use_alter=True), nullable=True)

    @declared_attr
    def updated_by(cls):
        return relationship('User', primaryjoin='User.id == %s.updated_by_id' % cls.__name__, remote_side='User.id')
    
    #Audit columns - legacy xD
    created_at = Column(DateTime, nullable=False, default=dt.now())
    updated_at = Column(DateTime, nullable=False, default=dt.now(), onupdate=dt.now())
