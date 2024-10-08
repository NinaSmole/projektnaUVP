import pandas as pd

def zdrzui(file1_path, file2_path, output_path, encoding='utf-8'):
    file1 = pd.read_csv(file1_path, encoding=encoding)
    file2 = pd.read_csv(file2_path, encoding=encoding)
    vse_knjige = pd.concat([file1, file2], ignore_index=True)
    vse_knjige.insert(0, 'id', range(1, len(vse_knjige) + 1))
    vse_knjige.to_csv(output_path, index=False, encoding=encoding)

def odstrani(input, output, column_name,):
    data_frame = pd.read_csv(input, encoding='utf-8')
    data_frame = data_frame.drop(columns=[column_name])
    data_frame.to_csv(output, index=False, encoding='utf-8')
    
odstrani('zdruzene_knjige.csv', 'koncne_knjige.csv', 'count_id')
#zdrzui('knjige.csv', 'knjige1.csv', 'zdruzene_knjige.csv')
    