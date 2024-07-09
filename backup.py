import os
import shutil
import datetime
import schedule
import time

source_dir = r"C:\Users\Paulo Cesar\OneDrive\Imagens\Capturas de tela"
destination_dir = r'C:\Users\Paulo Cesar\OneDrive\Imagens\Imagens da Câmera'

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f'Folder copied to: {dest_dir}')
    except FileExistsError:
        print(f'Folder already exists in: {dest_dir}')
    except Exception as e:
        print(f'Error copying folder: {e}')

schedule.every().day.at('15:53').do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)
