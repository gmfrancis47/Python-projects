import os
import shutil

# 📁 Adjust this path to the folder you want to organize
source_folder = os.path.expanduser('~/Documents')

# 📁 Destination folder (where sorted folders will go)
destination_folder = os.path.join(source_folder, 'Sorted')

# 🗂️ Define file types to sort
file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "PDFs": [".pdf"],
    "Text Files": [".txt", ".md"],
    "Python Scripts": [".py"],
    "Other": []  # Everything else
}

# ✅ Make the destination folder
os.makedirs(destination_folder, exist_ok=True)

# 🔁 Loop through all files
for filename in os.listdir(source_folder):
    filepath = os.path.join(source_folder, filename)
    
    # Only deal with files (not folders)
    if os.path.isfile(filepath):
        file_moved = False
        
        for folder_name, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                target_folder = os.path.join(destination_folder, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(filepath, os.path.join(target_folder, filename))
                print(f"Moved {filename} to {folder_name}")
                file_moved = True
                break
        
        # If no extension match, move to "Other"
        if not file_moved:
            target_folder = os.path.join(destination_folder, "Other")
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(target_folder, filename))
            print(f"Moved {filename} to Other")

print("✅ Done organizing files!")
