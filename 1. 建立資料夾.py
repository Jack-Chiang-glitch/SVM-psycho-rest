import os
import numpy as np

# 設定主資料夾路徑
main_directory = "C:\\Jack\\Rppg_acquire_8.18\\The-rPPG-Acquiring-System-main\\TriAnswer_Records(processed)"
#main_directory = "C:\\Jack\\Rppg_acquire_8.18\\The-rPPG-Acquiring-System-main\\TriAnswer_Records(unprocessed)"



def Retrieve_tester_list():
    # 生成範圍1到15的數字，排除7和10
    range_1_to_15 = np.setdiff1d(np.arange(1, 35), [7, 10])
    # 生成範圍51到58的數字
    range_51_to_58 = np.arange(51, 59)
    # 合併兩個範圍
    result = np.concatenate((range_1_to_15, range_51_to_58))
    #return result
    return  [38,39,40,41]


# 建立 01-01 到 15-04 的資料夾
for i in Retrieve_tester_list():
    for j in range(1, 5):
        folder_name = f"{str(i).zfill(2)}-{str(j).zfill(2)}"
        folder_path = os.path.join(main_directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"資料夾已建立: {folder_path}")
"""
###########################
#建立 RF1_process RF2_process FR1_porcess FR2_process 資料夾
folder_name_list = ["FR1_process", "FR2_process","RF1_process","RF2_process"]
for folder_name in folder_name_list:
    folder_path = os.path.join(main_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    

"""