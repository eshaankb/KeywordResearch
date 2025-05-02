import click
import pandas as pd

@click.command()
@click.argument("maining")
def main(maining):
    click.echo(f"this cli is {maining} made by click")

if __name__ == "__main__":
    main()