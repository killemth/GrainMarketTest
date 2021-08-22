"""
Distributed-Lock Data Model.
"""

from datetime import datetime
from configuration import databaseContext
from helpers.keyRandomizer import randomKey

######################################################################

_db = databaseContext

######################################################################

class DistributedLock(_db.Model):
    """
    Represents a Distributed Lock Object and Handle.
    """
    __tablename__ = "distributed-lock"

    LockId = _db.Column(_db.String(16), primary_key = True, default = randomKey)
    LockContext = _db.Column(_db.String(128), unique = True)
    LastUpdated = _db.Column(
        _db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow
    )
