import pandas as pd
import re
import user_submission
import groupfinding
def recommender(k):
    a =[]
    recommendation=[]
    new_problems=[]

    def Subsequences(arr, index, subarr):
        if index == len(arr):
            if len(subarr) == 2 or len(subarr) == 3:
                a.append(subarr)

        else:
            Subsequences(arr, index + 1, subarr)
            Subsequences(arr, index + 1, subarr + [arr[index]])
        return a

    df=pd.read_excel("Userproblems.xlsx",sheet_name="userproblems",header=None)
    df= df.fillna(0)
    prblm_df=pd.read_excel("problemset.xlsx",header=None)
    problems=list(prblm_df.iloc[:,0]) # list contains all the problems ...
    #print(df.head(5))


    user_problem={}  # contains username as key and their solved problems as list
    for i in range(len(df)):
        l=(list(df.iloc[i]))
        if 0 in l:
            index = l.index(0);
            l=l[:index]
        user_problem[l[0]]=l[1:]

    diff_level=pd.read_excel("DIFFICULTY-LEVEL.XLSX")

    diff_score={}# tags:{code:rating} --> Eg algorith:[sum2:1002]
    tags={} # problem name : tags
    for i in range(len(diff_level)):
        if diff_level["Tag"][i] not in diff_score:
            diff_score[diff_level["Tag"][i]]={diff_level["Code"][i]:diff_level["Complexity"][i]}
        else:
            temp_dict=diff_score[diff_level["Tag"][i]]
            temp_dict[diff_level["Code"][i]]=diff_level["Complexity"][i]
            diff_score[diff_level["Tag"][i]]=temp_dict
        tags[diff_level["Code"][i]]=diff_level["Tag"][i]

    #user_name=input("Enter the User_name : ")
    user_name=k
    group_df = pd.read_excel("Groups.xlsx", header=None, sheet_name="group")
    group1 = list(group_df.iloc[0, :])
    group2 = list(group_df.iloc[1, :])
    group3 = list(group_df.iloc[2, :])

    if user_name in group1:
        output = pd.read_csv("output1.txt", header=None)
    elif user_name in group2:
        output = pd.read_csv("output2.txt", header=None)
    elif user_name in group3:
        output = pd.read_csv("output3.txt", header=None)
    else:
        new_problems=user_submission.submission(user_name)
        n=str(int(groupfinding.find(user_name))+1)
        #print(f"output{n}.txt")
        output = pd.read_csv(f"output{n}.txt", header=None)
        
    HUSP = []
    for i in range(len(output)):
        l = re.findall(r'(\d+) -1', output[0][i])
        HUSP.append(l)

    HUSP_dict = {}
    for i in HUSP:
        # print(i)
        for j in i:
            HUSP_dict[int(j)] = 0

    upattern=[]
    for i in HUSP:
        upattern.append(" ".join(i))

    problem_solved=[]
    user_patt=[]
    if user_name  not in user_problem:
        user_problem[user_name]=new_problems
    problem_solved=user_problem[user_name]
    user_patt=[]
    for i in problem_solved:# i iterate users solved problem . . .
                if i not in problems:
                    problems.append(i)
                user_patt.append(problems.index(i))
      

    if len(user_patt)>=10:

        i = len(user_patt) - 1
        sub = []
        j = 10
        while (i >= 0 and j > 0):
            if user_patt[i] in HUSP_dict:
                sub.append(user_patt[i])

            j -= 1
            i -= 1
        sub = sub[::-1]
        a = []
        subseq = Subsequences(sub, 0, [])

        pattern = []
        for i in subseq:
            l = []
            for j in i:
                l.append(str(j))
            pattern.append(" ".join(l))



        result = []
        for i in pattern:
            for j in upattern:
                ind = j.find(i)
                if ind != -1:
                    arr = j[ind + len(i):].split(" ")
                    result += arr


        result=set(result)
        if '' in result:
            result.remove('')

        tot_rec=0

        for i in result:
            i=int(i)
            if  int(i) not in user_patt:
                if len(recommendation)==8: break
                recommendation.append("https://www.codechef.com/problems/"+problems[i])
        tot_rec+=len(recommendation)



        if tot_rec<4:
            recent_prblm = []
            r_prblm = []
            i = len(problem_solved) - 1

            while (i >= 0 and len(recent_prblm) < 2):
                if problem_solved[i] not in tags:
                    i -= 1
                    continue;
                if tags[problem_solved[i]] not in recent_prblm:
                    recent_prblm.append(tags[problem_solved[i]])
                    r_prblm.append(problem_solved[i])

                i -= 1

            for i in range(len(recent_prblm)):
                temp = diff_score[recent_prblm[i]]
                temp_prblm = list(temp.keys())
                ind = temp_prblm.index(r_prblm[i])
                count = 0
                while ind < len(temp_prblm) and count < 2:
                    if temp_prblm[ind] not in problem_solved :
                        count += 1
                        tot_rec += 1
                        recommendation.append("https://www.codechef.com/problems/"+temp_prblm[ind])
                    ind += 1

    else:

            temp=["conditional-statements","algorithms"]
            for i in temp:
                temp_prblm=diff_score[i]
                #print(temp_prblm)
                temp_prblm=list(temp_prblm.keys())
                l=0
                p=[]
                while(len(p)<3 and l < len(temp_prblm)):
                    if temp_prblm[l] not in problem_solved:
                        p.append(temp_prblm[l])
                    l+=1
                for i in p:
                    recommendation.append("https://www.codechef.com/problems/"+i)
    return  recommendation

# out=recommender();

# for i in out:
#     print("https://www.codechef.com/problems/"+i)

