import pandas as pd
import numpy as np
from scipy.signal import firwin,filtfilt
import matplotlib.pyplot as plt
import os

main_directory = "C:\\Jack\\Rppg_acquire_8.18\\The-rPPG-Acquiring-System-main\\TriAnswer_Records(processed)"

#datatype = "Neurokit"

def Get_ppg_sequence(i,j, datatype):
    folder_name = f"{str(i).zfill(2)}-{str(j).zfill(2)}"
    file_path = os.path.join(main_directory, folder_name, "PPG_processed.csv")
    ppg_data_frame = pd.read_csv(file_path)
    ppg_sequence = ppg_data_frame[datatype]
    return ppg_sequence.to_numpy()

def Save_ppg_dataframe(four_stage_ppg_df, i, datatype):  # R : Remove outliers F : Filtering 1 : intitial 2 : final
    serial_number = f"{str(i).zfill(2)}"
    main_directory = "C:\\Jack\\Rppg_acquire_8.18\\The-rPPG-Acquiring-System-main\\TriAnswer_Records(processed)"
    sub_directory = datatype + "_process"
    output_file_path = os.path.join(main_directory, sub_directory, serial_number + "_PPG.csv")
    four_stage_ppg_df.to_csv(output_file_path, index=False)
    
    
    
def Retrieve_tester_list():
    # 生成範圍1到15的數字，排除7和10
    range_1_to_15 = np.setdiff1d(np.arange(1,32), [7, 10, 19])
    # 生成範圍51到58的數字
    range_51_to_58 = np.arange(51, 59)
    # 合併兩個範圍
    result = np.concatenate((range_1_to_15, range_51_to_58))
    #return result
    return [38,39,40,41]

    
def Combine_four_stage_ppg(datatype):
    for i in Retrieve_tester_list():   # 1 16,   51, 59
        if i == 7 or i == 10: continue
        first_rest, psycho_pressure, second_rest, physic_pressure = \
            Get_ppg_sequence(i, 1, datatype), Get_ppg_sequence(i, 2, datatype), \
                Get_ppg_sequence(i, 3, datatype), Get_ppg_sequence(i, 4, datatype)
        if i%2==0: 
            psycho_pressure, physic_pressure = physic_pressure, psycho_pressure
        
        print(i)
        print(first_rest.shape)
        print(psycho_pressure.shape)
        print(second_rest.shape)
        print(physic_pressure.shape)
        
        
        four_stage_ppg_df = pd.DataFrame({
            "First_rest": first_rest,
            "Psycho": psycho_pressure,
            "Second_rest": second_rest,
            "Physic": physic_pressure
        })
        Save_ppg_dataframe(four_stage_ppg_df, i, datatype)
        print(datatype + "  " + f"{str(i).zfill(2)}")
        
        
        
datatype_list = ["Neurokit","FR1","FR2","RF1","RF2"]
for datatype in datatype_list:
    Combine_four_stage_ppg(datatype)
    
    
    
    

    
