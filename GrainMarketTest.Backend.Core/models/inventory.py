from datetime import datetime
from configuration import databaseContext, serializerContext
from models.commodity import Commodity, CommoditySchema
from marshmallow import fields

######################################################################

_db = databaseContext

######################################################################

class Inventory(_db.Model):
    __tablename__ = "inventory"

    InventoryId = _db.Column(_db.Integer, primary_key = True)
    CommodityId = _db.Column(_db.Integer, _db.ForeignKey("commodity.CommodityId"))
    OwnerEntityId = _db.Column(_db.Integer, _db.ForeignKey("entity.EntityId"))
    Quantity = _db.Column(_db.Integer)
    LastUpdated = _db.Column(
        _db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow
    )

class InventorySchema(serializerContext.SQLAlchemyAutoSchema):
    class Meta:
        model = Inventory
        sqla_session = _db.session
        load_instance = True

class InventorySummary():
    def __init__(self, commodity:Commodity, totalQuantity:int, pendingQuantity:int, timestamp:datetime):
        self.Commodity = commodity
        self.ValidityTimestamp = timestamp
        self.TotalQuantity = totalQuantity
        self.PendingQuantity = pendingQuantity

class InventorySummarySchema(serializerContext.Schema):
    ValidityTimestamp = fields.DateTime()
    TotalQuantity = fields.Integer()
    PendingQuantity = fields.Integer()
    Commodity = fields.Nested(CommoditySchema)