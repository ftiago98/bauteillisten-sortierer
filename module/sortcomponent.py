import pandas as pd  
import numpy as np

def sort_component(row_counter, df_read):
    
    filt = (df_read['KZ'] == df_read.at[row_counter, 'KZ']) & (df_read['A'] == df_read.at[row_counter, 'A']) & (df_read['B'] == df_read.at[row_counter, 'B']) & (df_read['W'] == df_read.at[row_counter, 'W']) & (df_read['D'] == df_read.at[row_counter, 'D']) & (df_read['D1'] == df_read.at[row_counter, 'D1']) & (df_read['D2'] == df_read.at[row_counter, 'D2']) & (df_read['D3'] == df_read.at[row_counter, 'D3']) & (df_read['IsoArt'] == df_read.at[row_counter, 'IsoArt']) & (df_read['IsoZ'] == df_read.at[row_counter, 'IsoZ']) & (df_read['LtgTyp'] == df_read.at[row_counter, 'LtgTyp'])
    counter_lenght = 0
    counter_square_meters_isolation = 0 
    item_counter = 0

    for row in df_read.loc[filt, 'L']:
        counter_lenght += int(row)
    
    for row in df_read.loc[filt, 'IsoOf']:
        counter_square_meters_isolation += int(row)
        
    for row in df_read.loc[filt, 'Anz']:
        item_counter += int(row)

    df_sorted = []
    df1 = None
    # append both rows 
    df1 = pd.DataFrame([[df_read.at[row_counter, 'Bez'], df_read.at[row_counter, 'KZ'], df_read.at[row_counter, 'A'], df_read.at[row_counter, 'B'], df_read.at[row_counter, 'W'], df_read.at[row_counter, 'D'], df_read.at[row_counter, 'D1'], df_read.at[row_counter, 'D2'], df_read.at[row_counter, 'D3'], df_read.at[row_counter, 'IsoArt'], df_read.at[row_counter, 'IsoZ'], df_read.at[row_counter, 'LtgTyp'], item_counter, counter_lenght, counter_square_meters_isolation ]],
                columns=['Bez', 'KZ', 'A', 'B', 'W', 'D', 'D1', 'D2', 'D3', 'IsoArt', 'IsoZ', 'LtgTyp', 'Stk.', 'L', 'Isom²'])

    df_sorted = pd.concat([df1])
    
    return df_sorted