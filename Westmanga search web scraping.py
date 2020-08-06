from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#path ke tempat file chrome driver
PATH = "/run/media/dimas/Data/[Manjaro Linux File]/web scraping//chromedriver"
driver = webdriver.Chrome(PATH)
#settings agar driver menunggu web terload dengan tenggang maksimal waktu selama 10 detik
driver.implicitly_wait(10)
driver.get("https://westmanga.info/")
#print title dari web page
print(driver.title)
print()

#Mencari kotak search
search = driver.find_element_by_id("s")
search.clear()
#memasukkan karakter ke dalam kotak pencarian dan pencet enter(return)
search.send_keys(input("Masukkan nama manga yang anda inginkan! : "))
search.send_keys(Keys.RETURN)
#mencari class name "fulled" di dalam web
main = driver.find_element_by_class_name("fulled")
#Mencari list elements yang bernama "result-search"
titles = main.find_elements_by_class_name("result-search")
#berputar di dalam list "result search" dan mencari elemen class bernama "search-title" dan print
for title in titles:
    title_ = title.find_element_by_class_name("search_title")
    #print()
    print(title_.text)
    
print("Apakah anda melanjutkan memilih manga spesifik? Jika tidak maka keluar")
go_in = input(bool)
if go_in == True:
    print("Pilih manga yang ada di list! #case sensitive")
    input_user = input(str)
    link = driver.find_element_by_link_text(input_user)
    link.click()

else:
    driver.quit()
    



#time.sleep(5)

#driver.quit()