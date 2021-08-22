"""
Inventory Helper Methods.
"""

from sqlalchemy import func
from models.inventory import Inventory
from models.bid import Bid, BidState

def lookupCurrentQuantity(commodityId:int):
    """
    Use to Lookup the Currenty Volume/Quantity of a Commodity.

    :returns:       Current Total Volume.
    """
    query = Inventory.query.with_entities(
            func.sum(Inventory.Quantity).label("quantity")
        ).filter_by(
            CommodityId = commodityId
        ).first()

    return query.quantity or 0

def lookupPendingQuantity(commodityId:int):
    """
    Use to Lookup the Currenty Pending-Bid Volume/Quantity of a Commodity.

    :returns:       Current Total Volume in Pending Bids.
    """
    query = Bid.query.with_entities(
            func.sum(Bid.Quantity).label("quantity")
        ).filter_by(
            CommodityId = commodityId,
            BidState = BidState.PENDING.value
        ).first()

    return query.quantity or 0

# TODO: Make more efficient; execute from one DB command, instead of x2 round-trips
def calculateAvailableQuantity(commodityId:int):
    """
    Use to Calculate the Available Volume/Quantity of a Commodity.

    :returns:       Current Available Volume.
    """
    return lookupCurrentQuantity(commodityId) - lookupPendingQuantity(commodityId)
