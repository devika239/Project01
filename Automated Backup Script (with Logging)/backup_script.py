import os
import zipfile
import datetime
import shutil
import logging


SOURCE_FOLDER = "data"                # Folder to backup (change as needed)
BACKUP_FOLDER = "backups"            # Folder where backups are stored
LOG_FILE = "backup.log"              # Log file name


# Create backup folder if it doesn't exist
os.makedirs(BACKUP_FOLDER, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_backup():
    # Get current timestamp for filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"backup_{timestamp}.zip"
    zip_path = os.path.join(BACKUP_FOLDER, zip_name)

    # Create ZIP archive
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as backup_zip:
        for foldername, subfolders, filenames in os.walk(SOURCE_FOLDER):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                arcname = os.path.relpath(filepath, SOURCE_FOLDER)
                backup_zip.write(filepath, arcname)
                logging.info(f"Backed up: {filepath} as {arcname}")

    # Log backup summary
    backup_size = os.path.getsize(zip_path) / (1024 * 1024)  # in MB
    logging.info(f"Backup created: {zip_name} ({backup_size:.2f} MB)")
    print(f"✅ Backup successful: {zip_path} ({backup_size:.2f} MB)")

# Run the backup
if __name__ == "__main__":
    create_backup()
