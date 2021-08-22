"""
Inventory Bid API Controller to Serve Web Requests.
"""

from datetime import datetime
from flask import abort
from models.commodity import Commodity
from models.inventory import InventorySummary, InventorySummarySchema
from helpers.inventory import lookupCurrentQuantity, lookupPendingQuantity

######################################################################

def getCommodityInventory(commodityId: int):
    """
    Handles requests to /api/inventory/{commodityId} by preparing an inventory summary.

    :return:        inventory summary for specified commodity.
    """
    commodity = Commodity.query.filter_by(CommodityId = commodityId).one_or_none()

    if commodity is None:
        abort(404, "Lost on the farm?  This simply isn't here...")

    #........................................

    data = InventorySummary(
        commodity,
        lookupCurrentQuantity(commodity.CommodityId),
        lookupPendingQuantity(commodity.CommodityId),
        datetime.utcnow()
        )
    
    return InventorySummarySchema().dump(data)
