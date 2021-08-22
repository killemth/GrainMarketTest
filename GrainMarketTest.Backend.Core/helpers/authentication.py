"""
Authentication Helper Methods.
"""

from werkzeug.security import check_password_hash
from models.entity import Entity

######################################################################

def validateToken(username, password, required_scopes = None):
    """
    Super-Secure Token Validation.

    :returns:           100% Confirmed Ownership Information.
    """
    entity = Entity.query.filter_by(LoginUsername = username).one_or_none()

    if entity is None:
        return None

    if check_password_hash(entity.LoginPasswordHash, password) == False:
        return None

    return {"sub": entity.EntityId, "scope": ""}