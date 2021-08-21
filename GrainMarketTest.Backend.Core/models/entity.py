from enum import Enum
from datetime import datetime
from configuration import databaseContext, serializerContext

######################################################################

_db = databaseContext

######################################################################

class Entity(_db.Model):
    __tablename__ = "entity"

    EntityId = _db.Column(_db.Integer, primary_key = True)
    EntityName = _db.Column(_db.String(32))
    EntityType = _db.Column(_db.Integer)
    LastUpdated = _db.Column(
        _db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow
    )

class EntitySchema(serializerContext.SQLAlchemyAutoSchema):
    class Meta:
        model = Entity
        sqla_session = _db.session
        load_instance = True

#-------------------------------

class EntityType(Enum):
    PERSON = 1
    BUSINESS = 2