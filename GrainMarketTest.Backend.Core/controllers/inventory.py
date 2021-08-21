from datetime import datetime
from flask import make_response, abort
from configuration import databaseContext
from models.commodity import Commodity, CommoditySchema
from models.inventory import Inventory, InventorySummary, InventorySummarySchema
from models.bid import Bid
from helpers.inventory import *

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