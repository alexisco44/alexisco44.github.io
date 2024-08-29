import pandas as pd

def group_by_columns(dataframe, rows_groupby, cols_groupby):
    pivot_table = pd.pivot_table(
        dataframe,
        values='Consomme',
        index=rows_groupby,  # Groupement en ligne
        columns=cols_groupby,  # Groupement en colonne
        aggfunc='sum',
        margins=True,  # Ajout des totaux et sous-totaux
        margins_name='Total'
    )
    return pivot_table

# Exemple d'appel de la fonction
imputations_df = pd.DataFrame({
    'Commande': ['Commande1', 'Commande2', 'Commande1'],
    'Collaborateur': ['Alice', 'Bob', 'Alice'],
    'Periode': ['2023-01', '2023-01', '2023-02'],
    'Consomme': [10.5, 20, 15]
})

grouped_data = group_by_columns(imputations_df, ['Collaborateur'], ['Commande'])
print(grouped_data)
