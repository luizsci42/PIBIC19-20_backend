import json
from tfidf_nltk import tf_idf
from textextract import gerar_dicionario
from textextract import escrever_json


def escrever_arquivo(texto):
    with open('arquivos/saida.json', 'w', encoding='utf8') as arquivo_saida:
        saida = dict(resumo=texto)
        json.dump(saida, arquivo_saida, ensure_ascii=False)


# Dicionário com os respectívos tópicos e seus conteúdos extraídos da Wikipédia
original = gerar_dicionario()
topicos_e_resumos = []

for i in range(0, len(original)):
    # Mandamos texto por texto para ser resumido
    resumo = tf_idf(original[i][1])
    # Criamos uma lista de tuplas com os tópicos e seus respectivos conteúdos
    topicos_e_resumos.append((original[i][0], resumo))

escrever_json(topicos_e_resumos)
