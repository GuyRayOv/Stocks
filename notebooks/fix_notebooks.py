import os
import json
import shutil


def fix_notebooks():
    # Get all .ipynb files in the current directory
    notebooks = [f for f in os.listdir('.') if f.endswith('.ipynb')]

    if not notebooks:
        print("No .ipynb files found in the current directory.")
        return

    print(f"Found {len(notebooks)} notebooks. Starting repair...\n")

    for filename in notebooks:
        try:
            # 1. Create a backup
            backup_name = filename + '.bak'
            shutil.copy(filename, backup_name)

            # 2. Load the notebook JSON
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 3. Check for the issue and fix
            fixed = False
            if 'metadata' in data and 'widgets' in data['metadata']:
                del data['metadata']['widgets']
                fixed = True

            # 4. Save if changes were made
            if fixed:
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=1)
                print(f"[FIXED] {filename} (Backup saved as {backup_name})")
            else:
                # Clean up backup if no fix was needed
                os.remove(backup_name)
                print(f"[OK]    {filename} (No widgets metadata found)")

        except Exception as e:
            print(f"[ERROR] Could not process {filename}: {e}")

    print("\nAll operations complete.")


if __name__ == "__main__":
    fix_notebooks()