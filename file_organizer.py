import os
import shutil

# Ask the user for a folder path
directory = input("Enter your folder path: ").strip()

# File type categories
file_types = {
    "Images": ['jpg', 'jpeg', 'png'],
    "Documents": ['pdf', 'docx', 'txt'],
    "Media": ['mp3', 'mp4'],
    "Code": ['py', 'c', 'cpp']
}

# Check if the path exists
if not os.path.exists(directory):
    print("❌ The directory path doesn't exist.")
    exit()

# Loop through each file in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    # Only organize files (not subfolders)
    if os.path.isfile(file_path):
        # Get the file extension (in lowercase)
        extension = filename.split(".")[-1].lower()

        # Find the right folder category
        for folder_name, extensions in file_types.items():
            if extension in extensions:
                target_folder = os.path.join(directory, folder_name)

                # Create target folder if it doesn't exist
                os.makedirs(target_folder, exist_ok=True)

                # Move the file
                target_path = os.path.join(target_folder, filename)
                shutil.move(file_path, target_path)
                break
