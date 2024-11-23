import pandas as pd
import numpy as np
from scipy.signal import firwin,filtfilt
import matplotlib.pyplot as plt
import os

i, j = 1, 4
main_directory = "C:\\Jack\\Rppg_acquire_8.18\\The-rPPG-Acquiring-System-main\\TriAnswer_Records(processed)"
sec_main_directory = "C:\\Jack\\Rppg_acquire_8.18\\The-rPPG-Acquiring-System-main\\TriAnswer_Records(unprocessed)"

folder_name = f"{str(i).zfill(2)}-{str(j).zfill(2)}"
file_path = os.path.join(main_directory, folder_name, "PPG_processed.csv")

PPG_df = pd.read_csv(file_path)
FR2 = PPG_df["FR2"].to_numpy()
RF2 = PPG_df["RF2"].to_numpy()

file_path = os.path.join(sec_main_directory, folder_name, "PPG_R.csv")
PPG_df = pd.read_csv(file_path, header=None)
raw_PPG = PPG_df.iloc[:, 0][:30000]  # 取得第一個欄位的所有值
print(raw_PPG.shape)


plt.plot(FR2 - RF2 , label='Difference', color='red', marker='o', markersize=0.1)
plt.figure(figsize=(12, 6))


low = 20000
up =  23000
#low, up = 5000,6000


plt.plot(-raw_PPG[low:up])

import neurokit2 as nk
cleaned_ppg = nk.ppg_clean(raw_PPG[low:up], sampling_rate=100)
plt.plot(-cleaned_ppg)










# 繪製未處理的資料
plt.plot(-FR2[low:up], label='Filter Remove', color='red', linestyle='-', linewidth=1)

# 繪製處理後的資料
plt.plot(-RF2[low:up], label='Remove Filter', color='blue', linestyle='-', linewidth=1)



# 添加圖例
plt.legend()

# 顯示圖形
plt.show()
