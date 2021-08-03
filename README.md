> ![Logo Kinvo](https://github.com/kinvoapp/kinvo-mobile-test/blob/master/logo.svg)

# Teste para candidatos à vaga de Desenvolvedor Python (com foco em IA - inteligencia Artificial)  


## Instruções para rodar o codigo

1. criar uma env e baixar todas as bibliotecas existente no arquivo bibliotecas.txt

2. instalar o pacote de portugues do Spacy
	- python -m spacy download pt_core_news_sm
	
3. rodar o arquivo train_model.py para treinar o modelo

4. iniciar a api flask
	- CMD - set FLASK_APP=main.py
	- Bash: export FLASK_APP=main.py
	- flask run

5. para puxar e salvar as noticias, utilizar o metodo put no caminho /get_news

6. puxar as entidades das noticias das noticias salvas, utilizar o metodo GET no caminho /get_entity



## Instruções:

1. Minerar 5 notícias sobre ações da B3. Importante salvar para ser usadas no processamento de linguagem natural(PNL) posteriormente. 
	 - https://financenews.com.br/feed/
	 - https://www.ultimoinstante.com.br/feed/

2. Extrair as entidades das 5 notícias mineradas anteriormente(entity recognition).


Criar uma api com dois end-points para:

	- minerar e salvar as noticías;
	- extrair as entidades das notícias mineradas(entity recognition);


  ```

3. Após terminar seu teste submeta um pull request e aguarde seu feedback.


### Pré-requisitos:

* Utilizar Flask;
* Utilizar Python;
* Utilizar Spacy;
* Utilizar Scrapy;


* **Importante:** Usamos o mesmo teste para todos os níveis de desenvolvedor, **junior**, **pleno** ou **senior**, mas procuramos adequar nossa exigência na avaliação com cada um desses níveis sem, por exemplo, exigir excelência de quem está começando :-)

## Submissão

Para iniciar o teste, faça um fork deste repositório, crie uma branch com o seu nome e depois envie-nos o pull request.
Se você apenas clonar o repositório não vai conseguir fazer push e depois vai ser mais complicado fazer o pull request.

**Sucesso!**
