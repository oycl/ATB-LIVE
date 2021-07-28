from typing import List, Dict, Tuple
from odoo import exceptions
from base64 import b64decode
import csv
from io import StringIO


def get_csv(
    file, remove_top=1, delimiter: str = ";", encoding="utf-8-sig"
) -> Tuple[List[str], List[Dict]]:
    """Converts the uploaded file to the header and list of lines.

    The header is a list of header column name.
    The lines are represented as dicts, mapping column names to values.
    :param file: binary file to convert
    :param remove_top: how many lines of the top should to be removed
    :param delimiter: which character separates the columns
    :param encoding: csv encoding
    """
    string = ""
    try:
        string = b64decode(file).decode(encoding=encoding)
    except UnicodeDecodeError:
        pass

    if not string:
        raise exceptions.UserError(f"Could not decode file, expected {encoding}.")

    string_file = StringIO(string)
    reader = iter(csv.reader(string_file, delimiter=delimiter))

    for _ in range(0, remove_top):
        next(reader)  # skip <remove_top> lines

    header = next(reader)

    lines = []
    for row_index, row in enumerate(reader):
        if len(row) < len(header):
            raise exceptions.UserError(
                f"Line {row_index} has a different length from the header ({len(row)} < {len(header)})"
            )
        line = {}

        # handle empty rows
        if "".join(row) == "":
            continue

        for index, column in enumerate(header):
            try:
                line[column] = row[index]
            except KeyError:
                line[column] = ""
        lines.append(line)
    return header, lines
