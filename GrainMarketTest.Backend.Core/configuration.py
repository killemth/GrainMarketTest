import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

######################################################################

baseDirectory = os.path.abspath(os.path.dirname(__file__))

# Super-Great Best-Practice Stuff Here
databaseName = "grainMarketData.db"
databaseConnectionString = f"sqlite:///{os.path.join(baseDirectory, databaseName)}"

######################################################################

# Setup our Base Application Stuff and Things
connexApplication = connexion.App(__name__, specification_dir = baseDirectory)
flaskApplication = connexApplication.app

######################################################################

# Configure SQLAlchemy ORM in Flask Application Context
flaskApplication.config["SQLALCHEMY_ECHO"] = True
flaskApplication.config["SQLALCHEMY_DATABASE_URI"] = databaseConnectionString
flaskApplication.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

######################################################################

# Set our Global Database and Mallowed-Marsk Contexts
databaseContext = SQLAlchemy(flaskApplication)
serializerContext = Marshmallow(flaskApplication)