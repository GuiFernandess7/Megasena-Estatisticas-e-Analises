def app():
    
    def load_data(filename):
        data = pd.read_excel(filename)
        matrix = data.to_numpy(copy=True)
        return matrix

    def get_repetition_by_column(matriz, column_index: int, number: int):
        """Retorna o número de repetições de determinado número em determinada coluna
        Parâmetros: Os dados, número da bola (```column_index```) e o valor da bola (```number```)"""

        repetitions = np.count_nonzero(matriz[:, column_index] == number)
        return repetitions

    def get_repetitions_by_number(matriz, number):
        """Retorna um ```array``` em que cada coluna corresponde ao número de repetições de determinado
        número (```number```)"""

        repetitions = np.sum(np.equal(matriz, number), axis=0)
        return repetitions

    def most_commom_numbers_by_column(matriz, number_range: int, column=0):
        """Retorna uma lista de tuplas: [(numero da bola, repetição desse número nos jogos anteriores)]
        Parâmetros: Os dados , a coluna (column) e a quantidade de tuplas"""

        bola_dict = {}
        numbers, repetitions = np.unique(matriz[:, column], return_counts=True)
        values = dict(zip(numbers, repetitions))
        filtered_values = Counter(values).most_common(number_range)
        bola_dict[f"Bola {column + 1}"] = filtered_values
        return bola_dict

    def get_most_repeated_numbers(matriz, frequency=5, export_data=False):
        """Retorna um dicionário com os valores das bola e o número de repetições referentes a cada bola
        Parâmetros: Os dados, as 5 bolas que possuem mais repetições, e a opção de exportar os dados em um arquivo json"""

        num_frequent = frequency
        frequency_dict = {}

        for column in range(matriz.shape[1]):
            unique, counts = np.unique(matriz[:, column], return_counts=True)
            sorted_indices = np.argsort(counts)[::-1]

            frequent_numbers = unique[sorted_indices[:num_frequent]]
            frequent_counts = counts[sorted_indices[:num_frequent]]
            frequency_dict[column+1] = {}

            for i, number in enumerate(frequent_numbers):
                frequency_dict[column+1][int(number)] = frequent_counts[i]
        
        if export_data:
            with open("jogos.json", "w") as file:
                json.dump(frequency_dict, fp=file, cls=NumpyEncoder, indent=3)

        return frequency_dict
        
    def generate_sequences(matriz, number_range=None):
        """Cria sequências (lista) com base nos dados gerados com os números que mais aparecem"""

        frequencies = get_most_repeated_numbers(matriz, number_range)
        keys = [list(valores.keys()) for _, valores in frequencies.items()]
        keys = np.array(keys)
        indices = np.random.randint(0, keys.shape[1], size=keys.shape[0])
        sequence = keys[np.arange(keys.shape[0]), indices]
        sequence = sequence.astype(int)
        sequence = sequence.tolist()
        if any((matriz[:] == np.array(sequence)).all(1)):
            return 
        else:
            return sequence

    # Wrapper function
    def main():
        data = load_data("../megasena-results.xlsx")
        num_rows, num_cols = data.shape
        menu = int(input("""O que deseja fazer?
        [1] - Acessar quantas vezes um número se repetiu (acesso por bola)
        [2] - Acessar quantas vezes um número se repetiu em cada uma das bolas
        [3] - Acessar os números que mais se repetiram em determinada bola
        [4] - Gerar uma sequência
        """))
        if menu == 1:
            numero = int(input("Selecione um valor para a bola (1 a 60): "))
            bola = int(input("Seleciona uma posição da bola (1 a 6): "))
            if bola > 6:
                print("Número Inválido")
                time.sleep(2)
                main()
            else:
                resultado = get_repetition_by_column(data, bola, numero)
                print(f"Houveram {resultado} repetições do número {numero} na posição {bola} nos últimos {num_rows} jogos")
        if menu == 2:
            numero = int(input("Selecione um valor para a bola (1 a 60): "))
            result = get_repetitions_by_number(data, numero)
            print(f"Lista de repetições do número {numero} por posição: {result}")
        if menu == 3:
            bola = int(input("Seleciona uma posição da bola (1 a 6): "))
            bola -= 1
            repeticoes = int(input("Número máximo de repetições: "))
            result = most_commom_numbers_by_column(data, repeticoes, bola)
            resultados = [r for r in result.values()]
            print(resultados)
        if menu == 4:
            seq = int(input("Quantas sequências deseja gerar? "))
            for s in range(0, seq):
                new_sequence = generate_sequences(data, 5)
                response = f"{s} - {new_sequence}"
                print(response)
        input(" ")
    
    main()
    
if __name__ == "__main__":
    import pandas as pd
    import numpy as np
    from collections import Counter
    from itertools import combinations
    from encoder import NumpyEncoder
    import json
    import time

    app()


