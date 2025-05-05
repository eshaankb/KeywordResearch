import click
from keywordresearch.utils import read_file
from keywordresearch.kmeans import cluster_data
from typing import TextIO

@click.command()
@click.argument('input_file', type=click.File('r'))
def main(input_file : TextIO):
    df = read_file(input_file)
    cluster_data(df["Keyword"])

    


if __name__ == "__main__":
    main()