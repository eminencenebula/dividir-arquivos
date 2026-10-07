import os
import subprocess
import sys
from tkinter import Tk, filedialog


def selecionar_arquivo():
    # Oculta a janela principal do Tkinter
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo TXT",
        filetypes=[("Arquivos TXT", "*.txt"), ("Todos os arquivos", "*.*")],
    )

    root.destroy()
    return caminho_arquivo


def dividir_txt():
    arquivo = selecionar_arquivo()

    if not arquivo:
        print("Nenhum arquivo selecionado.")
        return

    linhas_por_arquivo = 32718

    # Cria pasta de saída no mesmo diretório do arquivo original
    pasta_origem = os.path.dirname(arquivo)
    pasta_saida = os.path.join(pasta_origem, "Saida")
    os.makedirs(pasta_saida, exist_ok=True)

    print("\nLendo arquivo...")

    # Lê o arquivo original com codificação UTF-8
    with open(arquivo, "r", encoding="utf-8", errors="ignore") as f:
        linhas = f.readlines()

    total_linhas = len(linhas)
    print(f"Total de linhas encontradas: {total_linhas}\n")

    parte = 1

    # Fatia as linhas e grava cada bloco
    for i in range(0, total_linhas, linhas_por_arquivo):
        bloco = linhas[i : i + linhas_por_arquivo]
        nome_saida = f"parte_{parte:03d}.txt"
        caminho_saida = os.path.join(pasta_saida, nome_saida)

        with open(caminho_saida, "w", encoding="utf-8") as f_out:
            f_out.writelines(bloco)

        print(f"Parte {parte:03d} criada com {len(bloco)} linhas")
        parte += 1

    total_arquivos = parte - 1

    print("\n=================================")
    print("PROCESSO CONCLUIDO")
    print("=================================")
    print(f"Arquivo original : {arquivo}")
    print(f"Total de linhas : {total_linhas}")
    print(f"Arquivos gerados : {total_arquivos}")
    print(f"Saida : {pasta_saida}")
    print("=================================\n")

    # Abre a pasta de saída no Explorer (Windows)
    if sys.platform == "win32":
        os.startfile(pasta_saida)


if __name__ == "__main__":
    dividir_txt()