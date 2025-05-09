import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def get_kenh_14():
    # Cấu hình trình duyệt không hiển thị (headless)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    # Khởi tạo WebDriver
    url = "https://kenh14.vn/xa-hoi.chn"
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    
    scroll_pause_time = 2
    last_height = driver.execute_script("return document.body.scrollHeight")

    for _ in range(5):  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Lấy HTML sau khi cuộn
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    news = soup.find_all('h3', class_='knswli-title')
    links = [link.find('a').attrs["href"] for link in news if link.find('a')]
    links = list(dict.fromkeys(links))  # Bỏ trùng

    

    data = []

    for link in links:
        try:
            news = requests.get("https://kenh14.vn" + link)
            soup = BeautifulSoup(news.content, 'html.parser')

            title = soup.find("h1", class_="kbwc-title").text.strip() if soup.find("h1", class_="kbwc-title") else ""
            description = soup.find("h2", class_="knc-sapo").text.strip() if soup.find("h2", class_="knc-sapo") else ""
            body = soup.find("div", class_="detail-content") 

            try:
                paragraphs = body.find_all(['p']) if body else []
                content = "\n".join(p.get_text(strip=True) for p in paragraphs)
            except:
                content = ""

            try:
                image = body.find("img").attrs["src"] if body and body.find("img") else ""
            except:
                image = ""
            
            item = [title, description, image, content]
            data.append(item)
            
        except Exception as e:
            print(f" Lỗi khi xử lý bài viết: {e}")

    df1 = pd.DataFrame(data, columns=["title", "description", "image", "content"])
    df1.to_excel("output_kenh14.xlsx", index=False)

    print(" Đã lưu file thành công")

# Tự động chạy lúc 6 giờ sáng
schedule.every().day.at("06:00").do(get_kenh_14)

if __name__ == "__main__":
    print("Chương trình đang chạy...")
    while True:
        # get_kenh_14()
        schedule.run_pending()
        time.sleep(1)
        
