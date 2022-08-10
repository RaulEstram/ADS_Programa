from tkinter.filedialog import asksaveasfile


class FilesManagger:

    @staticmethod
    def saveDictAsCsvFile(data: dict):
        columns = list(data[0].keys())
