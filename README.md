# Palavras PT-BR (Português Brasileiro)
## Words PT-BR (Brazilian Portuguese)

**Palavras_PT-BR.db**: A sqlite database <br>
**Palavras_PT-BR.txt**: Text file, one word per line <br>
**Current number of words:** 1.916.706<br>
<hr>

#### Website
To access a preview of the words, visit **[https://alfredofilho.github.io/Palavras_PT-BR/](https://alfredofilho.github.io/Palavras_PT-BR/)**

#### scripts/

  - `db_create.py`: Recreates the database.
  - `db_delete.py`: Deletes words from the database.
  - `db_insert.py`: Inserts words into the database.
  - `db_select.py`: Selects data from the database.
  - `AVLTree.py`: Implements an AVL Binary Tree.
  - `example_usage_tree.py`: Contains a example of AVL Tree usage.



#### How was this file created?
- As a first base I used the [IntelliJ dictionary](https://github.com/rafaelsc/IntelliJ.Portuguese.Brazil.Dictionary)
- Web scraping to get some popular [Brazilian Portuguese verbs](https://www.conjugacao.com.br/verbos-populares/)
- [Spacy](https://spacy.io/models/pt#pt_core_news_sm) to separate all verbs in the infinitive tense 
    - Web scraping again to conjugate in all verb tenses with the website [https://www.conjugacao.com.br/](https://www.conjugacao.com.br/)
- Deleted roman numerals
- Some suspicious words that seemed wrong were deleted
- I added a few manually that I saw were missing