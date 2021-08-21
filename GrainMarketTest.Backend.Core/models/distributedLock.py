from datetime import datetime
from sqlalchemy import UniqueConstraint
from configuration import databaseContext, serializerContext
from helpers.keyRandomizer import randomKey

######################################################################

_db = databaseContext

######################################################################

class DistributedLock(_db.Model):
    __tablename__ = "distributed-lock"

    LockId = _db.Column(_db.String(16), primary_key = True, default = randomKey)
    LockContext = _db.Column(_db.String(128), unique = True)
    LastUpdated = _db.Column(
        _db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow
    )