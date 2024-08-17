# import requests

# # 字幕文件的URL
# url = "https://www.amazon.co.jp/gp/video/detail/B0B7487NLD/ref=atv_hm_hom_c_5m1aZK_brws_1_32?jic=8%7CEgRzdm9k"

# # 发送HTTP GET请求下载字幕
# response = requests.get(url)

# # 检查请求是否成功
# if response.status_code == 200:
#     # 将字幕内容写入文件
#     with open("downloaded_subtitles.vtt", "w", encoding="utf-8") as file:
#         file.write(response.text)
# else:
#     print("Failed to download the subtitles.")


# from selenium import webdriver

# # 指定Chrome WebDriver的路径
# driver_path = '/Users/zhaoxue/develop/python-webSpd/chrome-mac-arm64'
# driver = webdriver.Chrome(executable_path=driver_path)

# # 访问网页
# driver.get("https://www.amazon.co.jp/gp/video/detail/B0B7487NLD")

# # 等待页面加载，确保所有元素可访问
# driver.implicitly_wait(10)  # 等待10秒

# # 以下是一个假设的元素定位和数据提取示例
# # 假设我们知道字幕存储在某个元素中，这里我们需要实际页面结构来确定如何提取
# # 例如：
# # subtitle_element = driver.find_element_by_id("subtitleElementId")
# # subtitle_text = subtitle_element.text

# # 如果需要保存提取到的文本，可以写入文件
# # with open("downloaded_subtitles.vtt", "w", encoding="utf-8") as file:
# #     file.write(subtitle_text)

# # 关闭浏览器
# driver.quit()






from selenium import webdriver
from selenium.webdriver.chrome.service import Service

try:
    s = Service('/Users/zhaoxue/develop/python-webSpd/chrome-mac-arm64')
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.google.com")  # 打开一个示例网页来测试
    print("ChromeDriver is working.")
except Exception as e:
    print("Failed to launch ChromeDriver:", e)
finally:
    if driver:
        driver.quit()
