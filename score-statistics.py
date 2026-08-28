def score_analysis(score_list):
    max_score=max(score_list)
    min_score=min(score_list)
    average_score=sum(score_list)/len(score_list)
    return max_score,min_score,round(average_score,2)
if __name__ == '__main__':
    score_list=[]
    print("请逐个输入分数，输入a时结束录入")
    while True:
        User_input=input("请输入分数:")
        if User_input.lower()=="a":
            break
        else:
            try:
                score=float(User_input)
                if 0<=score<=150:
                    score_list.append(score)
                else:
                    print("分数应在0~150之间")
            except ValueError:
                print("输入无效，请正确输入数字")
    if len(score_list)==0:
        print("没录入任何分数，自动退出")
    else:
        high,low,average=score_analysis(score_list)
        result_text=f"""
        ====成绩统计结果====
        最高分：{high}
        最低分：{low}
        平均分{average}"""
        print(result_text)
        with open("result.txt","w",encoding="utf-8") as f:
            f.write(result_text)







