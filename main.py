import re

import fitz
import pandas as pd
from fitz import Document, Page
from fitz.table import Table, TableFinder

VERTICAL_LINES_EVEN = [
    28.34600067138672,
    365.66900634765625,
    450.70851135253906,
    484.72450256347656,
    544.2520141601562,
    599.4709167480469,
    654.7124481201172,
    709.9311370849609,
]
VERTICAL_LINES_ODD = [
    39.685001373291016,
    377.00799560546875,
    462.0469970703125,
    496.06298828125,
    555.5908203125,
    610.8094482421875,
    666.0281982421875,
    721.2471618652344,
]
HORIZONTAL_LINES = [500]

COLUMNS = [
    "description",
    "",
    "code",
    "Preis",
    "EQS 350",
    "EQS 450+",
    "EQS 580 4MATIC",
    "Mercedes-AMG EQS 53 4MATIC+",
]


def get_dataframes_from_doc(doc_path: str) -> pd.DataFrame:
    """Main function to extract table data from the specified PDF document."""

    doc = fitz.open(doc_path)

    serienausstattungen_df = pd.concat(
        [get_dataframe_from_page(doc, page_number) for page_number in range(7, 18)],
        ignore_index=True,
    )
    return serienausstattungen_df


def get_dataframe_from_page(doc: Document, page_number: int) -> pd.DataFrame:
    """Extract table data from a specified page."""

    page = doc[page_number - 1]
    tables = find_tables_from_page(page)
    return pd.concat(
        [get_dataframe_from_table(table) for table in tables], ignore_index=True
    )


def find_tables_from_page(page: Page) -> TableFinder:
    """Find tables from a specified page."""

    vertical_lines = VERTICAL_LINES_EVEN if page.number % 2 == 0 else VERTICAL_LINES_ODD
    return page.find_tables(
        vertical_lines=vertical_lines, horizontal_lines=HORIZONTAL_LINES
    )


def get_dataframe_from_table(table: Table) -> pd.DataFrame:
    """Extract desired data from a specified table."""

    df = table.to_pandas()
    df.columns = COLUMNS
    df = df[df.code.notna() & (df.code != "")]
    selected_col_index = [2, 4, 5, 6, 7]
    new_df = df[[COLUMNS[i] for i in selected_col_index]].copy()

    keywords = ["Nicht mit", "Nur mit", "Enthält"]
    for keyword in keywords:
        new_df[keyword] = df.description.apply(lambda x: search_code(x, keyword))

    return new_df


def search_code(string: str, keyword: str) -> list[str]:
    """Search for codes in a string based on a specified keyword."""

    pattern = re.compile(r"\((\w+)\)")
    if re.search(keyword, string, flags=re.IGNORECASE):
        return pattern.findall(string)
    return []


if __name__ == "__main__":
    get_dataframes_from_doc(doc_path="./Mercedes-Benz-EQS.pdf")
