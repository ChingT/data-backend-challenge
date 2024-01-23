import fitz
import matplotlib.pyplot as plt
import numpy as np
from fitz import Page
from fitz.table import Table

DPI = 150


def show_image(item, title: str = ""):
    """Display a pixmap.

    Generates an RGB Pixmap from item using a constant DPI and using matplotlib
    to show it inline of the notebook.

    Args:
        item: any PyMuPDF object having a "get_pixmap" method.
        title: a string to be used as image title
    """

    pix = item.get_pixmap(dpi=DPI)
    img = np.ndarray([pix.h, pix.w, 3], dtype=np.uint8, buffer=pix.samples_mv)
    plt.figure(dpi=DPI)
    plt.title(title)
    _ = plt.imshow(img, extent=(0, pix.w * 72 / DPI, pix.h * 72 / DPI, 0))


def draw_cells(page: Page, table: Table):
    page.draw_rect(table.bbox, color=fitz.pdfcolor["green"], width=1)
    for cell in table.header.cells:
        page.draw_rect(cell, color=fitz.pdfcolor["red"], width=0.3)
    for cell in table.cells:
        page.draw_rect(cell, color=fitz.pdfcolor["blue"], width=0.3)
