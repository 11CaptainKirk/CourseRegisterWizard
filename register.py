from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os


from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())

pw = os.getenv("REG_PW")
print(pw)

driver.get("https://utdirect.utexas.edu/registration/registration.WBX?s_ccyys=20232&s_student_eid=&s_nonce=B10A78A8401D219ACBADDC46086F227ADEC2B924&s_unique_add=&s_unique_drop=+&s_request=STSWP&s_swap_unique_drop=54635&s_swap_unique_add=54595&s_submit=Submit")
sleep(5)
driver.quit()



