from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook
import time

# Step 1: Set up the Chrome driver
driver = webdriver.Chrome()  # Make sure ChromeDriver is installed

# Step 2: Create an Excel workbook and sheet
wb = Workbook()
ws = wb.active
ws.title = "Books Data"
ws.append(["Title", "Price"])  # Header row

# Step 3: Loop through pages (pagination)
for page in range(1, 4):  # You can increase the range for more pages
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    print(f"Scraping: {url}")
    driver.get(url)
    time.sleep(2)  # Wait for page to load

    # Step 4: Find all book containers on the page
    books = driver.find_elements(By.CLASS_NAME, "product_pod")
    for book in books:
        # Step 5: Extract book title and price
        title = book.find_element(By.TAG_NAME, "h3").text
        price = book.find_element(By.CLASS_NAME, "price_color").text
        ws.append([title, price])  # Save to Excel

# Step 6: Save the Excel file
wb.save("scraped_books.xlsx")
print("✅ Data exported successfully to scraped_books.xlsx")

driver = webdriver.Chrome(executable_path="driver = webdriver.Chrome(executable_path=")



# Step 7: Quit the browser
driver.quit()

