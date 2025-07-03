import azure.functions as func
import logging
from api.bp_page import bp as page_bp

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
app.register_blueprint(page_bp)
