import pathlib
import azure.functions as func
from jinja2 import Environment, FileSystemLoader, select_autoescape

bp = func.Blueprint()

# ------------------------------------------------------------------
#  Set up Jinja2 *once* at import time.
#  We point the loader at the "templates" folder that sits next to
#  this file (you can adjust the path to suit your structure).
# ------------------------------------------------------------------
TEMPLATE_DIR = pathlib.Path(__file__).parent / "templates"
jinja_env = Environment(
    loader=FileSystemLoader(str(TEMPLATE_DIR)),
    autoescape=select_autoescape(["html", "xml"])
)

@bp.function_name("hello_page")
@bp.route(route="hello", methods=["GET"])
def hello_page(req: func.HttpRequest) -> func.HttpResponse:
    """
    GET /api/hello/<name>
    Renders an HTML page via Jinja2.
    """

    html = jinja_env.get_template("hello.html").render(name="World")

    return func.HttpResponse(
        html,
        mimetype="text/html; charset=utf-8"
    )

@bp.route(route="hello", methods=["POST"])
def hello_post(req: func.HttpRequest) -> func.HttpResponse:
    """
    POST /api/hello
    Handles form submissions from the hello.html page.
    """
    name = req.form.get("name", "World")
    html = jinja_env.get_template("hello.html").render(name=name)

    return func.HttpResponse(
        html,
        mimetype="text/html; charset=utf-8"
    )