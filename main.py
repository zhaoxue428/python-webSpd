from bs4 import BeautifulSoup
import requests
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import os

# 确保目标文件夹存在
os.makedirs("txts", exist_ok=True)

# 通过每一章的链接地址，下载文章内容
def down_txts(url):
    try:
        html = requests.get(url, headers=headers).text
        #soup作用就是从html里面“筛选出”我们
        soup = BeautifulSoup(html, "lxml")
        # 获取到标题
        # 找到class=wap_none的h1
        title_obj = soup.find("h1", class_="wap_none")
        # 获取到内容
        # 找到id=chaptercontent的div
        con_obj = soup.find("div", id="chaptercontent")
        # 判断不能为空
        if title_obj and con_obj:
            # 获取到标题
            title = title_obj.get_text()
            # 获取到内容
            con = con_obj.get_text()
            with open(f"txts/{title}.txt", "w", encoding='utf-8') as f:
                f.write(con)
                print(f"{title}已经下载完毕。。。")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

if __name__ == '__main__':
    url = "https://www.bqka.cc/book/159995/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64)"
    }
    # 把每一张的链接地址放到urls里面
    urls = []

    # 获取到url这个网页对应的html
    # 为什么要加headers，因为爬虫的原理就是通过python去模拟浏览器
    # 请求，需要加浏览器的信息
    html = requests.get(url, headers=headers).text
    # soup作用就是从html里面筛选出我们想要的内容
    soup = BeautifulSoup(html, "lxml")
    # 找到class="listmain"的div里面所有的超链接
    items = soup.find("div", class_="listmain").find_all("a")
    for item in items:
        # 获取到每一章的链接地址
        href = item.get("href")
        if href != "javascript:dd_show()":
            url = "https://www.bqka.cc" + href
            urls.append(url)

    starttime = datetime.now()
    # for url in urls:
    #     down_txts(url)
    with ThreadPoolExecutor(max_workers=50) as exe:
        exe.map(down_txts, urls)

    endtime = datetime.now()
    print(f"总共用了{(endtime - starttime).seconds}秒")
