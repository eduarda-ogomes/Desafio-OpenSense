# Desafio OpenSense

Para o desafio, decidi utilizar a biblioteca `BeautifulSoup`, pois ela é ideal para a coleta de dados em páginas `HTML`.

A princípio, minha ideia era utilizar tags `div` e `classes` para filtrar os dados dos arquivos disponibilizados. Porém, apenas um deles tinha `div` personalizadas; os demais não possuíam identificação. A partir disso, considerei padronizar os arquivos `HTML`, mas não tinha certeza se seria permitido, então segui outro método.

A solução encontrada foi utilizar o comando `search()`, que usa um objeto regex onde é possível informar uma palavra ou frase específica a ser buscada no arquivo. Dessa forma, utilizei esse comando para encontrar o CNPJ.

Para o restante das informações, identifiquei que, quando o documento possuía processos, eles estavam organizados em uma tabela com uma cor de fundo específica, diferente das demais presentes no arquivo. Então, utilizei o filtro de linhas `tr` em conjunto com o atributo `bgcolor`. Dessa forma, consegui obter todas as informações necessárias.

Por fim, para a criação da nova tabela, utilizei a biblioteca Pandas, gerando um novo arquivo `HTML` com as informações salvas na lista `todos_processos`.


Fonte de pesquisa ultilzadas durante o projeto:
- [Documentação da Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#a-regular-expression)
- [Documentação Beautiful Soup¶](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/#uma-expressao-regular-regex)
- Tutoriais no Youtube
