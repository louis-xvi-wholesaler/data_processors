# 导入所需库：numpy用于数值计算，matplotlib用于绘图，scipy用于线性拟合
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from math import log, sqrt
import re

def extract_numbers(text:str) -> list:
    '''
    Docstring for extract_numbers
    extracts numbers of a given text string 从给定文档串中提取数字
    
    :param text: the text to be processsed\
    待处理文本
    :returns: a list of numbers, sequenced as original\
    数字构成的列表，按原顺序排列
    '''
    # example 示例
    # text = "温度从-5.3℃升至20.5℃，变化25.8℃"
    # result = extract_numbers(text)
    # print(result)  # 输出: [-5.3, 20.5, 25.8]
    
    # match integers and decimals 匹配整数或小数（包括负数）
    numbers = re.findall(r'-?\d+(?:\.\d+)?', text)
    # convert to numbers 转换为浮点数或整数
    result = []
    for num in numbers:
        if '.' in num:
            result.append(float(num))
        else:
            result.append(int(num))
    return result


# ------------------input the lists of variables --------------------

# input the list of independent variables 填入自变量数据
x_data = np.array(list(map(lambda x: x - 15.559,
                           [
                               24.372, 29.191, 33.942, 38.727, 43.434 
                           ]))) 
# np.arange(1, 11) -> array([1,2,3,4,5,6,7,8,9,10])

# input the list of independent variables 填入因变量数据

y_data = np.array(list(map(log,
    [11.4, 10.2,  8.96, 7.60, 7.04 
                   ]))) 
# ----------------------------------------------------------------------

# 线性拟合核心计算：返回斜率、截距、相关系数r、p值、标准误差
# std_err stands for standard error
# std_err 就是斜率标准差，斜率标准差和斜率标准误差是一个东西
slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)


# 根据拟合得到的斜率和截距，生成拟合直线的y值
# calculate the value of y according to the fitting line
extension = (max(x_data) - min(x_data)) * 0.05 # 
x_fit = np.linspace(min(x_data) - extension, max(x_data) + extension, 120)  # generate 120 points to make the line smooth 生成120个点使直线平滑
y_fit = slope * x_fit + intercept

# residuals 残差
y_pred = slope * x_data + intercept
residuals = y_data - y_pred

# the standard error for residuals 残差标准差
residual_std = np.std(residuals, ddof=2)

def draw_linear(show_formula=True):
    '''
    Docstring for draw_linear
    draw the fitting line
    绘制拟合直线
    
    :param show_formula: the default is True, and if it is designated as False, the formula will not appear in the figure.\
    默认为 True，如果被指定为 False ， 拟合公式将不会出现在图上。
    '''
    # create a screen and set its size 创建绘图窗口并设置大小
    plt.figure(figsize=(8, 5))

    # plot original scatters 绘制原始散点：blue 蓝色，size 大小80
    plt.scatter(x_data, y_data, color='blue', s=80, 
             label='data', marker='x') # edgecolor='black', black-margined 边缘黑色
    # plot the fitting line 绘制拟合直线：绿色实线，线宽2
    plt.plot(x_fit, y_fit, color='turquoise', linewidth=2, label='fitting')

    # set the title and axis labels 设置图表标题和坐标轴标签（editable 可根据需求修改文字内容）
    plt.title('linear fitting', fontsize=14, pad=15)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('U', fontsize=12)

    # add and show the fitting formula and coefficient of association 添加拟合公式和相关系数文本：显示在图表左上角
    if show_formula:
        fit_text = f'formula : y = {slope:.4f}x + {intercept:.4f}\n \
        r = {r_value:.6f} p = {p_value:e}'
        plt.text(0.05, 0.95, fit_text, transform=plt.gca().transAxes, 
            fontsize=11, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # show the legend and grid 显示图例和网格线
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)  # alpha determines the transparency of the grid. alpha控制网格透明度

    # show the figure 显示图像
    plt.show()

def print_data_linear(y_uncertainty=float('-inf'), 
                      distribution='uniform', 
                      show_b_uncertainty=None):
    '''
    Docstring for print_data_linear
    get relative data printed
    把相关数据打印出来
    
    :param y_uncertainty: the uncertainty of dependent variables. if it is designated, B type and compound uncertainties
    will be shown unless show_b_uncertainty is designated as False; if not, B type and compound uncertainties won't be shown.\n
    因变量不确定度，如果给定值，B类不确定度和合成不确定度会被打印出来，除非参数show_b_uncertainty被指定为False；如果不给值，上述两类不确定度将不会被打印。\n
    :param distribution: the distribution pattern of random errors, whose default is 'uniform'. also 'triangular' and 'normal' can be designated.\n
    随机误差分布方式，默认为uniform（均匀），也可指定为triangular（三角）或normal（正态）\n
    :param show_b_uncertainty: Description
    '''

    dis_dic = {
        'uniform':sqrt(3),
        'triangular':sqrt(6),
        'normal':3
    }
    print("线性回归拟合结果")
    print("=" * 40)
    print(f"斜率 (slope): {slope:.6f}")
    print(f"截距 (intercept): {intercept:.6f}")
    print(f"斜率的标准误差 (slope stderr)A类: {std_err:.8f}")

    if show_b_uncertainty != False:
        if y_uncertainty != float('-inf'):
            show_b_uncertainty = True
        if show_b_uncertainty:
            k = dis_dic[distribution]
            S_xx = sum(x**2 for x in x_data) - sum(x_data)**2 / len(x_data)
            b_uncertainty = y_uncertainty / (k * sqrt(S_xx))
            print(f"斜率的B类不确定度： {b_uncertainty:.8f}")
            c_uncertainty = sqrt(std_err**2 + b_uncertainty**2)
            print(f"斜率的合成不确定度：{c_uncertainty:.8f}")

    print(f"残差标准差 (residual std): {residual_std:.8f}")
    print(f"相关系数 (R): {r_value:.8f}")
    print(f"R平方 (R-squared): {r_value**2:.8f}")
    print(f"P值 (P-value): {p_value:e}")


if __name__ == '__main__':
    #print_data_linear(0.01, show_b_uncertanty=False)
    #draw_linear()
    pass