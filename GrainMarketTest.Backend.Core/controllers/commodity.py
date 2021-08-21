from flask import make_response, abort
from configuration import databaseContext
from models.commodity import Commodity, CommoditySchema

######################################################################

def getAll():
    """
    Handles requests to /api/commodity by returning a list of all commodities.

    :return:        all commodities supported.
    """
    data = Commodity.query.order_by(Commodity.CommodityName).all()
    schema = CommoditySchema(many = True)
    
    return schema.dump(data)