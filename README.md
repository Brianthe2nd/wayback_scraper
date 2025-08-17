# Project Setup & Usage Guide

## 1. Download the Project Folder
- Download the project folder from the provided link.  

---

## 2. Install Dependencies (One-Time Setup)
These steps only need to be done **once**.  

### Install Python
1. Open **Command Prompt** (`cmd`).  
2. Run:  
   ```bash
   winget install Python.Python.3
   ```
3. Verify installation:  
   ```bash
   python -V
   ```

### Install Ruby
1. In the same `cmd`, run:  
   ```bash
   winget install RubyInstallerTeam.Ruby
   ```
2. Verify installation:  
   ```bash
   ruby -v
   ```

⚠️ **Note:** If either of the commands to verify installation shows an error, close Command Prompt and open it again, then re-run the version check.

---

## 3. Install Python & Ruby Packages
Navigate into the downloaded folder using `cd` (replace with your folder path).Default path if you installed in Downloads will be:  
```bash
cd Downloads/wayback_scraper
```

Then install the requirements:

### Python requirements
```bash
pip install -r requirements.txt
```

### Ruby gem
```bash
gem install wayback_machine_downloader
```

---

## 4. Unzip the Archive (if present)
If there is a file called `archive.zip` in the project folder, unzip it before running the script.  

You can do this using Python:  
```bash
py -m zipfile -e archive.zip .
```

Or manually:
- Right-click `archive.zip` → **Extract All** → choose the same folder.

---

## 5. Running the Script
Once everything is installed (and the archive is extracted, if present):  
1. Open Command Prompt.  
2. Navigate to the project folder:  
   ```bash
   cd Downloads/wayback_scraper
   ```
3. Run the script:  
   ```bash
   py downloads.py
   ```

---

## ⚠️ Important Warnings
- **Do not delete or move the following files from the project folder:**  
  - `tweets.csv`  
  - `error_tweets.txt`  
  - `errors.txt`  
- These files are required for the script to run correctly.  
- You **only need to install Python, Ruby, and requirements once**. After that, just run:  
  ```bash
  cd Downloads/wayback_scraper
  py downloads.py
  ```
