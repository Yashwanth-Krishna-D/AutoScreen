from customtkinter import * 
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import filedialog, messagebox
from fpdf import FPDF
import os
import instagram_main 

root=CTk(fg_color="white")
root.geometry("1440x900")
root.title("AUto Screen")


img_insta=Image.open("insta5.jpg")
img_insta=img_insta.resize((120,120))
img_insta = CTkImage(light_image=img_insta, size=(100, 100))

img_2=Image.open("whatsapp.webp")
img_2=img_2.resize((120,120))
img_2 = CTkImage(light_image=img_2, size=(100, 100))


# Create a frame
frame = CTkFrame(root, width=500, height=900)
frame.place(x=1050,y=0)

# Load and resize the image
img_3 = Image.open("proj.webp")
img_3 = img_3.resize((1000, 5500))  # Resize the image to fit the frame
img_3 = ImageTk.PhotoImage(img_3)

# Create a label with the image and place it in the frame
label = tk.Label(frame, image=img_3)
label.place(x=0, y=0, relwidth=1, relheight=1)

def get_image_paths(image_extensions=['.jpg', '.png', '.jpeg']):
    image_paths = []
    base_folder = 'instagram_screenshots'
    # Walk through the base folder and its subfolders
    for root, dirs, files in os.walk(base_folder):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_paths.append(os.path.join(root, file))

    return image_paths



from PIL import Image
import os

def images_to_pdf(image_paths, output_pdf_path):
    # Open the images and convert them to RGB to ensure PDF compatibility
    image_list = []
    for image_path in image_paths:
        img = Image.open(image_path)
        if img.mode in ('RGBA', 'P'):  # Convert PNG images with transparency to RGB
            img = img.convert('RGB')
        image_list.append(img)

    # Save the images as a PDF
    if image_list:
        image_list[0].save(output_pdf_path, save_all=True, append_images=image_list[1:], quality=100, resolution=100.0)
    print(f"PDF saved successfully at: {output_pdf_path}")
    messagebox.showinfo("Success", f"PDF created successfully: {output_pdf_path}")



def select_folder_and_convert():
    # Path to the folder containing images
    folder_path = "D:\\Web Scraping Selenium\\instagram_screenshots"
    
    # Get the list of image paths
    image_paths = get_image_paths()

    # Create a list of PIL.Image objects
    img_list = []
    for image_path in image_paths:
        if os.path.exists(image_path):
            try:
                pil_image = Image.open(image_path)
                pil_image = pil_image.resize((200, 200))  # Resize the image as needed
                img_list.append(pil_image)
            except Exception as e:
                print(f"Error loading image {image_path}: {e}")

    if img_list:
        output_path = os.path.join(folder_path, "images.pdf")
        images_to_pdf(image_paths, output_path)
    else:
        messagebox.showinfo("No Images Found", "No images found to add to the PDF.")



def clear():
        welcome_label.place_forget()
        username_entry.place_forget()
        pass_entry.place_forget()
        login_button.place_forget()
        error_label.place_forget()
        sign_up.place_forget()
        

        back_button_3.place_forget()
        new_label.place_forget()
        new_password.place_forget()
        user_id.place_forget()
        confirm_password.place_forget()
        name_entry.place_forget()
        continue_user.place_forget()

        ques_label.place_forget()
        insta_button.place_forget()
        whatsapp_button.place_forget()
        back_button_1.place_forget()
        
        say_label.place_forget()
        insta_username.place_forget()
        insta_password.place_forget()
        collect_evidence_button.place_forget()
        back_button_2.place_forget()
        key_text.place_forget()
        keyword_label.place_forget()
        loading_bar.place_forget()

        #scroll_label.place_forget()
        scroll.place_forget()
        back_button_4.place_forget()
        convert_button.place_forget()


def check_login():
        clear()
        ques_label.place(x=304,y=184)
        insta_button.place(x=248,y=296)
        whatsapp_button.place(x=450,y=296)
        back_button_1.place(x=45,y=23)


def back():
    clear()
    login_page()

def login():
    
    username=username_entry.get()
    password=pass_entry.get()
    if username=="" and password=="":
        check_login()
    else:
        error_label.pack(pady=20)

def insta_():
    clear()

    say_label.place(x=304,y=184)
    insta_username.place(x=248,y=296)
    insta_password.place(x=248,y=353)
    keyword_label.place(x=248,y=410)
    key_text.place(x=248,y=480)
    collect_evidence_button.place(x=248,y=650)
    back_button_2.place(x=45,y=23)
    frame.place(x=1050,y=0)
    

def collect():
     insta_user=insta_username.get()
     insta_pass=insta_password.get()
     keys=key_text.get("1.0", "end-1c")
     print(insta_user,insta_pass,keys)
     keys=keys.split(',')
     print(keys)
     return (insta_user,insta_pass,keys)

def signup():
     clear()

     new_label.place(x=304,y=184)
     name_entry.place(x=248,y=300)
     user_id.place(x=248,y=353)
     new_password.place(x=248,y=410)
     confirm_password.place(x=248,y=463)
     continue_user.place(x=248,y=562)
     back_button_3.place(x=820,y=18)

