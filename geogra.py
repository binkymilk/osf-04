#!usr/bin/python3
import click
import pandas as pd
from geomancer.spellbook import SpellBook

@click.group()
def main():
    pass

@main.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path())
@click.option("--spellbook_path", type=click.Path(exists=True))
def extract(input_path, output_path, spellbook_path):
    df = pd.read_csv(input_path)
    spellbook = SpellBook.read_json(spellbook_path)
    df_with_features = spellbook.cast(df)
    df_with_features.to_csv(output_path, index=False)
    print(df_with_features)

@main.command()
def version():
    print("v1.0.0")

if __name__ == "__main__":
    main()
