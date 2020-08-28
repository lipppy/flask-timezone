import os
from flask import Flask
from application.helpers import is_number
from application.timezoneapi import TimezoneHelper

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

# Frontend / Public content
from application._frontend.routes import urls_frontend
app.register_blueprint(urls_frontend)

# Timezone API
from application._api.v1.routes import urls_api
app.register_blueprint(urls_api, url_prefix='/data/v1')
