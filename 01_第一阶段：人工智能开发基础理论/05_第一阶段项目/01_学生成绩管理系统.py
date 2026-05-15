import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

try:
    data = pd.read_excel('./学生信息.xlsx',dtype={'学号': str,'姓名':str,'班级':str})
except FileNotFoundError:
    data={}
df=pd.DataFrame(data)
df = df.reset_index(drop=True)

# 添加学生信息
def add_student_data():
    global df
    while True:
        #添加一个判断逻辑，允许用户返回上一级
        print("1.确认录入数据")
        print("2.返回")
        #用户输入选项用来执行下一步
        input_choice=input("请选择1~2")

        if input_choice=="1":
            pass
        elif input_choice=="2":
            break#跳出函数循环
        else:
            print("输入不为1或2，请重新输入")
            continue#返回该判断逻辑，重新输入
        #输入学号
        input_id=input("请输入学号：")
        if not df.empty:
            if input_id in df['学号'].tolist():
                print(f"学号 {input_id} 已存在，请勿重复录入", end="\n\n")
                continue
            elif input_id == "":
                print("录入失败，输入不能为空", end="\n\n")
                continue
        elif input_id=="":
            print("录入失败，输入不能为空",end="\n\n")
            continue
        # 输入姓名
        input_name=input("请输入姓名：")
        if input_name=="":
            print("录入失败，输入不能为空",end="\n\n")
            continue
        #输入班级
        input_class=input("请输入班级：")
        if input_class=="":
            print("录入失败，输入不能为空",end="\n\n")
            continue
        # 输入语文成绩
        input_chinese=float(input("请输入语文成绩："))
        if input_chinese=='':
            pass
        elif input_chinese<0 or input_chinese>100:
            print("录入失败，请输入0到100之中的数",end="\n\n")
            continue

        # 输入数学成绩
        input_math = float(input("请输入数学成绩："))
        if input_math == '':
            pass
        elif input_math < 0 or input_math > 100:
            print("录入失败，请输入0到100之中的数", end="\n\n")
            continue

        #输入英语成绩
        input_english = float(input("请输入英语成绩："))
        if input_english == '':
            pass
        elif input_english < 0 or input_english > 100:
            print("录入失败，请输入0到100之中的数", end="\n\n")
            continue

        total_score = input_chinese + input_math + input_english
        average_score = total_score / 3

        #通过字典方式来创建dataframe
        data={
            '学号':input_id,
            '姓名':input_name,
            '班级':input_class,
            '语文成绩':input_chinese,
            '数学成绩':input_math,
            '英语成绩':input_english,
            '总分':total_score,
            '平均分':average_score,
        }

        df_new=pd.DataFrame([data])
        df=pd.concat([df,df_new])
        df = df.reset_index(drop=True)
        # 重新计算总分和平均分
        score_cols = ['语文成绩', '数学成绩', '英语成绩']
        df['总分'] = df[score_cols].sum(axis=1)
        df['平均分'] = df[score_cols].mean(axis=1).round(2)

        print("录入成功",end="\n\n")


#获取学生信息
def get_student_data():
    while True:
        # 添加一个判断逻辑，允许用户返回上一级
        print("1.按学号精准查询")
        print("2.按姓名模糊查询")
        print("3.按班级查询")
        print("4.查看全部数据")
        print("5.返回")
        input_choice=input("请选择1~5")
        if input_choice=="1":
            input_id=input("请输入学号：")
            if input_id in df['学号'].tolist():
                pass
            else:
                print("暂无学生信息",end="\n\n")
                continue
            print(df[df['学号']==input_id])
        elif input_choice=="2":
            input_name=input("请输入姓名")
            if df[df['姓名'] == input_name].empty :
                print("信息不存在",end="\n\n")
            else:
                print(df[df['姓名'] == input_name])
        elif input_choice=="3":
            input_class=input("请输入班级：")
            if df[df['班级'] == input_class].empty:
                print("信息不存在", end="\n\n")
            else:
                print(df[df['班级'] == input_class])
        elif input_choice=="4":
            print(df)
        elif input_choice=="5":
            break
        else:
            print("请输入正确的选项",end="\n\n")
            continue


