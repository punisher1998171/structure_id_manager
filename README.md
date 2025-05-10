# 🏗️ Structure ID Manager

A simple and efficient terminal-based Python application that allows you to **create**, **view**, **update**, and **delete** structure IDs — all synced with a local CSV file and mirrored as folders on your filesystem. Ideal for infrastructure inspection workflows and asset documentation.

---

## 📂 Features

- ➕ Add new structure IDs
- 📄 View all saved IDs
- ✏️ Update existing structure IDs (with optional folder rename)
- ❌ Delete structure IDs (with optional folder deletion)
- 📁 Automatically generate folders for each ID
- 🔁 Regenerate all missing folders from existing IDs
- 🧾 Auto-saves data in `Structure ID.csv`

---

## 💡 How It Works

The app manages structure IDs in a CSV file (`Structure ID.csv`) and creates corresponding folders under a root directory called `Structure IDs`. All actions are performed through the terminal menu.

---

## 🚀 Getting Started

### 🔧 Prerequisites

Ensure you have **Python 3** and **pandas** installed.

Install `pandas` via pip if needed:

```
pip install pandas
```

---

### 📥 Cloning the Repository

```
git clone https://github.com/punisher1998171/structure-id-manager.git
cd structure-id-manager
python structure_id_manager.py
```

---

## 🧪 Example Use

```
🛠️ Welcome to Structure ID Manager 🛠️

Choose an option:
1. Add Structure ID
2. View All IDs
3. Update ID
4. Delete ID
5. Generate Folders
6. Exit

Enter your choice (1-6): 1
Enter the new ID: STR-01-1232
✅ Structure ID added successfully!
✅ Structure ID folders created successfully!
```

---

## 📁 Folder & Data Structure

### CSV File (`Structure ID.csv`)

```
Structure ID
STR-01-1232
STR-01-1233
...
```

### Folder Structure (`Structure IDs/`)

```
Structure IDs/
├── STR-01-1232/
├── STR-01-1233/
...
```

- Folders are automatically created or renamed based on structure ID changes.
- If the folder doesn’t exist, it will be created upon adding or via the “Generate Folders” option.
- Folder deletion is optional when deleting a structure ID.

---

## 🧠 Notes

- Duplicate ID entries are not allowed.
- All inputs are automatically converted to uppercase.
- Missing CSV or folder directories are created automatically.
- Safe and interactive prompts guide every action.
