import os
from flask import render_template
import configuration

######################################################################

connexApplication = configuration.connexApplication
connexApplication.add_api("swagger.yml")

######################################################################

@connexApplication.route("/")
def default():
    #return redirect(url_for("/api./api_swagger_ui_index"))
    return render_template("default.html")


if __name__ == "__main__":
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    connexApplication.run(host = HOST, port = PORT, debug = True)
