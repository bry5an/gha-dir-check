import os
import sys
import re

ALLOWED_SUBDIRS = {"permissionboundary_policy", "network_firewall_policy"}

def validate_structure():
    base_dir = os.getcwd()

    # Get all top-level directories (excluding .git)
    top_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(d) and d != ".git"]

    # Check that all top-level directories are 12-digit numbers
    for dir_name in top_dirs:
        if not re.fullmatch(r"\d{12}", dir_name):
            print(f"❌ ERROR: Invalid top-level directory: '{dir_name}'. Only 12-digit numeric directories are allowed.")
            return False

        # Get subdirectories
        sub_dirs = [d for d in os.listdir(dir_name) if os.path.isdir(os.path.join(dir_name, d))]

        # Check that subdirectories are only from the allowed set
        for subdir in sub_dirs:
            if subdir not in ALLOWED_SUBDIRS:
                print(f"❌ ERROR: Invalid subdirectory '{subdir}' inside '{dir_name}'.")
                print("   Only 'permissionboundary_policy' and 'network_firewall_policy' are allowed.")
                return False

    print("✅ Directory structure is valid.")
    return True

if __name__ == "__main__":
    if not validate_structure():
        sys.exit(1)
