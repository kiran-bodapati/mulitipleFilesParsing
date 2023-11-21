import os
import click
import pandas as pd
@click.command()
@click.argument('folder_name',type=click.Path(exists=True))
@click.argument('output_name',type=str)
@click.option('--column','-c',help='Name of the column to access,reverse and compliment')


def process_files(folder_name,output_name,column):
    '''
       process CSV files in a folder and reverse and compliment a specified column.
    '''
    csv_files=[file for file in os.listdir(folder_name) if file.endswith('.csv')]
    result_df=pd.DataFrame()
    for csv_file in csv_files:
        file_path=os.path.join(folder_name,csv_file)
        df=pd.read_csv(file_path,names=[
        "Lane",
        "Sample_ID",
        "Sample_Name",
        "Sample_Plate",
        "Sample_Well",
        "Index_Plate_Well",
        "I7_Index_ID",
        "index",
        'I5_Index_ID',
        'index2',
        "Sample_Project",
        "Description",
            ],
                       skiprows=20,
                       header=0,)
        reversed_complimented_column=df[column].apply(lambda x:''.join([{"A":"T","T":"A","G":"C","C":"G"}.get(base,base) for base in x[::-1]]))
        result_df[csv_file]=reversed_complimented_column
        
    output_path=os.path.join(output_name,'reverse_complemented_results1.csv')
    result_df.to_csv(output_path,index=False)
    click.echo(f"Results saved to {output_path}")


    
process_files()
