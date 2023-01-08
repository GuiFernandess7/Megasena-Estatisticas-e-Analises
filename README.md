# Megasena - Estatísticas e Análises

No site da caixa (https://asloterias.com.br/download-todos-resultados-mega-sena), é possível fazer download da planilha de todos os jogos da megasena que já ocorreram. 
Nesse programa eu utilizo a biblioteca Numpy para criar uma matriz com base na planilha.

Requisitos:
----------

Numpy:
```
pip install numpy
```

Etapas de Desenvolvimento:
---------------------------
1. Capturar dados da planilha e convertê-los em uma matrix
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
