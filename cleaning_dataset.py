import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#load data
sample_csv_path = r'C:\Users\zanot\Desktop\Tesi Aziende\Tesi\combined_dataset.csv'
df_loaded = pd.read_csv(sample_csv_path)

#display
print(df_loaded)

#PUNTO 1) colonne con n.d, s.d, nulle
nd_count = (df_loaded == 'n.d.').sum()
sd_count = (df_loaded == 's.d.').sum()
null_count = df_loaded.isnull().sum()

print("Count of 'n.d.':\n", nd_count)
print("Count of 's.d.':\n", sd_count)
print("Count of null:\n", null_count)

#Percentuale
nd_percentage_per_column = (df_loaded == 'n.d.').mean() * 100
sd_percentage_per_column = (df_loaded == 's.d.').mean() * 100
null_percentage_per_column = df_loaded.isnull().mean() * 100

print("Percentage of 'n.d.':\n", nd_percentage_per_column)
print("Percentage of 's.d.':\n", sd_percentage_per_column)
print("Percentage of null:\n", null_percentage_per_column)

#Selezionato colonne con meno le 10% della combinazione dei tre
combined_percentage_per_column = nd_percentage_per_column + sd_percentage_per_column + null_percentage_per_column
selected_columns = combined_percentage_per_column[combined_percentage_per_column < 10].index.tolist()

df_selected = df_loaded[selected_columns]

print("Selected columns DataFrame:\n", df_selected)

column_list = df_selected.columns.tolist()
print("Lista di tutte le colonne nel dataset:")
print(column_list)

#PUNTO 2) varianza 
df_selected = df_selected.apply(pd.to_numeric, errors='coerce')
variance_int64_columns = df_selected.var()
variance_int64_columns = variance_int64_columns[df_selected.dtypes == 'float64']

print("Variance", variance_int64_columns)

#varianza
varianza_colonne = np.var(df_selected, axis=0)

print("Varianza delle colonne:", varianza_colonne)

#Visualizzazione colonne con varianza più alta
variances_df = pd.DataFrame(variance_int64_columns, columns=['Variance'])
top_20_variances = variances_df.sort_values(by='Variance', ascending=False).head(20)

# Plotting Top 10
plt.figure(figsize=(20, 10))
top_20_variances['Variance'].plot(kind='bar')
plt.xlabel('Columns', fontsize=12)
plt.ylabel('Variance', fontsize=12)
plt.title('Top 20 Columns by Variance', fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#PUNTO 3) Matrice di correlazione
correlation_matrix = df_selected.corr()


# Display the correlation matrix using a heatmap
plt.figure(figsize=(25, 20))
heatmap = sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm', vmin=-1, vmax=1)
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=45, horizontalalignment='right', fontsize=10)
heatmap.set_yticklabels(heatmap.get_yticklabels(), rotation=0, fontsize=10)
plt.title('Correlation Matrix Heatmap', fontsize=18)
plt.show()

