# 大数据采集与处理实验2

- 姓名：柳兆星
- 学号：112404150131
- 班级：数据科学与大数据技术软件1241班
- Python：3.11

## 实验内容

1. 使用 `requests`、`BeautifulSoup` 和 CSS 选择器爬取中国大学排名，保存为 `data/university_rankings.csv`。
2. 爬取百度新闻镜像页的热点标题和详情链接，保存为 `data/baidu_news.csv`。

## 安装依赖

在 PyCharm 终端运行：

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 运行

```powershell
.\.venv\Scripts\python.exe experiment2_web_parsing.py
```

正常运行时会显示两个案例的提取数量，并在 `data` 文件夹生成两个 CSV 文件。

## 建议截图

1. `get_html` 函数：标注请求、编码处理和异常处理。
2. `parse_university_rankings` 函数：标注 `table > tbody > tr` 和 `td` CSS 选择器。
3. `parse_baidu_news` 函数：标注热点新闻、焦点新闻选择器。
4. 终端运行成功结果，以及用 Excel 打开的两个 CSV 文件。