#修改教务成绩
def update_student_data():
    while True:
        # 添加一个判断逻辑，允许用户返回上一级
        print("1.确认修改数据")
        print("2.返回")
        #用户输入选项用来执行下一步
        input_choice=input("请选择1~2")
        if input_choice=="1":
            pass
        elif input_choice=="2":
            break#跳出函数循环
        else:
            print("输入不为1或2，请重新输入")
            continue#返回该判断逻辑，重新输入
        #用户输入学号
        input_id=input("请输入学号:")
        #检验学生是否存在
        if input_id in str(df['学号'].values):
            pass
        else:
            print("学号不存在，请重新输入",end="\n\n")
            continue

        while True:
            input_update_category=input("请输入你要修改的信息(姓名,班级,语文成绩,数学成绩,英语成绩)为:")
            if input_update_category in["姓名",'班级','语文成绩','数学成绩','英语成绩']:
                break
            else:
                print("请输入正确的你应该修改的信息",end="\n\n")
                continue
        while True:
            input_update_info=input(f"你需要修改的{input_update_category}为：")
            if input_update_category=='姓名':
                df.loc[df['学号']==input_id,'姓名']=input_update_info
                break
            elif input_update_category=='班级':
                df.loc[df['班级']==input_id,'班级']=input_update_info
                break
            elif input_update_category=='语文成绩'or'数学成绩'or'英语成绩':
                if float(input_update_info)<0 or float(input_update_info)>=100:
                    print("请输入0-100之间的数",end="\n\n")
                    continue
                else:
                    input_update_info=float(input_update_info)
                    if input_update_category=='语文成绩':
                        df.loc[df['学号'] == input_id, '语文成绩'] = input_update_info
                        break
                    elif input_update_category=='数学成绩':
                        df.loc[df['学号']==input_id,'数学成绩']=input_update_info
                        break
                    elif input_update_category=='英语成绩':
                        df.loc[df['学号']==input_id,'英语成绩']=input_update_info
                        break
        print(f"已将学号{input_id}的{input_update_category}修改为{input_update_info}")


#删除教务数据
def delete_student_data():
    global df
    while True:
        print("1.确认删除数据")
        print("2.退出")
        input_choice=input("请选择1~2")
        if input_choice=="1":
            pass
        elif input_choice=="2":
            break
        else:
            continue
        input_id = input("请输入学号：")
        if input_id in df['学号'].tolist():
            pass
        else:
            print("暂无学生数据", end="\n\n")
            continue
        print("1.是否确定要删除该学生的所有数据")
        print("2.不删除")
        input_choice=input("请选择1~2")
        if input_choice=="1":
            df=df[df['学号']!=input_id]
            print(f"学号为{input_id}被成功删除了")
        elif input_choice=="2":
            continue


