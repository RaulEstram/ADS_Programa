from tkinter.filedialog import asksaveasfile


class FilesManagger:

    @staticmethod
    def saveDictAsCsvFile(data: dict):
        save = asksaveasfile(title="Guardar archivo",
                             filetypes=(("Guardar como CSV", ".csv"), ("Guardar como txt", ".txt")),
                             defaultextension=".csv")
        file_data = ""
        try:
            columns = data[0].keys()
            for item in columns:
                file_data += item + ", "
            file_data += "\n"
            for element in range(len(data)):
                for item in columns:
                    file_data += data[element][item].replace(",", ";") + ","
                file_data += "\n"
            print(file_data)
            save.write(file_data)
            save.close()
        except AttributeError:
            pass
        except KeyError:
            pass
