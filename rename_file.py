import re

from pathlib import Path


def rename(p):
    print(p)
    directory = p.parent
    # change date format
    new_name = re.sub(r"^(20\d\d)(\d\d)(\d\d)", r"\1-\2-\3", p.name)
    # delete space before '€'
    new_name = re.sub(r" €", "€", new_name)
    # replace all the space by '_'
    new_name = re.sub(" ", "_", new_name)
    p.rename(Path(directory, new_name))


def main():
    """
    Script to rename my personal files
    Ex:
    20201101-Amazon-Invoice of sceen (299,34 €)
    ==>  2020-11-01-Amazon-Invoice_of_sceen_(299,34€)
    """

    target_dir = input("Please input directory path to be renamed:")
    if not Path(target_dir).is_dir():
        raise SystemExit("Wrong directory path")

    for p in Path(target_dir).glob("**/*"):
        if p.is_file():
            rename(p)


if __name__ == "__main__":
    main()
