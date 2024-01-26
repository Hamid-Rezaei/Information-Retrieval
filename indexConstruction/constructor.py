import json

from indexConstruction.inverted_index.inverted_index import InvertedIndex

PATH = "D:\Data\Docs\\University\\term7\Inforamtion Retrieval\project\search_engine\Dataset\IR_data_news_12k.json"


def constructor():
    with open(PATH, 'r') as news:
        documents = json.load(news)

    inverted_index = InvertedIndex(documents=documents)
    inverted_index.save(inverted_index, 'inverted_index.pkl')


if __name__ == "__main__":
    constructor()
    # ii: InvertedIndex = InvertedIndex.load('inverted_index.pkl', 'rb')
    # print(ii.dictionary['ها'])
