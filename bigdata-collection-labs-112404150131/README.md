# 大数据采集与处理实验

- 姓名：柳兆星
- 学号：112404150131
- 班级：数据科学与大数据技术软件1241班
- GitHub 用户名：KL2223

## 实验内容

本仓库用于提交“大数据采集与处理”课程实验。实验一包括：

1. 使用 Requests 调用 QQ 表情搜索接口并将图片保存到本地。
2. 使用 Requests 查询手机号码归属地，并将响应源代码保存为本地 HTML。

## 目录结构

```text
bigdata-collection-labs-112404150131/
├── README.md
└── lab01/
    ├── REPORT.md
    ├── lab1_html_api.ipynb
    ├── data/
    │   ├── companies.json
    │   └── devices.json
    └── images/
        ├── 01_qq_code.png
        ├── 02_qq_images.png
        ├── 03_phone_code.png
        └── 04_phone_result.png
```

## 运行环境

- Python 3.11
- requests 2.x
- JupyterLab 或 PyCharm

安装依赖：

```bash
python -m pip install requests
```

运行 Notebook 前，请将其中的手机号变量设置为自己的号码。不要在公开仓库中提交访问令牌、密码、Cookie 等敏感信息。
