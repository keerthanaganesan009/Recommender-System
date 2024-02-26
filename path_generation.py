import pandas as pd
def path(address):
    inp=address+".xlsx"
    excel =pd.read_excel(inp,sheet_name="Sheet1")
    data=pd.DataFrame(index=["basic-programming,Easy","basic-programming,Medium","basic-programming,Mid Hard","basic-programming,Hard","basic-programming,Very Hard",
    "conditional-statements,Easy","conditional-statements,Medium","conditional-statements,Mid Hard","conditional-statements,Hard","conditional-statements,Very Hard",
    "implementation,Easy","implementation,Medium","implementation,Mid Hard","implementation,Hard","implementation,Very Hard",
    "ad-hoc,Easy","ad-hoc,Medium","ad-hoc,Mid Hard","ad-hoc,Hard","ad-hoc,Very Hard",
    "arrays,Easy","arrays,Medium","arrays,Mid Hard","arrays,Hard","arrays,Very Hard",
    "strings,Easy","strings,Medium","strings,Mid Hard","strings,Hard","strings,Very Hard",
    "math,Easy","math,Medium","math,Mid Hard","math,Hard","math,Very Hard",
    "mathematics,Easy","mathematics,Medium","mathematics,Mid Hard","mathematics,Hard","mathematics,Very Hard",
    "sorting,Easy","sorting,Medium","sorting,Mid Hard","sorting,Hard","sorting,Very Hard",
    "binary-search,Easy","binary-search,Medium","binary-search,Mid Hard","binary-search,Hard","binary-search,Very Hard",
    "data-structures,Easy","data-structures,Medium","data-structures,Mid Hard","data-structures,Hard","data-structures,Very Hard",
    "algorithms,Easy","algorithms,Medium","algorithms,Mid Hard","algorithms,Hard","algorithms,Very Hard",
    "greedy-algorithms,Easy","greedy-algorithms,Medium","greedy-algorithms,Mid Hard","greedy-algorithms,Hard","greedy-algorithms,Very Hard",
    "dynamic-programming,Easy","dynamic-programming,Medium","dynamic-programming,Mid Hard","dynamic-programming,Hard","dynamic-programming,Very Hard",
    "graphs,Easy","graphs,Medium","graphs,Mid Hard","graphs,Hard","graphs,Very Hard",
    "segment-trees,Easy","segment-trees,Medium","segment-trees,Mid Hard","segment-trees,Hard","segment-trees,Very Hard"],columns=["basic-programming,Easy","basic-programming,Medium","basic-programming,Mid Hard","basic-programming,Hard","basic-programming,Very Hard",
    "conditional-statements,Easy","conditional-statements,Medium","conditional-statements,Mid Hard","conditional-statements,Hard","conditional-statements,Very Hard",
    "implementation,Easy","implementation,Medium","implementation,Mid Hard","implementation,Hard","implementation,Very Hard",
    "ad-hoc,Easy","ad-hoc,Medium","ad-hoc,Mid Hard","ad-hoc,Hard","ad-hoc,Very Hard",
    "arrays,Easy","arrays,Medium","arrays,Mid Hard","arrays,Hard","arrays,Very Hard",
    "strings,Easy","strings,Medium","strings,Mid Hard","strings,Hard","strings,Very Hard",
    "math,Easy","math,Medium","math,Mid Hard","math,Hard","math,Very Hard",
    "mathematics,Easy","mathematics,Medium","mathematics,Mid Hard","mathematics,Hard","mathematics,Very Hard",
    "sorting,Easy","sorting,Medium","sorting,Mid Hard","sorting,Hard","sorting,Very Hard",
    "binary-search,Easy","binary-search,Medium","binary-search,Mid Hard","binary-search,Hard","binary-search,Very Hard",
    "data-structures,Easy","data-structures,Medium","data-structures,Mid Hard","data-structures,Hard","data-structures,Very Hard",
    "algorithms,Easy","algorithms,Medium","algorithms,Mid Hard","algorithms,Hard","algorithms,Very Hard",
    "greedy-algorithms,Easy","greedy-algorithms,Medium","greedy-algorithms,Mid Hard","greedy-algorithms,Hard","greedy-algorithms,Very Hard",
    "dynamic-programming,Easy","dynamic-programming,Medium","dynamic-programming,Mid Hard","dynamic-programming,Hard","dynamic-programming,Very Hard",
    "graphs,Easy","graphs,Medium","graphs,Mid Hard","graphs,Hard","graphs,Very Hard",
    "segment-trees,Easy","segment-trees,Medium","segment-trees,Mid Hard","segment-trees,Hard","segment-trees,Very Hard"])

    data.fillna(0,inplace=True)
    prev=excel.loc[0,"Tag"]+','+excel.loc[0,"Complexity"]
    prev_username=excel.loc[0,"User Name"]
    datas=dict()
    for i in range(1,len(excel)+1):
        if i !=len(excel) and excel.loc[i,"Result"]!="Right Answer":
                continue
        if i !=len(excel) and (prev_username==excel.loc[i,"User Name"]):
            current=excel.loc[i,"Tag"]+","+excel.loc[i,"Complexity"]
            data[current][prev]=1
            prev=current
        else:
            datas[prev_username.strip()]=data
            if i ==len(excel):
                break
            prev_username=excel.loc[i,"User Name"]
            data=data*0
            prev=excel.loc[i,"Tag"]+','+excel.loc[i,"Complexity"]
            datas[prev_username.strip()]=data
    return datas
#print(path("kaviyacsa27"))