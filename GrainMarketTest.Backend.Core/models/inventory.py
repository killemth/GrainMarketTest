"""
Inventory Data Models and Schemas for API Output and Database.
"""

from datetime import datetime
from marshmallow import fields
from configuration import databaseContext, serializerContext
from models.commodity import Commodity, CommoditySchema

######################################################################

_db = databaseContext

######################################################################

class Inventory(_db.Model):
    """
    Represents an Entity-Bound Inventory for a Commodity.
    """
    __tablename__ = "inventory"

    InventoryId = _db.Column(_db.Integer, primary_key = True)
    CommodityId = _db.Column(_db.Integer, _db.ForeignKey("commodity.CommodityId"))
    OwnerEntityId = _db.Column(_db.Integer, _db.ForeignKey("entity.EntityId"))
    Quantity = _db.Column(_db.Integer)
    LastUpdated = _db.Column(
        _db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow
    )

class InventorySchema(serializerContext.SQLAlchemyAutoSchema):
    """
    Represents the Serializable Schema for the Model.
    """
    class Meta:
        """
        Meta Data for Marshmallow Schema Mapping.
        """
        model = Inventory
        sqla_session = _db.session
        load_instance = True

class InventorySummary():
    """
    Represents an Inventory Summary of a Commodity.
    """
    def __init__(
            self,
            commodity:Commodity,
            totalQuantity:int,
            pendingQuantity:int,
            timestamp:datetime
        ):
        self.Commodity = commodity
        self.ValidityTimestamp = timestamp
        self.TotalQuantity = totalQuantity
        self.PendingQuantity = pendingQuantity

class InventorySummarySchema(serializerContext.Schema):
    """
    Represents the Serializable Schema for the Model.
    """
    ValidityTimestamp = fields.DateTime()
    TotalQuantity = fields.Integer()
    PendingQuantity = fields.Integer()
    Commodity = fields.Nested(CommoditySchema)