def loading():
    loading_bar.place(x=248,y=720)
    loading_bar.start()
    details=collect()
    instagram_main.scrap(details[0], details[1],details[2])
    
    #list of images
    path_list=get_image_paths()
    img_list=list()

    for i in range(len(path_list)):
        if os.path.exists(path_list[i]):
            
                image=Image.open(path_list[i])
                image = image.resize((200,200))  # Resize the image to fit the frame
                
                image = CTkImage(light_image=image,size=(200,200))
                img_list.append(image)
    clear()
    frame.place_forget()
    print(img_list)
    scroll.place(x=74,y=46)
    back_button_4.place(x=74,y=760)
    convert_button.place(x=1300,y=760)
    for i in range(len(img_list)):
        scroll_label = CTkLabel(scroll,text="", height=1, width=1, image=img_list[i])
        scroll_label.grid(row=i // 3, column=i % 3, padx=10, pady=10)
        


# New User Setup
new_label=CTkLabel(root,text="Setup New User",text_color="black",fg_color="white",height=44,width=373,font=("Helvetica",25),bg_color="white")
name_entry=CTkEntry(root,text_color="black",placeholder_text="First Name",width=484,height=48,border_color="black",fg_color="white",bg_color="black")
user_id=CTkEntry(root,text_color="black",placeholder_text="User ID",width=484,height=48,border_color="black",fg_color="white",bg_color="black")
new_password=CTkEntry(root,text_color="black",placeholder_text="Password",width=484,height=48,show="*",border_color="black",fg_color="white",bg_color="black")
confirm_password=CTkEntry(root,text_color="black",placeholder_text="Confirm Password",width=484,height=48,show="*",border_color="black",fg_color="white",bg_color="black")
continue_user=CTkButton(root,text="Create User",width=484,height=48,border_color="black",fg_color="black",text_color="white",bg_color="black")
back_button_3=CTkButton(root,text="Sign In",command=back,text_color="black",
    fg_color="white",bg_color="black",hover=False,height=29,width=99,border_color="black",border_width=1,corner_radius=0)
     


#Login Page
welcome_label=CTkLabel(root,height=44,width=157,text="Account Log In",text_color="black",font=("Helvetica",25),bg_color="white")
sign_up=CTkButton(root,text="Sign Up",height=29,width=99,text_color="black",
    fg_color="white",bg_color="black",border_color="black",border_width=1,hover=False,corner_radius=0,command=signup)
error_label=CTkLabel(root,text="The username or password you entered is incorrect",text_color="red",fg_color="white",height=44,width=373,font=("Helvetica",15),bg_color="white")
username_entry=CTkEntry(root,text_color="black",
    placeholder_text="username",fg_color="white",bg_color="black",
    height=48,
    width=484
    )
login_button=CTkButton(root,
    text="Login",
    command=login,
    text_color="white",
    fg_color="black",
    bg_color="black",
    hover=False,
    height=48,
    width=484
    )
pass_entry=CTkEntry(root,
    placeholder_text="password",
    show="*",
    fg_color="white",bg_color="black",
    height=48,
    width=484,
    text_color="black"
    )


#instagram
key_text=CTkTextbox(root,text_color="black",height=120,width=484,fg_color="white",border_color="black",border_width=3)
insta_username=CTkEntry(root,text_color="black",placeholder_text="username",fg_color="white",bg_color="black",width=484,height=48)
insta_password=CTkEntry(root,placeholder_text="password",text_color="black",show="*",fg_color="white",bg_color="black",width=484,height=48)

say_label=CTkLabel(root,
    text="Enter the login credentials",
    text_color="black",
    fg_color="white",
    font=("Helvetica",34))

keyword_label=CTkLabel(root,text="Enter the keywords to search",text_color="black",fg_color="white",height=44,width=373,font=("Helvetica",20),bg_color="white")

collect_evidence_button=CTkButton(root,
    text="Collect Evidences",
    text_color="white",
    fg_color="black",
    bg_color="black",
    hover=False,
    height=48,
    width=484,
    command=loading
    )

#choose page
back_button_1=CTkButton(root,text="Back",command=back,text_color="white",
    fg_color="black",bg_color="black",hover=False,height=29,width=105)
ques_label=CTkLabel(root,text="Which social Media do you want to access?",
    text_color="black",
    fg_color="white",
    font=("Helvetica",34),
    bg_color="white")

insta_button=CTkButton(root,text="Instagram",
    height=150,
    width=150,
    image=img_insta,
    fg_color="white",
    bg_color="beige",
    hover_color="silver",
    text_color="black",
    anchor="center",
    compound="top",
    command=insta_,
    font=("Helvetica",14),
    hover=False,
    border_color="black",
    border_width=3
    )

whatsapp_button=CTkButton(root,text="Whatsapp",
    height=150,
    width=150,
    image=img_2,
    fg_color="white",
    bg_color="beige",
    hover_color="silver",
    text_color="black",
    anchor="center",
    compound="top",
    font=("Helvetica",14),
    hover=False,
    border_color="black",
    border_width=3
    )
back_button_2=CTkButton(root,text="Back",command=check_login,text_color="white",
    fg_color="black",bg_color="black",hover=False,height=29,width=105)

# loading screen
loading_bar=CTkProgressBar(root,mode="indeterminate",height=5,fg_color="white",progress_color="black",bg_color="white",width=484,corner_radius=30,)

#preview page
scroll=CTkScrollableFrame(root,width=1310,height=680,fg_color="silver",scrollbar_button_color="black")
label_list=list()
#scroll_label=CTkLabel(scroll,height=150,width=150)
back_button_4=CTkButton(root,text="Back",command=insta_,text_color="white",
    fg_color="black",bg_color="black",hover=False,height=29,width=105)
convert_button = CTkButton(root,text="Dowload PDF",command=select_folder_and_convert,text_color="white",
    fg_color="black",bg_color="black",hover=False,height=29,width=105)




def login_page():
    welcome_label.place(x=412,y=184)
    username_entry.place(x=248,y=310)
    pass_entry.place(x=248,y=371)
    login_button.place(x=248,y=476)
    sign_up.place(x=820,y=18)

login_page()


root.mainloop()