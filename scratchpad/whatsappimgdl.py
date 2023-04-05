import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the path to the Chrome driver
driver = webdriver.Chrome("/path/to/chromedriver")

# Navigate to WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Wait for the user to scan the QR code and log in
input("Press Enter once you have logged into WhatsApp Web")

# Find all the chats on the screen
chats = driver.find_elements_by_class_name("_2wP_Y")

# Loop through each chat
for chat in chats:
    # Get the name of the chat
    name = chat.find_element_by_class_name("_25Ooe").text
    
    # Check if the chat has unread messages
    unread = chat.find_elements_by_class_name("_1_WHN")
    if len(unread) > 0:
        # Click on the chat to open it
        chat.click()

        # Find all the messages in the chat
        messages = driver.find_elements_by_class_name("_3zb-j")
        for message in messages:
            try:
                # Find the image in the message
                image = message.find_element_by_class_name("_1WliW")
                src = image.get_attribute("src")
                
                # Download the image
                response = requests.get(src)
                with open(f"{name}.jpg", "wb") as f:
                    f.write(response.content)
            except:
                # Not an image, continue
                continue

# Close the browser
driver.close()
