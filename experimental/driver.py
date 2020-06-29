from selenium import webdriver 
  
# Taking input from user 
search_string = input("Input the URL or string you want to search for:") 
  

search_string = search_string.replace(' ', '+')  
  
browser = webdriver.Chrome('/home/cjoshea/chromedriver') 
  
for i in range(1): 
    matched_elements = browser.get("https://www.google.com/search?q=" +
                                     search_string + "&start=" + str(i))
    print(matched_elements) 
