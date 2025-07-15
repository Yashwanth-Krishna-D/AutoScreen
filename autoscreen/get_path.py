import os

def get_image_paths(image_extensions=['.jpg', '.png', '.jpeg']):
    image_paths = []
    base_folder = 'instagram_screenshots'
    # Walk through the base folder and its subfolders
    for root, dirs, files in os.walk(base_folder):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_paths.append(os.path.join(root, file))

    return image_paths

image_paths = get_image_paths()

# Print all image paths
for path in image_paths:
    print(path)
