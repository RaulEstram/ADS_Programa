import json

import requests


class ADS:

    # Constructor
    def __init__(self, token: str = "TnEWAPDi8n5R3taijqXleJDTZ5LNDr2LMJjOOsec"):
        self._token = token

    # Funcion para realizar la peticion al ADS y que regrese la informacion para el usuario
    def getStrData(self, key: str) -> str:
        response = requests.get(
            "https://api.adsabs.harvard.edu/v1/search/query?"
            "q={key}&rows=50&fl=author,title,pub,bibcode,doi,volume,year,page_range,links_data"
            "&sort=date desc".format(
                key=key), headers={'Authorization': 'Bearer ' + self._token}
        )
        data = self._getStrAllArticles(response.json())
        return data

    # Funcion para realizar la peticion al ADS y que regrese un dict con la informacion para su posterior uso
    def getDictData(self, key: str) -> dict:
        response = requests.get(
            "https://api.adsabs.harvard.edu/v1/search/query?"
            "q={key}&rows=50&fl=author,title,pub,bibcode,doi,volume,year,page_range,links_data"
            "&sort=date desc".format(
                key=key), headers={'Authorization': 'Bearer ' + self._token}
        )
        data = self._getCleanDictWithAllArticles(response.json())
        return data

    """
    Funcion para regresar un Dict limpio de un Articulo, es el complemento de otras funciones

    Se le tien que pasar como argumento la parte "semi limpia" del dict que regresa la peticion.
    """

    @staticmethod
    def _getCleanDataByArticle(data: dict) -> dict:
        keys = data.keys()
        return {
            'authors': "".join(map(str, data['author'])),
            'title': data['title'][0],
            'pub': data['pub'],
            'url': "url",
            'bibcode': data['bibcode'],
            'doi': data['doi'][0],
            'page_range': data['page_range'] if 'page_range' in keys else "Undefined",
            'volume': data['volume'],
            'year': data['year'],
        }

    """
    Funcion para mostrar resultados al usuario final

    Se le tiene que pasar como argumento la peticion cruda.
    """

    def _getStrAllArticles(self, data: dict) -> str:
        # resultado que vamos a regresar
        result = ""
        # for para iterar todos los elementos obtenidos por la peticion api
        for element in data['response']['docs']:

            url_list = ""
            authors_list = ""
            dic_data = self._getCleanDataByArticle(element)

            # for para obtener los links del articulo en lista
            for elem in element["links_data"]:
                res = json.loads(elem)
                if res["type"] == "pdf":
                    url_list += "\n    • Academic pdf: {pdf}".format(pdf=res["url"])
                if res["type"] == "electr":
                    url_list += "\n    • Online: {online}".format(online=res["url"])
            url_list += "\n    • ADS: https://ui.adsabs.harvard.edu/abs/{bibcode}/abstract".format(
                bibcode=dic_data['bibcode'])

            # For para tener los nombres de los participantes del articulo en lista

            for elem in element['author']:
                authors_list += "\n    • {author}".format(author=elem)

            item = " ■ Authores: {authors}\n ■ Título del artículo: {title}\n ■ Revista: {pub}\n ■ URL: {url}\n ■ BIBCODE: {bibcode}\n ■ DOI: {doi}\n ■ Páginas: {page_range}\n ■ Volumen: {volume}\n ■ Año: {year}\n\n".format(
                authors=authors_list,
                title=dic_data['title'],
                pub=dic_data['pub'],
                url=url_list,
                bibcode=dic_data['bibcode'],
                doi=dic_data['doi'],
                page_range=dic_data['page_range'],
                volume=dic_data['volume'],
                year=dic_data['year'],
            )
            result += item + "\n\n"

        # return de la informacion ya limpia
        return result

    """
    Funcion para tener un diccionario limpio con todos los articulos de la peticion

    Se le pasa como argumento el resultado de la peticion en crudo.
    """

    def _getCleanDictWithAllArticles(self, data):
        dict_data = {}
        count = 0
        for element in data['response']['docs']:
            element_data = self._getCleanDataByArticle(element)
            dict_data[count] = element_data
            count += 1
        return dict_data
