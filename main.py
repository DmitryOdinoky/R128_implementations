import pyLoudness
import os
import datetime
import pandas as pd

#loudness_stats = pyLoudness.get_loudness("D:/SW/-=Python projects=-/R128-implementations/R128_implementations/data/FILTERED_1/Metal/rty.wav")

#%%

this_time = str(datetime.datetime.now().time()).replace(':','-').replace('.','-')
this_date = str(datetime.datetime.now().date())
todays_date = this_date + '_'  + this_time

path_1 = "D:/SW/-=Python projects=-/R128-implementations/R128_implementations/data/FILTERED_2_inv/El_beats_3/"
path_2 = "D:/SW/-=Python projects=-/R128-implementations/R128_implementations/data/FILTERED_2_inv/El_beats_1/"
path_3 = "D:/SW/-=Python projects=-/R128-implementations/R128_implementations/data/FILTERED_2_inv/Metal/"


#loudness_stats = pyLoudness.get_loudness("D:/SW/-=Python projects=-/R128-implementations/R128_implementations/data/FILTERED_2_via_HD650_sim/El_beats_3/asd.wav")



var_dict = {'profile': [],
            'el_beats_3': [],
            'el_beats_1': [],
            'metal': []
            }

def calculate_loudness_match(path):
    
    files = [file for file in os.listdir(path) if file.endswith('.wav')]
    
    profiles = []
    loudness_values = []
    
    for f in files:
        
        loudness_stats = pyLoudness.get_loudness(path + f)
        profiles.append(f)
        loudness_values.append(loudness_stats['Integrated Loudness']['I'])
        
    return profiles, loudness_values
        
var_dict['profile'], var_dict['el_beats_3'] = calculate_loudness_match(path_1)
var_dict['profile'], var_dict['el_beats_1'] = calculate_loudness_match(path_2)
var_dict['profile'], var_dict['metal'] = calculate_loudness_match(path_3)

attributes = list(var_dict.keys())
index = var_dict['profile']

lst = []

for key in var_dict:
    
    lst.append(var_dict[key])
    
    
transposed = list(map(list, zip(*lst)))
        
df = pd.DataFrame(transposed ,index=index, columns=attributes)  
df = df.drop(columns=['profile'],axis=0)
  
df.to_excel(f'output_ver_{todays_date}.xlsx')    
    