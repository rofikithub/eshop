from tkinter import messagebox

from view.licenses import LicensesView


def licenses(self) -> str:
    key = '123456789'
    if key == '123456789':
        return "Active"
    elif key == '987654321':
        return "Inactive"
    else:
        return "Empty"
