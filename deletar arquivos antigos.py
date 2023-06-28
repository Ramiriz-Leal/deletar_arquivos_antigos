import os
import shutil
from datetime import datetime, timedelta

def delete_files(directory, days):
    cutoff_date = datetime.now() - timedelta(days=days)
    deleted_files = []  # Lista para armazenar os caminhos dos arquivos excluidos
    files = os.listdir(directory)
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))
            if modified_date < cutoff_date:
                os.remove(file_path)
                deleted_files.append(file_path)  # Adiciona o caminho do arquivo a lista de arquivos excluidos
                print(f"Arquivo excluido: {file_path}")

    return deleted_files

#Listando diretorios e excluindo os mesmos
print("excluindo arquivos anteriores a 4 dias.")
print()
print("Pasta1")
deleted_files_list = delete_files("\\\\pasta\\subpasta", 4)
print("Pasta2") 
deleted_files_list += delete_files("\\\\pasta\\subpasta", 4)


# Excluindo backup HD anterior a 10 dias
print("Excluindo backup HD anterior a 10 dias")
print()
deleted_files_list += delete_files("\\\\pasta\\pastalog", 10)

# Gerando a data e hora atual
now = datetime.now()
date_time = now.strftime("%Y-%m-%d_%H-%M-%S")

# Escrevendo o resultado no arquivo de log
log_file_path = "\\\\pasta\\pastalog\\delete_" + date_time + ".txt"
log_content = "Backups anteriores a X dias removidos!\n"
log_content += "===== Arquivos antigos de backup excluidos com sucesso! =====\n"

# Adiciona informacoes sobre os arquivos excluidos ao log_content
log_content += "Arquivos excluidos:\n"
for file_path in deleted_files_list:
    log_content += file_path + "\n"

with open(log_file_path, "w") as log_file:
    log_file.write(log_content)

print("Operacao concluida. Resultados gravados no arquivo de log:", log_file_path)