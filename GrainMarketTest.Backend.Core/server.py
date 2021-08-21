import os
from flask import render_template
import configuration

######################################################################

connexApplication = configuration.connexApplication
connexApplication.add_api("swagger.yml")

######################################################################

@connexApplication.route("/")
def default():
    """
    This function just responds to the browser URL
    localhost:5000/
    """
    return render_template("default.html")


if __name__ == "__main__":
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    connexApplication.run(host = HOST, port = PORT, debug = True)
