import click
from keywordresearch.utils import read_file
from typing import TextIO

@click.command()
@click.argument('input_file', type=click.File('r'))
def main(input_file : TextIO):
    print(type(input_file))
    df = read_file(input_file)
    print(f"there are {len(df)} rows")
    


if __name__ == "__main__":
    main()