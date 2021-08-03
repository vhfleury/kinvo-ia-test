import pandas as pd
import spacy


class noticias():

    def __init__(self) -> None:

        self.news = pd.read_csv('../news/noticias_extraidas.csv')
        self.nlp = spacy.load("../model/")


    def main(self):

        dados = list()

        for posicao in range(self.news.shape[0]):
            content_news = self.news.iloc[posicao]
            news = self.get_noticia(content_news)
            
            self.link = self.get_link(content_news)
            self.titulo = self.get_titulo(content_news)
            self.entidades = self.get_entidades(news)

            dados.append(self.imprime_entidades())
        return dados

    def imprime_entidades(self):

        return {"titulo":self.titulo,
                "link": self.link,
                "entidades": self.entidades}

    def get_noticia(self, content_news):
        return content_news['noticia']

    def get_link(self, content_news):
        return content_news['link']

    def get_titulo(self, content_news ):
        return content_news['titulo']

    def get_entidades(self, news):

        texto = self.nlp(news)
        enti = list()

        for entidade in texto.ents:
            enti.append({"trexo": entidade.text, "entidade": entidade.label_}) 
        
        return enti

