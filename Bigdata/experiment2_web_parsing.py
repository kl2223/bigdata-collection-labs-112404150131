"""实验2：网页解析。

案例1：爬取中国大学排名并保存为 CSV。
案例2：爬取百度新闻热点标题与详情链接并保存为 CSV。

适用环境：Python 3.11
"""

from __future__ import annotations

import csv
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


UNIVERSITY_URL = "http://www.bspider.top/gaosan/"
NEWS_URL = "http://www.bspider.top/baidunews/"
OUTPUT_DIR = Path(__file__).resolve().parent / "data"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/130.0 Safari/537.36"
    )
}


def get_html(url: str, timeout: float = 15.0) -> str:
    """发送 GET 请求，处理编码并返回网页 HTML。"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=timeout)
        response.raise_for_status()
        response.encoding = response.apparent_encoding or "utf-8"
        return response.text
    except requests.RequestException as error:
        raise RuntimeError(f"网页请求失败：{url}\n{error}") from error


def parse_university_rankings(html: str) -> list[list[str]]:
    """使用 CSS 选择器提取高校排名表格。"""
    soup = BeautifulSoup(html, "lxml")
    rows: list[list[str]] = []

    for row in soup.select("table > tbody > tr"):
        cells = [cell.get_text(" ", strip=True) for cell in row.select("td")]
        if len(cells) >= 6:
            rows.append(cells[:6])

    if not rows:
        raise RuntimeError("未提取到高校排名，网页结构可能已经改变")
    return rows


def parse_baidu_news(html: str, base_url: str = NEWS_URL) -> list[list[str]]:
    """提取热点要闻、焦点新闻的标题和详情链接。"""
    soup = BeautifulSoup(html, "lxml")
    news_rows: list[list[str]] = []
    seen: set[tuple[str, str]] = set()

    selectors = (
        ("热点要闻", "div.hotnews a"),
        ("焦点新闻", "ul.focuslistnews a"),
    )

    for category, selector in selectors:
        for link in soup.select(selector):
            title = link.get_text(" ", strip=True)
            href = link.get("href", "").strip()
            if not title or not href:
                continue

            detail_url = urljoin(base_url, href) if href != "#" else href
            key = (title, detail_url)
            if key in seen:
                continue

            seen.add(key)
            news_rows.append([category, title, detail_url])

    if not news_rows:
        raise RuntimeError("未提取到新闻数据，网页结构可能已经改变")
    return news_rows


def save_csv(path: Path, header: list[str], rows: list[list[str]]) -> None:
    """使用 UTF-8 with BOM 保存 CSV，方便 Excel 正确显示中文。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)


def run_university_case() -> Path:
    html = get_html(UNIVERSITY_URL)
    rows = parse_university_rankings(html)

    expected_header = ["名次", "学校名称", "总分", "全国排名", "星级排名", "办学层次"]
    if rows[0] == expected_header:
        rows = rows[1:]

    output = OUTPUT_DIR / "university_rankings.csv"
    save_csv(output, expected_header, rows)
    print(f"案例1完成：共提取 {len(rows)} 所高校，已保存到 {output}")
    return output


def run_news_case() -> Path:
    html = get_html(NEWS_URL)
    rows = parse_baidu_news(html)
    output = OUTPUT_DIR / "baidu_news.csv"
    save_csv(output, ["新闻分类", "新闻标题", "详情链接"], rows)
    print(f"案例2完成：共提取 {len(rows)} 条新闻，已保存到 {output}")
    return output


def main() -> None:
    print("开始执行实验2网页解析……")
    run_university_case()
    run_news_case()
    print("两个案例均已完成。")


if __name__ == "__main__":
    main()
