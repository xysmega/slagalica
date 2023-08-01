import pyautogui
import selenium
import pytesseract
import cv2
import win32api
import string
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from time import sleep
from PIL import Image
options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)


def slagalica():
        
        a = 'a' , Image.open('a.png')
        b = 'b' , Image.open('b.png')
        c = 'c' , Image.open('c.png')
        d = 'd' , Image.open('d.png')
        e = 'e' , Image.open('e.png')
        f = 'f' , Image.open('f.png')
      #  g = 'g' , Image.open('g.png')
        h = 'h' , Image.open('h.png')
        i = 'i' , Image.open('i.png')
        j = 'j' , Image.open('j.png')
        k = 'k' , Image.open('k.png')
      #  l = 'l' , Image.open('l.png')
        m = 'm' , Image.open('m.png')
        n = 'n' , Image.open('n.png')
        o = 'o' , Image.open('o.png')
        p = 'p' , Image.open('p.png')
        r = 'r' , Image.open('r.png')
        s = 's' , Image.open('s.png')
        t = 't' , Image.open('t.png')
        u = 'u' , Image.open('u.png')
        v = 'v' , Image.open('v.png')
        č = 'č' , Image.open('č.png')
      #  š = 'š' , Image.open('š.png')
      #  đ = 'đ' , Image.open('đ.png')
      #  dz = 'dz' , Image.open('dz.png')
      #  lj = 'lj' , Image.open('lj.png')
       
        
    
    
        ss = pyautogui.screenshot("nigga.png" ,  region=(420,550,540,40))
        im = cv2.imread('nigga.png')
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('nagger.png', gray)

        slova=pytesseract.image_to_string(gray ,config='--psm 11', lang='srp_latn')
        print(slova)
       
        
        url = 'https://www.ludara.com/resenja-slagalica/'
        driver.get(url)
        try :
            element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"letters")))
            element.clear()
            element.send_keys(slova)

            element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"words-btn")))
            element.click()

            parentElement = driver.find_element(By.CLASS_NAME, "style2")
            elementList = parentElement.find_elements(By.TAG_NAME, "h3")
            resenje = (elementList[0].get_attribute("innerHTML"))
            print(resenje)
            sps = list(resenje.lower())
            
            for z in sps :
                
                
                p= '.png'
                z=z+p
                x,y=pyautogui.locateCenterOnScreen(z)
                pyautogui.moveTo(x,y)
                pyautogui.click(x,y)


        except Exception as e:
            print("Error:", e)
        
def mojBroj():
        

        url = 'https://www.ludara.com/resenja-moj-broj/'
        driver.get(url)
        try :
            element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"target")))
            element.clear()
            element.send_keys("300")
            
            element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"number1")))
            element.clear()
            element.send_keys("2")
            
            element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"number2")))
            element.clear()
            element.send_keys("5")
            
            element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"number3")))
            element.clear()
            element.send_keys("6")
            
            element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"number4")))
            element.clear()
            element.send_keys("5")
            
            element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"number5")))
            element.clear()
            element.send_keys("10")
            
            element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"number6")))
            element.clear()
            element.send_keys("25")
            
            element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"solve-btn")))
            element.click()

            parentElement = driver.find_element(By.CLASS_NAME, "style2")
            elementList = parentElement.find_elements(By.TAG_NAME, "h3")
            resenje = (elementList[0].get_attribute("innerHTML").replace(" ", ""))
            print(resenje)
            bpb=list(resenje)
            print(bpb)

        except Exception as e:
            print("Error:", e)
        
#sleep(5)
#if pyautogui.locateOnScreen('slagalica.png') :
#   slagalica()
#else:
#   print("ERROR!PANTELA JE PEDER! NIJE TI UPALJENA IGRA GOOBERU!")
def okrenimojbroj():
    if pyautogui.locateOnScreen('./igre/matematika.png') :
        mojBroj()
    else :
        win32api.MessageBox(0, 'PANTELA JE PEDER! NIJE TI UPALJENA IGRA GOOBERU!!', 'ERROR GOOBERU!', 0x00001000) 

def spojnice():
     
        url = 'https://www.ludara.com/resenja-spojnice/'
        driver.get(url)
        try :
            element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"k1")))
            element.clear()
            element.send_keys("pantelej")
            
            element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/article/div[2]/div[1]/form/div/div[3]/div/ul/li[1]/input")))
            element.click()
            
            parentElement = driver.find_element(By.CLASS_NAME, "style2")
            elements = parentElement.find_elements(By.TAG_NAME, "h3")
            #elementList = elements.(By.XPATH , "span")
            resenje = (elements[0].get_attribute("innerHTML"))
            res = resenje.replace("/", " ")
            
            # if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
            # newres=res+char
            for x in res :
              if x.isupper() or x==" " :
                newres=x
              else :
                pass
            
            print(newres)
        except Exception as e:
            print("Error:", e)
#slagalica()
#okrenimojbroj()
spojnice()