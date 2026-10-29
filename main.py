import os
import shutil

def organize_directory(target_dir):
    if not os.path.exists(target_dir):
        print(f"Directory {target_dir} does not exist.")
        return

    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Documents': ['.pdf', '.docx', '.txt', '.md', '.csv'],
        'Archives': ['.zip', '.tar', '.gz', '.rar'],
        'Scripts': ['.py', '.js', '.sh', '.json']
    }

    for filename in os.listdir(target_dir):
        if os.path.isdir(os.path.join(target_dir, filename)):
            continue
        
        _, ext = os.path.splitext(filename)
        moved = False
        
        for folder, exts in extensions.items():
            if ext.lower() in exts:
                folder_path = os.path.join(target_dir, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(os.path.join(target_dir, filename), os.path.join(folder_path, filename))
                print(f"Moved: {filename} -> {folder}/")
                moved = True
                break
        
        if not moved:
            other_path = os.path.join(target_dir, 'Others')
            os.makedirs(other_path, exist_ok=True)
            shutil.move(os.path.join(target_dir, filename), os.path.join(other_path, filename))
            print(f"Moved: {filename} -> Others/")

if __name__ == "__main__":
    target = input("Enter path to organize: ")
    organize_directory(target)
