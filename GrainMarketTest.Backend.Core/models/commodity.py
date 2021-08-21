from datetime import datetime
from configuration import databaseContext, serializerContext

######################################################################

_db = databaseContext

######################################################################

class Commodity(_db.Model):
    __tablename__ = "commodity"

    CommodityId = _db.Column(_db.Integer, primary_key = True)
    CommodityName = _db.Column(_db.String(32))
    CommodityType = _db.Column(_db.String(16))
    LastUpdated = _db.Column(
        _db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow
    )

class CommoditySchema(serializerContext.SQLAlchemyAutoSchema):
    class Meta:
        model = Commodity
        sqla_session = _db.session
        load_instance = True