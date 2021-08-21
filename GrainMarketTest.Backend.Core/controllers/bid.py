import logging
from flask import make_response, abort
from configuration import databaseContext
from models.commodity import Commodity
from models.bid import Bid, BidState
from models.distributedLock import DistributedLock
from helpers.inventory import *

######################################################################

_db = databaseContext

######################################################################

def postBid(commodityId, quantity):
    """
    Handles requests to /api/commodity by returning a list of all commodities.

    :return:        all commodities supported.
    """
    entityId = 1

    lockContext = f"commoditybid:{commodityId}"

    # Yeah, yeah, it is kind of pointless in this exact implementation...
    if DistributedLock.query.filter_by(LockContext = lockContext).exists() == True:
        abort(423, "BEC001|This commodity is currently suspended from bidding, try again.")

    lockHandle = None

    try:
        lockHandle = DistributedLock(LockContext = lockContext)
        _db.session.add(lockHandle)
        _db.session.commit()

        # Ensure the volume is still available.
        if calculateAvailableQuantity(commodityId) < quantity:
            return make_response("BEC002|There is not enough commodity volume to service this bid.", 200)

        # Add the new bid to the pipeline.
        _db.session.add(Bid(
            CommodityId = commodityId,
            BuyerEntityId = entityId,
            Quantity = quantity,
            InitiatedByBuyer = True,
            BidState = BidState.PENDING.value
            ))
        _db.session.commit()

    except:
        _db.session.rollback()
        logging.exception("message")
        abort(409, "BEC003|Unable to interact with the commodity at this time, try again.")

    finally:
        if lockHandle != None and lockHandle.LockId != None:
            _db.session.delete(lockHandle)
            _db.session.commit()
    
    return make_response("BEC004|The commodity bid has been filled successfully.", 200)