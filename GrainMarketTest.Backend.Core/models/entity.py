"""
Entity Data Models and Schemas for API Output and Database.
"""

from enum import Enum
from datetime import datetime
from configuration import databaseContext, serializerContext

######################################################################

_db = databaseContext

######################################################################

class Entity(_db.Model):
    """
    Represents an Entity on the Platform as a Person or Business.
    """
    __tablename__ = "entity"

    EntityId = _db.Column(_db.Integer, primary_key = True)
    EntityName = _db.Column(_db.String(32))
    EntityType = _db.Column(_db.Integer)
    LoginUsername = _db.Column(_db.String(32), unique = True, index = True)
    LoginPasswordHash = _db.Column(_db.String(128))
    LastUpdated = _db.Column(
        _db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow
    )

class EntitySchema(serializerContext.SQLAlchemyAutoSchema):
    """
    Represents the Serializable Schema for the Model.
    """
    class Meta:
        """
        Meta Data for Marshmallow Schema Mapping.
        """
        model = Entity
        sqla_session = _db.session
        load_instance = True

#-------------------------------

class EntityType(Enum):
    """
    Identifies the Type of Entity.
    """
    PERSON = 1
    BUSINESS = 2
