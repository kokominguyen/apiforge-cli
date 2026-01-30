from jinja2 import Environment, PackageLoader, select_autoescape


def generate_client(endpoints: list[dict], class_name: str) -> str:
    env = Environment(
        loader=PackageLoader("apiforge", "templates"),
        autoescape=select_autoescape()
    )
    template = env.get_template("client.j2")
    return template.render(
        class_name=class_name,
        endpoints=endpoints
    )
