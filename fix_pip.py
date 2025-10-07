#!/usr/bin/env python3
import os

# Define the correct shebang line
correct_shebang = '#!/home/ck/myProjects/ComfyUI/my_env/bin/python3.12'

# Files to fix
pip_files = [
    '/home/ck/myProjects/ComfyUI/my_env/bin/pip',
    '/home/ck/myProjects/ComfyUI/my_env/bin/pip3'
]

for file_path in pip_files:
    if os.path.exists(file_path):
        # Read the file
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        # Replace the first line (shebang) if it's incorrect
        if lines and lines[0].startswith('#!'):
            lines[0] = correct_shebang + '\n'
            
            # Write the file back
            with open(file_path, 'w') as f:
                f.writelines(lines)
            
            print(f"Fixed shebang in {file_path}")
    else:
        print(f"File not found: {file_path}")

print("Done!")