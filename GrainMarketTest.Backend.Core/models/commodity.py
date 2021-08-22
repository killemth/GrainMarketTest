"""
Commodity Data Models and Schemas for API Output and Database.
"""

from datetime import datetime
from configuration import databaseContext, serializerContext

######################################################################

_db = databaseContext

######################################################################

class Commodity(_db.Model):
    """
    Represents a Commodity within the Platform.
    """
    __tablename__ = "commodity"

    CommodityId = _db.Column(_db.Integer, primary_key = True)
    CommodityName = _db.Column(_db.String(32))
    CommodityType = _db.Column(_db.String(16))
    LastUpdated = _db.Column(
        _db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow
    )

class CommoditySchema(serializerContext.SQLAlchemyAutoSchema):
    """
    Represents the Serializable Schema for the Model.
    """
    class Meta:
        """
        Meta Data for Marshmallow Schema Mapping.
        """
        model = Commodity
        sqla_session = _db.session
        load_instance = True
