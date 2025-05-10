import pandas as pd
import os
import shutil

def load_ids():
    try:
        df = pd.read_csv("Structure ID.csv", dtype=str)
        df["Structure ID"] = df["Structure ID"].str.strip().str.upper()
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["Structure ID"])

def save_ids(str_ids_df):
    str_ids_df.to_csv("Structure ID.csv", index=False)

def create_id():
    str_ids_df = load_ids()
    
    print("\n[Add Structure ID]\n")
    
    while True:
        new_id = input("Enter the new ID: ").upper()
        if new_id == "":
            print("⚠️ You haven't entered a value! Please try again.")
        elif new_id in str_ids_df["Structure ID"].values: 
            print("⚠️ Structure ID already exists! Please try again.")
        else:
            break
    
    str_ids_df = pd.concat([str_ids_df, pd.DataFrame([{"Structure ID" : new_id}])], ignore_index=True)
    save_ids(str_ids_df)
    print(str_ids_df)
    print("✅ Structure ID added successfully!")
    gen_folders()

def read_ids():
    str_ids_df = load_ids()
    print("\n[View All Structure IDs]\n")
    if str_ids_df.empty:
        print("⚠️ No Structure IDs available.")
    else:
        print(str_ids_df.to_string(index=False))

def update_id():
    str_ids_df = load_ids()
    
    print("\n[Update Structure ID]\n")
    
    if str_ids_df.empty:
        print("⚠️ No Structure IDs available.")
        return

    while True:
        cur_id = input("Enter the ID you want to update: ").upper()
        if cur_id == "":
            print("⚠️ You haven't entered a value! Please try again.")
        elif cur_id not in str_ids_df["Structure ID"].values:
            print("⚠️ Structure ID not found! Please try again.")
        else:
            break

    while True:
        new_id = input("Enter the new ID: ").upper()
        if new_id == "":
            print("⚠️ You haven't entered a value! Please try again.")
        elif new_id in str_ids_df["Structure ID"].values:
            print("⚠️ Structure ID already exists! Please enter a different ID.")
        else:
            break

    while True:
        isUpdateFolder = input("Do you want to update the folder name of this structure as well? (Y for Yes, N for No) ").upper()
        cur_folder_id = f"./Structure IDs/{cur_id}"
        if isUpdateFolder == "Y":
            if os.path.exists(cur_folder_id):
                os.rename(cur_folder_id,f"./Structure IDs/{new_id}")
                print("✅ Structure ID folder updated successfully!")
                print(f"The directories in the 'Structure IDs' folder are {os.listdir("./Structure IDs")}\n")
                break
            else:
                print("⚠️ No folder with this structure ID available.")
                break
        elif isUpdateFolder == "N":
            break
        else:
            print("⚠️ You haven't entered a correct answer! Please try again.")

    index = str_ids_df.index[str_ids_df["Structure ID"] == cur_id][0]
    str_ids_df.at[index, "Structure ID"] = new_id
    save_ids(str_ids_df)

    print("✅ Structure ID updated successfully!")
    read_ids()

def delete_id():
    str_ids_df = load_ids()
    
    print("\n[Delete Structure ID]\n")
    
    if str_ids_df.empty:
        print("⚠️ No Structure IDs available.")
    else:
        cur_id = input("Enter the ID you want to delete: ").upper()
        
        if cur_id in str_ids_df["Structure ID"].values:
            index = str_ids_df.index[str_ids_df["Structure ID"] == cur_id][0]
            
            isDeleteFolder = input("Do you want to delete the folder of this structure as well? (Yes or No) ").upper()
            cur_folder_id = f"./Structure IDs/{cur_id}"
            if isDeleteFolder == "YES" or isDeleteFolder == "Y":
                if os.path.exists(cur_folder_id):
                    shutil.rmtree(cur_folder_id)
                    print("✅ Structure ID folder deleted successfully!")
                    print(f"The directories in the 'Structure IDs' folder are {os.listdir("./Structure IDs")}\n")
            else:
                print("No folder was deleted.")
                
            str_ids_df = str_ids_df.drop(index=index)
            save_ids(str_ids_df)
            print("✅ Structure ID deleted successfully!")
            read_ids()
        else:
            print("⚠️ Structure ID not found.")
            
def gen_folders():
    str_ids_df = load_ids()
    print("\n[Generate Folders Using the Available Structure IDs]\n")
    if str_ids_df.empty:
        print("⚠️ No Structure IDs available.")
    else:
        folders_created = False
        for i in range(0, len(str_ids_df)):
            if os.path.exists(f"Structure IDs/{str_ids_df["Structure ID"][i]}"): 
                next
            else:
                os.makedirs(f"Structure IDs/{str_ids_df["Structure ID"][i]}")
                folders_created = True
        
        if folders_created:
            print("✅ Structure ID folders created successfully!")
            print(f"The directories in the 'Structure IDs' folder are {os.listdir("./Structure IDs")}")
        else:
            print("All folders are already created, add a new structure to create the folder.")
            print(f"The directories in the 'Structure IDs' folder are {os.listdir("./Structure IDs")}")
     
def main():
    print("🛠️ Welcome to Structure ID Manager 🛠️\n")

    while True:
        print("\nChoose an option:")
        print("1. Add Structure ID")
        print("2. View All IDs")
        print("3. Update ID")
        print("4. Delete ID")
        print("5. Generate Folders")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            create_id()
        elif choice == "2":
            read_ids()
        elif choice == "3":
            update_id()
        elif choice == "4":
            delete_id()
        elif choice == "5":
            gen_folders()
        elif choice == "6":
            print("\nExiting... Goodbye! 👋")
            break
        else:
            print("⚠️ Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()