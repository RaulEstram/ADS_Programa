from tkinter import *


class QueriesManager:

    @staticmethod
    def createPreSqlQueries(data: dict, author: str) -> str:
        queries = ""
        for articule in data.keys():
            query = 'INSERT INTO `DatosADS` (`autores`, `title`, `pub`, `bibcode`, `doi`, `fpage`, `lpage`, `volumen`, `year`) VALUES ("{autor}", "{title}", "{pub}", "{bibcode}", "{doi}", "{fpage}", "{lpage}", "{volume}", "{year}");\n'.format(
                autor=author,
                title=data[articule]['title'],
                pub=data[articule]['pub'],
                bibcode=data[articule]['bibcode'],
                doi=data[articule]['doi'],
                fpage=data[articule]['page_range'].split("-")[0] if data[articule][
                                                                        'page_range'] != "Undefined" else None,
                lpage=data[articule]['page_range'].split("-")[1] if data[articule][
                                                                        'page_range'] != "Undefined" else None,
                volume=data[articule]['volume'],
                year=data[articule]['year']
            )
            queries += query
        return queries
