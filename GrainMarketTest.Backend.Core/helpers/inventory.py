from sqlalchemy import func
from models.inventory import Inventory
from models.bid import Bid

def lookupCurrentQuantity(commodityId:int):
	query = Inventory.query.with_entities(
        func.sum(Inventory.Quantity).label("quantity")
        ).filter_by(
            CommodityId = commodityId
            ).first()

	return (query.quantity or 0)

def lookupPendingQuantity(commodityId:int):
	query = Bid.query.with_entities(
        func.sum(Bid.Quantity).label("quantity")
        ).filter_by(
            CommodityId = commodityId
            ).first()

	return (query.quantity or 0)

# TODO: Make more efficient; execute from one DB command, instead of x2 round-trips
def calculateAvailableQuantity(commodityId:int):
	return lookupCurrentQuantity(commodityId) - lookupPendingQuantity(commodityId)