# Megasena - Estatísticas e Análises

No site da caixa (https://asloterias.com.br/download-todos-resultados-mega-sena), é possível fazer download da planilha de todos os jogos da megasena que já ocorreram. 
Nesse programa eu utilizo a biblioteca Numpy para criar uma matriz com base na planilha. Esse programa permite consultar o número de repetições de determinada bola em uma determinada posição levando em consideração todos os jogos e gerar novas sequências baseadas nos números que mais apareceram.

Requisitos:
----------

Numpy:
```
pip install numpy
```

Etapas de Desenvolvimento:
---------------------------
1. Capturar dados da planilha e convertê-los em uma matriz
2. Filtrar valores que mais se repetem baseados em repetições máximas e mínimas para cada coluna
3. Criar novas sequências baseadas nesses filtros
4. Comparar as sequências criadas aos jogos da tabela
5. Caso a sequência gerada não esteja na matriz, a sequência é mostrada. Caso contrário, é gerada uma nova sequência

Algumas das funcionalidades:
-----------------

Visualizar o número de repetições de determinado bola em determinada coluna para todos os jogos que já aconteceram:
```
def get_repetition_by_column(matriz, column_index: int, number: int):
        repetitions = np.count_nonzero(matriz[:, column_index] == number)
        return repetitions
```

Receber um ```array``` em que cada coluna corresponde ao número de repetições de determinado número
```
def get_repetitions_by_number(matriz, number):
        repetitions = np.sum(np.equal(matriz, number), axis=0)
        return repetitions
```

Retornar uma lista de tuplas: (numero da bola: repetição desse número nos jogos anteriores)
```
def most_commom_numbers_by_column(matriz, number_range: int, column=0):
        """Retorna uma lista de tuplas: [(numero da bola: repetição desse número nos jogos anteriores)]
        Parâmetros: Os dados , a coluna (column) e a quantidade de tuplas"""

        bola_dict = {}
        numbers, repetitions = np.unique(matriz[:, column], return_counts=True)
        values = dict(zip(numbers, repetitions))
        filtered_values = Counter(values).most_common(number_range)
        bola_dict[f"Bola {column + 1}"] = filtered_values
        return bola_dict
```

jogos.json:
----------
No dicionário abaixo, as primeiras chaves correspondentes à posição da bola. As segundas chaves correspondem ao número da bola e os valores à quantidade de repetições.
```
{
   "1": {
      "1": 249,
      "2": 236,
      "4": 215,
      "3": 197,
      "5": 185
   },
   "2": {
      "16": 128,
      "13": 125,
      "10": 121,
      "11": 113,
      "18": 106
   },
   ...
```

Gráficos:
--------

#### Número de Casas X Frequência


![bola1](https://user-images.githubusercontent.com/63022500/211217615-03079949-bd45-438f-be67-f444c0fb7e10.jpg)


![bola2](https://user-images.githubusercontent.com/63022500/211217619-d607e2d7-5931-48b1-a035-960d80d2aa49.jpg)


![bola3](https://user-images.githubusercontent.com/63022500/211217622-7df9c1b3-02c3-4faf-bad7-83c13f05f66e.jpg)

![bola4](https://user-images.githubusercontent.com/63022500/211217624-f04fd27e-f4de-4f79-b9d5-0e83f151c22d.jpg)

![bola5](https://user-images.githubusercontent.com/63022500/211217630-66cfb79a-72d0-478d-8cc5-3d6e81fbe37d.jpg)

![bola6](https://user-images.githubusercontent.com/63022500/211217635-7373f250-9dac-45ea-85a1-72976ab10781.jpg)

#### Geral: Frequência de todas as bolas, independente da posição

![geral](https://user-images.githubusercontent.com/63022500/211217704-31e3d24b-8b28-4e17-8f98-5bb54d3f1af1.jpg)

