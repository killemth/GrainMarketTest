"""
Builds and Seeds Database Locally.

WARNING: Will Remove Existing Database.
"""

import os
from configuration import databaseContext, databaseName, baseDirectory
from models.entity import Entity, EntityType
from models.commodity import Commodity
from models.bid import Bid
from models.inventory import Inventory
from models.distributedLock import DistributedLock

######################################################################

if os.path.exists(os.path.join(baseDirectory, databaseName)):
    os.remove(os.path.join(baseDirectory, databaseName))

databaseContext.create_all()
databaseContext.session.commit()

######################################################################

# Seed the Database with Commodities... haha?  Get it?  Nevermind, I'll leave...
COMMODITY = [
    {"CommodityName": "Soybeans", "CommodityType": "rowCrop"},
    {"CommodityName": "Corn", "CommodityType": "rowCrop"},
    {"CommodityName": "Alfalfa", "CommodityType": "forage"}
]

for commodity in COMMODITY:
    data = Commodity(
        CommodityName = commodity.get("CommodityName"),
        CommodityType = commodity.get("CommodityType")
        )

    databaseContext.session.add(data)

#-------------------------------

ENTITY = [
    {"EntityName": "John CornDoe", "EntityType": EntityType.PERSON.value},
    {"EntityName": "Wheaty McWheat", "EntityType": EntityType.PERSON.value},
    {"EntityName": "Combine McHarvesterFace", "EntityType": EntityType.PERSON.value},
    {"EntityName": "Super Evils", "EntityType": EntityType.BUSINESS.value},
    {"EntityName": "The Good Guyz", "EntityType": EntityType.BUSINESS.value}
]

for entity in ENTITY:
    data = Entity(
        EntityName = entity.get("EntityName"),
        EntityType = entity.get("EntityType")
        )

    databaseContext.session.add(data)

#-------------------------------
# *********************************

# Do it!  We need the IDs...
databaseContext.session.commit()

# *********************************
#-------------------------------

INVENTORY = [
    {
        "CommodityId": Commodity.query.filter_by(CommodityName = "Corn").one().CommodityId,
        "OwnerEntityId": Entity.query.filter_by(
                EntityName = "Super Evils"
            ).one().EntityId,
        "Quantity": 500
    },
    {
        "CommodityId": Commodity.query.filter_by(CommodityName = "Corn").one().CommodityId,
        "OwnerEntityId": Entity.query.filter_by(
                EntityName = "The Good Guyz"
            ).one().EntityId,
        "Quantity": 150
    },
    {
        "CommodityId": Commodity.query.filter_by(CommodityName = "Corn").one().CommodityId,
        "OwnerEntityId": Entity.query.filter_by(
                EntityName = "Combine McHarvesterFace"
            ).one().EntityId,
        "Quantity": 725
    }
]

for inventory in INVENTORY:
    data = Inventory(
        CommodityId = inventory.get("CommodityId"),
        OwnerEntityId = inventory.get("OwnerEntityId"),
        Quantity = inventory.get("Quantity")
        )

    databaseContext.session.add(data)

#-------------------------------

#databaseContext.session.add(ApiKey(
#        ApiKeyId = 1,
#        ApiKey = "2da30c1c-50d9-4ea6-936b-b23cbf4405fb",
#        IsLocked = False
#    ))

#-------------------------------

######################################################################

databaseContext.session.commit()