#教务数据统计分析
def gradeanalyzer():
    global df
    while True:
        print("1.计算各科平均分, 最高分, 最低分")
        print("2.自动计算每位学生总分与平均分")
        print("3.按总分进行排名")
        print("4.统计各班级平均分或总分情况")
        print("5.统计及格人数,不及格人数,优秀人数")
        print("6.返回")
        input_choice=input("请选择1~6")
        #计算各科平均分, 最高分, 最低分
        if input_choice=="1":
            chinese_average=sum(df['语文成绩'])/len(df['语文成绩'])
            chinese_max=max(df['语文成绩'])
            chinese_min=min(df['语文成绩'])
            print(f"语文成绩平均分为{chinese_average:.2f}，最高分为{chinese_max}，最低分为{chinese_min}")
            math_average = sum(df['数学成绩']) / len(df['数学成绩'])
            math_max = max(df['数学成绩'])
            math_min = min(df['数学成绩'])
            print(f"数学成绩平均分为{math_average:.2f}，最高分为{math_max}，最低分为{math_min}")
            english_average = sum(df['英语成绩']) / len(df['英语成绩'])
            english_max=max(df['英语成绩'])
            english_min=min(df['英语成绩'])
            print(f"英语成绩平均分为{english_average:.2f}，最高分为{english_max}，最低分为{english_min}",end="\n\n")
        #2.自动计算每位学生总分与平均分
        elif input_choice=="2":
            for student_id in df['学号']:
                chinese_score=df.loc[df['学号']==student_id,'语文成绩'].values[0]
                math_score=df.loc[df['学号']==student_id,'数学成绩'].values[0]
                english_score=df.loc[df['学号']==student_id,'英语成绩'].values[0]
                student_total=chinese_score+math_score+english_score
                student_average=student_total/3
                print(f"{df.loc[df['学号']==student_id,'姓名'].values[0]}的总分为{student_total},平均分为{student_average:.2f}")
            print()
        #3.按总分进行排名
        elif input_choice=="3":
            temp_df = df.copy()
            temp_df['总分'] = temp_df['语文成绩'] + temp_df['数学成绩'] + temp_df['英语成绩']
            ranked = temp_df.sort_values(by='总分', ascending=False)
            print(ranked[['学号', '姓名', '总分']])  # 只显示关键列
        #4.统计各班级平均分或总分情况
        elif input_choice=="4":
            #计算总分列
            df['总分'] = df['语文成绩'] + df['数学成绩'] + df['英语成绩']
            #遍历班级id，分别输出结果
            for class_id in df['班级'].unique():#unique方法去重
                class_total=df.loc[df['班级'] == class_id,'总分'].sum()
                class_average=class_total/(df.loc[:,'班级']==class_id).sum()
                print(f"班级{class_id}的总分是{class_total}，平均分为{class_average:.2f}")
        #5.统计及格人数,不及格人数,优秀人数
        elif input_choice=="5":
            pass_score = 60   #设置及格分数为60分
            excellent_score = 85 #设置优秀分数为85分
            chinese_pass_count=(df['语文成绩']>=pass_score).sum()
            chinese_fail_count=(df['语文成绩']<pass_score).sum()
            chinese_excellent_count=(df['语文成绩']>excellent_score).sum()
            print(f"语文成绩及格人数为{chinese_pass_count}人，不及格人数为{chinese_fail_count}人，优秀人数为{chinese_excellent_count}人")

            math_pass_count=(df['数学成绩']>=pass_score).sum()
            math_fail_count=(df['数学成绩']<pass_score).sum()
            math_excellent_count=(df['数学成绩']>excellent_score).sum()
            print(f"数学成绩及格人数为{math_pass_count}人，不及格人数为{math_fail_count}人，优秀人数为{math_excellent_count}人")

            english_pass_count=(df['英语成绩']>=pass_score).sum()
            english_fail_count=(df['英语成绩']<pass_score).sum()
            english_excellent_count=(df['英语成绩']>excellent_score).sum()
            print(f"英语成绩及格人数为{english_pass_count}人，不及格人数为{english_fail_count}人，优秀人数为{english_excellent_count}人")

        elif input_choice=="6":
            break
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
def data_visualization():
    while True:
        print("1.各科平均分柱状图")
        print("2.学生总分排名条形图")
        print("3.各科成绩分布直方图")
        print("4.班级平均分对比图")
        print("5.返回")
        input_choice=input("请选择1~5")
        if input_choice=="1":
            chinese_average = sum(df['语文成绩']) / len(df['语文成绩'])
            math_average = sum(df['数学成绩']) / len(df['数学成绩'])
            english_average = sum(df['英语成绩']) / len(df['英语成绩'])
            labels=['语文','数学','英语']
            values=[chinese_average,math_average,english_average]
            plt.figure(figsize=(max(10, len(labels) * 0.6), 8))
            bars=plt.bar(labels,values,align='center',width=0.3,label='平均分',
                    color=plt.cm.viridis(np.linspace(0, 0.8, len(labels))))
            for bar,value in zip(bars, values):
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width() / 2,
                    height+0.5,
                    f"{value:.2f}",
                    ha='center',
                    va='bottom',
                    fontsize=10,
                    fontweight='bold',
                    color='black')
            plt.xlabel('科目',fontsize=12,fontweight='bold')  # X轴标签
            plt.ylabel('平均分',fontsize=12,fontweight='bold')  # Y轴标签
            plt.title('各科平均分比较',fontsize=12,fontweight='bold')  # 图表标题
            plt.ylim(0, max(values) * 1.15)
            plt.tight_layout()
            plt.legend()
            plt.show()
        elif input_choice=="2":
            df_sort = df.sort_values(by='总分', ascending=False)
            labels = df_sort['姓名']
            values = df_sort['总分']
            # 设置图形大小，适应更多学生
            plt.figure(figsize=(max(10, len(labels) * 0.6), 8))  # 根据学生数量调整宽度
            # 绘制条形图
            bars = plt.bar(labels, values, align='center', width=0.5, label='总分',
                           color=plt.cm.viridis(np.linspace(0.2, 0.8, len(labels))))
            # 在条形上添加数值标签
            for bar, value in zip(bars, values):
                # 获取条形的高度
                height = bar.get_height()
                # 在条形顶部上方显示数值
                plt.text(bar.get_x() + bar.get_width() / 2,  # x位置：条形中心
                         height + 0.5,  # y位置：条形高度上方0.5单位
                         f'{value}',  # 显示的数值
                         ha='center',  # 水平居中
                         va='bottom',  # 垂直底部对齐
                         fontsize=10,
                         fontweight='bold',
                         color='darkblue')
            # 设置坐标轴标签和标题
            plt.xlabel('姓名', fontsize=12, fontweight='bold')
            plt.ylabel('总分', fontsize=12, fontweight='bold')
            plt.title('学生总分排名', fontsize=16, fontweight='bold', pad=20)
            # 添加图例
            plt.legend()
            # 添加横向网格线，提高可读性
            plt.grid(axis='y', alpha=0.3, linestyle='--')
            # 自动调整y轴上限，为数据标签留出空间
            plt.ylim(0, max(values) * 1.15)
            # 调整布局，防止标签被截断
            plt.tight_layout()
            plt.show()
        elif input_choice=="3":
            # 从数据源获取各科成绩
            语文成绩 = df['语文成绩']
            数学成绩 = df['数学成绩']
            英语成绩 = df['英语成绩']
            bins_chinese = int(np.sqrt(len(语文成绩)))
            bins_math = int(np.sqrt(len(数学成绩)))
            bins_english = int(np.sqrt(len(英语成绩)))
            # 基本直方图
            plt.subplot(2,2,1)
            plt.hist(语文成绩, bins_chinese, color='skyblue', edgecolor='black')
            plt.xlabel('成绩')
            plt.ylabel('频数')
            plt.title('语文成绩分布直方图')
            plt.grid(alpha=0.3)


            plt.subplot(2,2,2)
            plt.hist(数学成绩, bins_math, color='skyblue', edgecolor='black')
            plt.xlabel('成绩')
            plt.ylabel('频数')
            plt.title('数学成绩分布直方图')
            plt.grid(alpha=0.3)


            plt.subplot(2,2,3)
            plt.hist(英语成绩, bins_english, color='skyblue', edgecolor='black')
            plt.xlabel('成绩')
            plt.ylabel('频数')
            plt.title('英语成绩分布直方图')
            plt.grid(alpha=0.3)

            plt.tight_layout()

            plt.show()

        elif input_choice=="4":
            list_average = []
            for class_id in df['班级'].unique():  # unique方法去重
                class_total = df.loc[df['班级'] == class_id, '总分'].sum()
                class_average = class_total / (df.loc[:, '班级'] == class_id).sum()
                list_average.append(class_average)
            labels=df['班级'].unique()
            values=list_average
            plt.figure(figsize=(max(10, len(labels) * 0.6), 8))
            bars=plt.bar(labels,values,align='center' ,label='班级平均分',width=0.3,
                    color=plt.cm.viridis(np.linspace(0, 0.8, len(labels))))
            for bar, value in zip(bars, values):
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width() / 2,
                         height+0.5,
                         f"{value:.2f}",
                         ha='center',
                         va='bottom',
                         fontsize=10,
                         fontweight='bold',
                         color='darkblue')
            plt.xlabel('班级',fontsize=12,fontweight='bold')
            plt.ylabel('平均分',fontsize=12,fontweight='bold')
            plt.title('班级平均分对比图')
            plt.legend()
            plt.grid(alpha=0.3)
            plt.ylim(0, max(values) * 1.15)
            plt.tight_layout()
            plt.show()

        elif input_choice=="5":
            break


