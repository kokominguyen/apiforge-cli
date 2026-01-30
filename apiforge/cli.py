import click
from pathlib import Path
from .parser import load_spec, parse_endpoints
from .generator import generate_client


@click.command()
@click.argument("spec")
@click.option("--name", default="APIClient", help="Client class name")
@click.option("--output", default="client.py", help="Output file")
def main(spec, name, output):
    spec_data = load_spec(spec)
    endpoints = parse_endpoints(spec_data)

    code = generate_client(endpoints, name)

    out = Path(output)
    out.write_text(code, encoding="utf-8")

    click.echo(f"✅ Generated async API client → {out}")
