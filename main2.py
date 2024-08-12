from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


os.makedirs("txts2", exist_ok=True)
# 设置 ChromeDriver 路径
service = Service(executable_path=ChromeDriverManager().install())

# 创建 Chrome WebDriver 实例
driver = webdriver.Chrome(service=service)
driver.get("https://www.zhihu.com/people/xxx")

# 等待页面加载
driver.implicitly_wait(10)  # 等待10秒

# 获取页面HTML
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 打印页面标题
print(soup.title.text)
with open(f"txts2/{soup.title.text}.txt", "w", encoding='utf-8') as f:
                f.write(soup.title.text)
                print(f"{soup.title.text}已经下载完毕。。。")

# 你可以添加更多的代码来解析页面或提取你需要的数据
# ...

# 关闭浏览器
driver.quit()