def generate_analysis_report():
    report_lines = []
    report_lines.append("=" * 15)
    report_lines.append("【智能分析与预警报告】")
    report_lines.append("=" * 15)
    report_lines.append('\n')

    total_avg = df['总分'].mean()
    total_std=df['总分'].std()
    report_lines.append(f"全校学生:{len(df)}")
    report_lines.append('\n')
    report_lines.append(f"全校平均总分:{total_avg:.2f}")
    report_lines.append('\n')

    cv = total_std / total_avg if total_avg > 0 else 0
    if cv < 0.15:
        overall_eval = "整体成绩非常稳定，学生水平均衡"
    elif cv < 0.25:
        overall_eval = "整体表现良好，差异较小"
    elif cv < 0.35:
        overall_eval = "存在一定分化，需关注后进学生"
    else:
        overall_eval = "两极分化明显，应重点关注薄弱学生"
    report_lines.append(f"全校评价：{overall_eval}")
    report_lines.append("\n")

    report_lines.append("\n")
    report_lines.append("[学科分析]")
    report_lines.append("\n")
    subject_means = pd.Series({
        '语文': df['语文成绩'].mean(),
        '数学': df['数学成绩'].mean(),
        '英语': df['英语成绩'].mean()
    })
    best_subject = subject_means.idxmax()  # 最大值对应的索引（学科名）
    worst_subject = subject_means.idxmin()  # 最小值对应的索引
    report_lines.append(f"优势学科：{best_subject}({subject_means[best_subject]:.2f})")
    report_lines.append("\n")
    report_lines.append(f"劣势学科：{worst_subject}({subject_means[worst_subject]:.2f})")
    report_lines.append("\n")

    pass_score = 60  # 设置及格分数为60分
    chinese_fail_count = (df['语文成绩'] <= pass_score).sum()
    math_fail_count = (df['数学成绩'] <= pass_score).sum()
    english_fail_count = (df['英语成绩'] <= pass_score).sum()
    report_lines.append("\n")
    report_lines.append("[单科预警]")
    report_lines.append("\n")
    report_lines.append(f"语文不及格人数:{chinese_fail_count}(占比{chinese_fail_count/len(df)*100:.1f}%)")
    report_lines.append("\n")
    report_lines.append(f"数学不及格人数:{math_fail_count}(占比{math_fail_count/len(df)*100:.1f}%)")
    report_lines.append("\n")
    report_lines.append(f"英语不及格人数:{english_fail_count}(占比{english_fail_count/len(df)*100:.1f}%)")
    report_lines.append("\n")

    report_lines.append("\n")
    report_lines.append("[总分优异学生预警]")
    report_lines.append("\n")
    grage_sort=df.sort_values(by='总分', ascending=False)
    best_student=grage_sort['姓名'][:5]
    worst_student=grage_sort['姓名'][-5:]
    report_lines.append("前五名:")
    report_lines.append("\n")

    for i in best_student:
        report_lines.append(f"{i}({df.loc[df['姓名']==i,'班级'].values[0]}班)总分{df.loc[df['姓名']==i,'总分'].values[0]}")
        report_lines.append("\n")
    report_lines.append("后五名(成绩偏低):")
    report_lines.append("\n")
    for i in worst_student:
        report_lines.append(f"{i}({df.loc[df['姓名']==i,'班级'].values[0]}班)总分{df.loc[df['姓名']==i,'总分'].values[0]}")
        report_lines.append("\n")
    report_lines.append("\n")
    # report_lines.append("总分偏低预警(低于180分):")
    # report_lines.append("\n")
    # low_total=df[df['总分']<180]
    # if low_total.shape[0]>0:
    #     for i in low_total.index:
    #         report_lines.append(f"{i}({df.loc[df['姓名']==i,'班级'].values}班)总分{df.loc[df['姓名']==i,'总分'].values[0]}")
    #         report_lines.append("\n")
    # else:
    #     report_lines.append(f"总分表现：所有学生总分均高于180分，整体较好。")
    #     report_lines.append("\n")


    report_lines.append("\n【班级整体表现评价】")
    report_lines.append("\n")
    classes = df['班级'].unique()
    for cls in classes:
        class_df = df[df['班级'] == cls]
        class_avg = class_df['总分'].mean()
        class_std = class_df['总分'].std()
        class_cv = class_std / class_avg if class_avg > 0 else 0
        class_fail_ratio = (class_df['总分'] < 180).sum() / len(class_df)

        # 评价逻辑
        if class_cv < 0.15:
            stability = "成绩稳定，水平均衡"
        elif class_cv < 0.25:
            stability = "差异适中"
        else:
            stability = "两极分化明显"

        if class_avg >= 300 * 0.8:
            perf = "优秀"
        elif class_avg >= 300 * 0.6:
            perf = "良好"
        else:
            perf = "需提升"

        if class_fail_ratio > 0.2:
            warning = "后进学生比例较高"
        elif class_fail_ratio > 0.05:
            warning = "有少数后进学生"
        else:
            warning = ""

        report_lines.append(f"• {cls}：平均分 {class_avg:.1f}，{perf}，{stability}，{warning}")
        report_lines.append("\n")

    print(*report_lines)

def main():
    # 主程序需要死循环，当输入6时跳出循环
    while True:
        print("======AI教务数据分析系统======")
        print("1. 录入学生教务数据")
        print("2. 查询教务数据")
        print("3. 修改教务数据")
        print("4. 删除教务数据")
        print("5. 教务数据统计分析")
        print("6. 教务数据可视化")
        print("7. 智能分析与预警")
        print("8. 退出系统并导出文件")
        input_num = input()#记录输入的数字
        if input_num=="1":
            add_student_data()
        elif input_num=="2":
            get_student_data()
        elif input_num=="3":
            update_student_data()
        elif input_num=="4":
            delete_student_data()
        elif input_num=="5":
            gradeanalyzer()
        elif input_num=="6":
            data_visualization()
        elif input_num=="7":
            generate_analysis_report()
        elif input_num=="8":
            print("系统退出")
            break


if __name__ == '__main__':
    main()
    df.to_excel('学生信息.xlsx', index=False)  # 将存入的数据保存到excel表
    print("文件已成功保存，存储路径为E:\\Ai code\\10_第一阶段项目\\学生信息.xlsx")
















