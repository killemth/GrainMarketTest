"""
Commodity Bid Data Models and Schemas for API Output and Database.
"""

from enum import Enum
from datetime import datetime
from configuration import databaseContext, serializerContext
from helpers.keyRandomizer import randomKey
from models.entity import Entity

######################################################################

_db = databaseContext

######################################################################

class Bid(_db.Model):
    """
    Represents a Bid, bound to a Commodity and an Entity.
    """
    __tablename__ = "bid"

    BidId = _db.Column(_db.String(16), primary_key = True, default = randomKey)
    CommodityId = _db.Column(_db.Integer, _db.ForeignKey("commodity.CommodityId"))
    BuyerEntityId = _db.Column(_db.Integer, _db.ForeignKey(Entity.EntityId), nullable = True)
    SellerEntityId = _db.Column(_db.Integer, _db.ForeignKey(Entity.EntityId), nullable = True)
    InitiatedByBuyer = _db.Column(_db.Boolean)
    BidState = _db.Column(_db.Integer)
    Quantity = _db.Column(_db.Integer)
    LastUpdated = _db.Column(
        _db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow
    )

class BidSchema(serializerContext.SQLAlchemyAutoSchema):
    """
    Represents the Serializable Schema for the Model.
    """
    class Meta:
        """
        Meta Data for Marshmallow Schema Mapping.
        """
        model = Bid
        sqla_session = _db.session
        load_instance = True

#-------------------------------

class BidState(Enum):
    """
    Identifies the State Binding for a Bid.
    """
    EXPIRED = 0
    PENDING = 1
    DECLINED = 2
    ACCEPTED = 3
