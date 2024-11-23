import os
import shutil

# 原始資料夾路徑
#source_directory = "D:\\Trianswer\\TriAnswer_Records"
#source_directory = "D:\\old data"
source_directory = "D:"
# 目標資料夾路徑
target_directory = "C:\\Jack\\Rppg_acquire_8.18\\The-rPPG-Acquiring-System-main\\TriAnswer_Records(unprocessed)"


# 檔案名稱清單
files_to_copy = ["ECG_PPG_time_step.txt", "ECG.csv", "PPG_IR.csv", "PPG_R.csv"]

# 遍歷 01-01 到 15-04 的資料夾
for i in range(38, 42):
    for j in range(1, 5):
        folder_name = f"{str(i).zfill(2)}-{str(j).zfill(2)}"
        source_path = os.path.join(source_directory, folder_name)
        target_path = os.path.join(target_directory, folder_name)
        
        # 確認來源資料夾存在
        if os.path.exists(source_path):
            # 複製每個指定的檔案
            for file_name in files_to_copy:
                src_file = os.path.join(source_path, file_name)
                tgt_file = os.path.join(target_path, file_name)
                if os.path.exists(src_file):
                    shutil.copy(src_file, tgt_file)
                    print(f"複製 {file_name} 到 {target_path}")
                else:
                    print(f"{src_file} 不存在")
        else:
            print(f"來源資料夾 {source_path} 不存在")
            
