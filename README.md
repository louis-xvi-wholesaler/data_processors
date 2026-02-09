# This is a python file meant for linear fitting 这是一份用于线性拟合的python文件

three functions are provided here 这里提供了三个函数
you have to edit the file to process your own data. 你需要修改文件以处理你自己的数据。 

## extract_numbers

it extracts numbers of a given text string, and returns a list of numbers sequenced as original
从给定文档串中提取数字，返回数字构成的列表，按原顺序排列

## draw_linear
it draws the fitting line
绘制拟合直线
    
parameter show_formula: the default is True, and if it is designated as False, the formula will not appear in the figure.\
默认为 True，如果被指定为 False ， 拟合公式将不会出现在图上。

## print_data_linear
it gets relative data printed
把相关数据打印出来
including：
slope, intercept, slope stderr(A type), (B type uncertainty and compound uncertainty,) the standard error of residuals,
the value of coefficient of association, the value of R-squared, p-value
包括：
斜率、截距、斜率的标准误差 （A类）、（斜率的B类不确定度和合成不确定度、）残差标准差、相关系数、R平方 、P值
    
:param y_uncertainty: the uncertainty of dependent variables. if it is designated, B type and compound uncertainties
will be shown unless show_b_uncertainty is designated as False; if not, B type and compound uncertainties won't be shown.
因变量不确定度，如果给定值，B类不确定度和合成不确定度会被打印出来，除非参数show_b_uncertainty被指定为False；如果不给值，上述两类不确定度将不会被打印。

:param distribution: the distribution pattern of random errors, whose default is 'uniform'. also 'triangular' and 'normal' can be designated.
随机误差分布方式，默认为uniform（均匀），也可指定为triangular（三角）或normal（正态）
