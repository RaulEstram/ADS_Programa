from tkinter.filedialog import asksaveasfile


class FilesManagger:

    @staticmethod
    def saveDictAsCsvFile(data: str):
        try:
            with asksaveasfile(mode="wb", title="Guardar archivo",
                               filetypes=(("Guardar como txt", ".txt"), ("ALL FILES", ".*")),
                               defaultextension=".txt") as file:
                file.write(bytes(data, "utf-8"))
                file.close()
        except AttributeError:
            pass
        except KeyError:
            pass
