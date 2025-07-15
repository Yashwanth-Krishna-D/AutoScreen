import os
import warnings
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image


''' The above are the modules imported for the following functions:

#Os - To interact with files and directories in the system
#Warnings - To manipulate the warning messages with issues and to supress them
#transformers - It is a powerful library speacally designed for image captioning and recognition
#Blip - Bootstrapped Language Image Pre-Processor
#BlipProcessor - It is a processor for BlipModel which formats the input images such that it can be taken by the model
#BlipForConditionalGeneration - Model which returns the caption for the input image'''


# Suppress warnings
warnings.filterwarnings("ignore")

# Load the pretrained processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


''' The above are the created model and processor from the BLIP transformers:

#BlipProcessor.from_pretrained - loads the pretrained processor for the data set which handles the format and tokenization of image
#BlipForConditionalGeneration.from_Pretrained - loads the pretrained blip model '''


# Function to generate captioning:
def generateCaptioning(imagePath):
    try:
        image = Image.open(imagePath).convert("RGB")
        inputs = processor(image, return_tensors="pt")
        output = model.generate(**inputs)
        caption = processor.decode(output[0], skip_special_tokens=True)
        return caption
    
    except Exception as e:
        raise Exception(f"Error processing the image: {e}")


'''The above function generateCaptioning does the following tasks :

#imagePath - takes the path of the image from the database
#.convert(RGB) - formating to make all the input image to RedGreenBlue format
#return_tensors = pt - takes the input image and convert them to tensors specifically pytorch tensors
#tensors - multidimensional matrix that holds the images
#model generates the output in the encoded form
#.decode - decodes the encoded scrip and stores in the variable caption '''


# Function to access the file from the given folder:
def processImageFromFolder(folderPath):
    captions = []
    for fileName in sorted(os.listdir(folderPath)):
        if fileName.lower().endswith(('.png', '.jpg', '.jpeg')):
            imagePath = os.path.join(folderPath, fileName)
            caption = generateCaptioning(imagePath)
            captions.append(f"{fileName} : {caption}")
    return "\n".join(f"{index}) {caption}" for index, caption in enumerate(captions, 1))


'''The above function processImageFromFolder does the folowing taks:

#for loop - takes the fileName from the folder given
#if conditon - check if the file is a image
#imagePath - creates the image path using the join function which joins the os path, folder path and the file name
#generateCaptioning(imagePath) calls the function to generate the caption using the found imagePath
#.append - Adds the caption with the respective file name as a string to the array captions
#return - Joins all captions into a single string, enumerating them for easy reading.
#enumerate - to print the index and captions as a tuple and auto incrementation'''


# Main function:
def main(path):
    folderPath = path
    #input("Enter the path of the folder: ").strip()
    
    if not os.path.isdir(folderPath):
        print("The specified folder path does not exist")
        return
    
    Captions = processImageFromFolder(folderPath)
    captions = "A pyscho person kills another person bitchfully"
    print("\nGenerated Captions:\n")
    print(Captions)
    cap=list(Captions)
    return cap



    

'''The above main function does the following functions:
#folderPath - the user entered folderPath
#check whether the mentioned folder path is present in the Os directories
#processImageFromFolder - pass the folderPath as parameter to call the processImageFromFolder
#print the captions in the required format '''