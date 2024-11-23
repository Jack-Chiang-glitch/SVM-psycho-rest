import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import os
import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal as signal
from scipy.signal import welch
"""
i =9
datatype = "FR2"
serial_number = f"{str(i).zfill(2)}"
main_directory = "C:\\Jack\\Rppg_acquire_8.18\\The-rPPG-Acquiring-System-main\\TriAnswer_Records(processed)"
sub_directory = datatype + "_process"
file_path = os.path.join(main_directory, sub_directory, serial_number + "_PPG.csv")
ppg_dataframe = pd.read_csv(file_path)

ppg_first_rest      = ppg_dataframe["First_rest"].to_numpy()
plt.plot(ppg_first_rest[1000:1200])
"""

def Retrieve_tester_list():
    # 生成範圍1到15的數字，排除7和10
    range_1_to_15 = np.setdiff1d(np.arange(1, 16), [7, 10])
    # 生成範圍51到58的數字
    range_51_to_58 = np.arange(51, 59)
    # 合併兩個範圍
    result = np.concatenate((range_1_to_15, range_51_to_58))
    return result


def Get_ppg_data(i, datatype):

    serial_number = f"{str(i).zfill(2)}"
    main_directory = "C:\\Jack\\Rppg_acquire_8.18\\The-rPPG-Acquiring-System-main\\TriAnswer_Records(processed)"
    sub_directory = datatype + "_process"
    file_path = os.path.join(main_directory, sub_directory, serial_number + "_PPG.csv")
    ppg_dataframe = pd.read_csv(file_path)

    ppg_first_rest      = ppg_dataframe["First_rest"].to_numpy()
    ppg_psycho_stress   = ppg_dataframe["Psycho"].to_numpy()
    ppg_second_rest     = ppg_dataframe["Second_rest"].to_numpy()
    ppg_physical_stress = ppg_dataframe["Physic"].to_numpy()
    
    #return ppg_first_rest, ppg_psycho_stress, ppg_second_rest, ppg_physical_stress
    
    N = 30000
    return ppg_first_rest[:N], ppg_psycho_stress[:N], ppg_second_rest[:N], ppg_physical_stress[:N]

# 將每個 numpy array 切成 500 單位的區塊
def split_into_chunks(arr, chunk_size):
    return arr.reshape(-1, chunk_size)


def Get_Accuracy(i, datatype, chunk_size):
    ppg_first_rest, ppg_psycho_stress, ppg_second_rest, ppg_physical_stress = Get_ppg_data(i, datatype)
    X1 = split_into_chunks(ppg_first_rest, chunk_size)
    X2 = split_into_chunks(ppg_psycho_stress, chunk_size)
    # 根據時間序列分割數據
    split_index = int(X1.shape[0] * 0.8)
    # 創建標籤，0 代表 ppg_first_rest，1 代表 ppg_psycho_stress
    y1 = np.zeros(X1.shape[0])
    y2 = np.ones(X2.shape[0])
    
    
    # X1 第一次休息 X2 心理壓力
    
    X_train, X_test = np.vstack([ X1[:split_index], X2[:split_index] ]), \
                      np.vstack([ X1[split_index:], X2[split_index:] ])
                      
                      
    y_train, y_test = np.concatenate([ y1[:split_index], y2[:split_index] ]), \
                      np.concatenate([ y1[split_index:], y2[split_index:] ])
    # 打亂 y_train
    #np.random.shuffle(y_train)
    #print(y_train)
    # 創建 SVM 模型並進行訓練
    model = SVC(kernel='rbf')  # 你可以選擇不同的核函數
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'受試者 {i:02d} : accuracy {accuracy:.2f}')
    
    """
    #以下這段是隨機打亂標籤，檢查PIPILINE，如果PIPLINE正常，就應該是50%
    ##########################################################
    sum_acc = 0
    num =  500
    shuffle = True
    for j in range(num):
        if shuffle:
            np.random.shuffle(y_train)
        model.fit(X_train, y_train)
        # 預測
        y_pred = model.predict(X_test)
        # 計算準確率
        sum_acc += accuracy_score(y_test, y_pred)
    accuracy = sum_acc / num
    #print(str(i)+f' Accuracy: {accuracy:.2f}')
    print(f'受試者 {i:02d} : accuracy {accuracy:.2f}')
    return accuracy
    ##########################################################
    """
    


datatype = "FR2"

for i in Retrieve_tester_list():
    Get_Accuracy(i, datatype, chunk_size=200)

