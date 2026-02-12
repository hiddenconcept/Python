import os

# Specify your target directory
base_path = r"C:\Users\katch\Desktop\50 Days OF Data Analysis With Python"  # Change this path

# Create folders Day1 through Day50
for i in range(1, 51):
    folder_path = os.path.join(base_path, f"Day {i}")
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created: {folder_path}")

print("\nAll 50 folders created successfully!")