# 🏗️ Structure ID Manager
A simple terminal-based Python application that allows you to **create**, **view**, **update**, and **delete** structure IDs using a local CSV file. Ideal for infrastructure and asset management systems documentation.

---

## 📂 Features

- ➕ Add new structure IDs  
- 📄 View all saved IDs  
- ✏️ Update existing structure IDs  
- ❌ Delete specific structure IDs  
- 🧾 Automatically loads and saves from `Structure ID.csv`  

---

## 💡 How It Works

The app manages structure IDs in a CSV file named `Structure ID.csv`. All operations are performed via the terminal/command line.

---

## 🚀 Getting Started

### 🔧 Prerequisites

Make sure you have **Python 3** and **pandas** installed.

Install `pandas` if needed:
```
pip install pandas
```

## 📥 Cloning the Repository

To clone this repository to your local machine:

```
git clone https://github.com/punisher1998171/structure-id-manager.git
cd structure-id-manager
python structure_id_manager.py
```

---

## 📘 Example Use

```
🛠️ Welcome to Structure ID Manager 🛠️

Choose an option:
1. Add Structure ID
2. View All IDs
3. Update ID
4. Delete ID
5. Exit

Enter your choice (1-5): 1
Enter the new ID: STR-01-1232
✅ Structure ID added successfully!
```

---

## 📁 Data File Format

The application uses a single CSV file named `Structure ID.csv` with the following structure:

```
Structure ID
STR-01-1232
STR-01-1233
...
```

If the file does not exist, it will be created automatically.

---

## 📌 Notes

- The script ensures that no duplicate IDs are added.
- All inputs are automatically converted to uppercase for consistency.
- Empty states are handled gracefully (e.g. no IDs yet, no ID entered).
