import pandas as pd

from src.app.pipeline.transform import concat_data_frames

df_1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df_2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})


def testar_concatenacao_lista_dataframes():

    # arrange
    data_frame_list = [df_1, df_2]
    data_frame = pd.concat(data_frame_list, ignore_index=True)

    # act
    df = concat_data_frames(data_frame_list)

    assert df.shape == (4, 2)
    assert data_frame.equals(df)
    assert df.shape != (5, 2)
