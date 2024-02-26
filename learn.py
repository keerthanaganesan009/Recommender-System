import pandas as pd
import math
import path_generation 
from sklearn.decomposition import PCA
def Learn(name):
    datas=path_generation.path("submission_73733")
    new_data=(path_generation.path(name))
    a_list=list(datas.keys())
    user_mat=[]
    for j in range(len(a_list)):
        wholeprod=0
        us1=0
        us2=0
        for n in range(len(new_data[name])):
            zerochecki=list(new_data[name].iloc[n])
            zerocheckj=list(datas[a_list[j]].iloc[n])
            if 1 not in zerochecki or 1 not in zerocheckj:
                continue
            for m in range(len(datas[a_list[j]])):
                wholeprod+=(new_data[name].iloc[n,m]*datas[a_list[j]].iloc[n,m])
                us1+=(new_data[name].iloc[n,m]*new_data[name].iloc[n,m])
                us2+=(datas[a_list[j]].iloc[n,m]*datas[a_list[j]].iloc[n,m])
        us1=math.sqrt(us1)
        us2=math.sqrt(us2)
        if (us1*us2)==0:
            user_mat.append(0)
            continue
        user_mat.append(wholeprod/(us1*us2))
    
    data = pd.read_excel("CosineSimiliarity.xlsx",sheet_name="Sheet1")
    pca = PCA(2)
    transform=pca.fit_transform(data)    
    user_mat=pd.DataFrame(user_mat)
    user_mat=user_mat.T
    return pca.transform(user_mat)
