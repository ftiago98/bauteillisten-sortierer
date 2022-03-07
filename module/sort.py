import pandas as pd  
import numpy as np
from module.sortcomponent import sort_component

def sort(filepath, savepath):
    # Open file 
    df_read = pd.read_excel(filepath)

    # Fill empty fields with the value 0 -> Fields with nan generated problems when filtering
    df_read.replace(np.nan, '0', inplace=True)
    # Components with ID LT are renamed to component L
    df_read.replace({'LT': 'L'}, inplace=True)
    # Components with name Luftleitungsteil are renamed to Luftleitung
    df_read.replace({'Luftleitungsteil': 'Luftleitung'}, inplace=True)

    row_counter = 0
    df_sorted_list = []

    for index, row in df_read.iterrows():
        df_sorted = sort_component(row_counter, df_read)
        df_sorted_list.append(df_sorted)
        
        row_counter += 1
        
        
    # concat df_sorted_list to df_write
    df_write = pd.concat(df_sorted_list, ignore_index=True)

    # save new Excel file   
    df_write.drop_duplicates(subset = ['Bez', 'KZ', 'A', 'B', 'W', 'D', 'D1', 'D2', 'D3', 'IsoArt', 'IsoZ', 'LtgTyp', 'L', 'Isom²'], keep = 'first', inplace = True)
    df_write.to_excel(savepath + '/Bauteilliste_sortiert.xlsx', index=True)
    
    return 'finish'