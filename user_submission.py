import pandas as pd
import requests
import openpyxl as xl
from bs4 import BeautifulSoup

def submission(name)->list:
    data_list=[]
    data_list.append(name)
    problem1=[]
    excel = xl.Workbook()
    sheet = excel.create_sheet()
    sheet.append(["User Name","Problem","Tag","Complexity","Result"])
    excel_file_path = "codechef_problem.xlsx"
    df = pd.read_excel(excel_file_path,sheet_name="Problemset")

    indexes =list( df["Name"])
    df.index=indexes # type: ignore  

    count=0
    try:
        for i in range(len(data_list)):
            try:
                response = requests.get(f"https://www.codechef.com/users/{data_list[i]}/")
                #print(response)
                content = BeautifulSoup(response.text, 'html.parser')

                #print(content)
                practice=content.find("section",class_="rating-data-section problems-solved")
                h3 = practice.find("h3").text
                openbrac = h3.index("(")
                closebrac = h3.index(")")
                problem=[]
                counts = h3[openbrac + 1:closebrac]
                counts = int(counts)
                if counts > 0:
                    span = practice.find("span") # type: ignore 
                    solvedprblm = span.findAll("a")# type: ignore 
                    for i in solvedprblm:
                        print("-----------------------------------")
                        prblm = (i['href'])
                        index = str(i['href']).rfind("/")
                        prblm = prblm[index + 1:]
                        print(prblm)
                        problem.append((prblm))
                #print(practice + " lm")
                #check=practice.find("strong").text.strip()
                #print(check+" lm")
                #if check !="Practice:":
                 #   continue;

                #solved=practice.find("span")
                #problem=solved.find_all("a")
            except:
                continue
            for prblm in problem:
                count+=1
                try:
                    problem1.append(prblm)
                    #print([data_list[0], prblm.text, df["Tag"][prblm.text], df['Complexity'][prblm.text],"Right Answer"])
                    sheet.append([data_list[0], prblm, df["Tag"][prblm], df['Complexity'][prblm],"Right Answer"])
                except:
                    problem1.append(prblm)
                    sheet.append([data_list[0], prblm,"data-structures", "Medium","Right Answer"])
                    #print([data_list[0], prblm.text,"data-structures","Medium","Right Answer"])

    except:
        excel.save(f"{data_list[0]}.xlsx")
        return problem1
    excel.save(f"{data_list[0]}.xlsx")
    return problem1


