import os
import pandas as pd

def carica_csv_da_cartella(cartella):
    # Lista per memorizzare i DataFrame
    dataframe_list = []

    # Itera attraverso tutti i file nella cartella
    for filename in os.listdir(cartella):
        # Controlla se il file è un CSV
        if filename.endswith(".csv"):
            filepath = os.path.join(cartella, filename)
            # Leggi il CSV e aggiungilo alla lista
            df = pd.read_csv(filepath)
            dataframe_list.append(df)
    
    # Unisci tutti i DataFrame in uno solo
    dataframe_completo = pd.concat(dataframe_list, ignore_index=True)
    return dataframe_completo

def salva_csv_unico(dataframe, cartella_destinazione, nome_file):
    # Assicurati che la cartella di destinazione esista, altrimenti creala
    if not os.path.exists(cartella_destinazione):
        os.makedirs(cartella_destinazione)
    
    # Costruisci il percorso completo del file di output
    filepath = os.path.join(cartella_destinazione, nome_file)
    
    # Salva il DataFrame in un file CSV
    dataframe.to_csv(filepath, index=False)

# Esempio di utilizzo
cartella = r"C:\Users\zanot\Desktop\Tesi Aziende\Aida-Dataset\Aida-Dataset\parsed_aida_v0\by_years"
dataframe_unito = carica_csv_da_cartella(cartella)

# Specifica la cartella di destinazione e il nome del file di output
cartella_destinazione = r"C:\Users\zanot\Desktop\Tesi Aziende\Output"
nome_file = "combined_dataset.csv"

# Salva il DataFrame combinato
salva_csv_unico(dataframe_unito, cartella_destinazione, nome_file)

print(f"File combinato salvato in: {os.path.join(cartella_destinazione, nome_file)}")
print(dataframe_unito)

