import os
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from autoscreen import nlp
from autoscreen import ss
from autoscreen import img_process
def sanitize_folder_name(name):
    return ''.join(c if c.isalnum() or c in (' ', '_') else '_' for c in name)

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def extract_image(browser, name):
    try:
        # Ensure folder exists for saving images
        user_folder = os.path.join('instagram_images',sanitize_folder_name(name))
        create_directory(user_folder)

        # Scroll down to load more images if needed
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for images to load

        # Find all images
        images = browser.find_elements(By.TAG_NAME, "img")
        image_urls = [img.get_attribute("src") for img in images if img.get_attribute("src")]

        count = 0
        for image_url in image_urls:
            if image_url:
                try:
                    image_data = requests.get(image_url).content
                    save_as = os.path.join(user_folder, f"image_{count + 1}.jpg")
                    with open(save_as, 'wb') as image_file:
                        image_file.write(image_data)
                    print(f"Image {count + 1} saved as {save_as}")
                    count += 1
                except Exception as e:
                    print(f"Failed to save image {count + 1} from {image_url}: {e}")

        print(f"All images for {name} saved in folder: {user_folder}")
        path_of_img=user_folder
        print(path_of_img)
        img_process.main(path_of_img)
        
    except OSError as e:
        print(f"Error extracting images for {name}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while processing {name}: {e}")

def extract_text(browser, folder_name, name):
    try:
        chat_css_selector = "//div[contains(@class,'html-div xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x6ikm8r x10wlt62')]"
        time.sleep(5)
        messages = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, chat_css_selector)))
        chat_texts = [message.text for message in messages]
        

        # Example NLP usage
        flag = nlp.NLP(chat_texts)  # Call to your NLP function (assumed to be defined in nlp module)
        
        if flag == 1:
            ss.screenshot(browser, name)  # Take screenshot if the flag condition is met
        
    except Exception as e:
        print(f"Error extracting text for {name}: {e}")

def chats(browser, key):
    try:
        user_list_selector = "//div[contains(@class,'x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx x2lwn1j xeuugli x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x168nmei x13lgxp2 x5pf9jr xo71vjh x1lliihq xdj266r x11i5rnm xat24cr x1mh8g0r xg6hnt2 x18wri0h x1l895ks x1y1aw1k xwib8y2 xbbxn1n xxbr6pl')]"

        users = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, user_list_selector))
        )

        for i, user in enumerate(users):
            try:
                user.click()
                name = user.text.split("\n")[0]  # Extract the user's name
                print(f"*******{name}*****")
                extract_text(browser, 'instagram_images', name)
                extract_image(browser, name)

                browser.back()
                time.sleep(2)  # Adding a short delay to ensure the page is ready before the next click

                # Re-fetch the users list because the DOM may have changed after navigation
                users = WebDriverWait(browser, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, user_list_selector))
                )
            except Exception as e:
                print(f"Error processing user {i}: {e}")

    except Exception as e:
        print(f"Error in chats function: {e}")
