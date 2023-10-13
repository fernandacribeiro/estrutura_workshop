import glob  # biblioteca para listar arquivos
import os  # biblioteca para manipular arquivos e pastas
from typing import List

import pandas as pd


def extract_from_excel(path: str) -> List[pd.DataFrame]:

    """
    função para ler os arquivos da pasta data/input e retornar uma lista de dataframes

    args: path (str): caminho da pasta com os arquivos

    return: lista de dataframes
    """
    
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    data_frame_list = []

    for file in all_files:
        data_frame_list.append(pd.read_excel(file))
    
    return data_frame_list

"""
Chamada para teste do código como um arquivo principal e não como módulo
"""
if __name__ == "__main__":
    data_frame_list = extract_from_excel("estrutura_workshop\data\input")
    print(data_frame_list)