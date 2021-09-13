from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('application'),
    autoescape=select_autoescape()
)

