import os 
import shutil
import pandas as pd
import kagglehub


def load_dataset():

    print("Carreagando dataset...")
    # Download latest version

    destination_dir = 'data'
    os.makedirs(destination_dir, exist_ok=True)
    destination_file = os.path.join(destination_dir, "Carbon_(CO2)_Emissions_by_Country.csv")

    if not os.path.exists(destination_file):
        print("Baixando dataset mais recente do Kaggle...")
        path = kagglehub.dataset_download("ravindrasinghrana/carbon-co2-emissions")
        source_file = os.path.join(path, "Carbon_(CO2)_Emissions_by_Country.csv")
        shutil.copy(source_file, destination_file)
        print("Dataset baixado e salvo em data/.")
    else:
        print("Dataset já existe em data/ - usando arquivo local.")

    df = pd.read_csv(destination_file)
    print(f"Dataset carregado com sucesso. Total de linhas e colunas {df.shape})")
    return df

if __name__ == "__main__":
    df = load_dataset()
    print(df.head())