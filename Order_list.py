import pandas as pd
import matplotlib.pyplot as plt 

# Data  cleaning = process of fixing/removing:
#                  incomplete,incorrect and irrelevant data 
#                   75% of the work is done with pandas is data cleaning 




# Read the Excel file
file_path = "C:/Users/Nhlan/OneDrive/Documents/Personal projects/Python/Order_list/order_list.xlsx"

data = pd.read_excel(file_path)


#1.  Drop irrelevent columns
data = data.drop(columns=["Unnamed: 0","Unnamed: 0.1","Unnamed: 0.2"])

# 2.  Handle missing data 
#data = data.dropna(subset=["Unnamed: 0","Unnamed: 0.1"])
#data= data.fillna({"payment_sequential":"5"})

#3. Fix inconsistent values 
data["payment_type"] = data["payment_type"].replace({"credit_card":"Credit Card "})
data["payment_type"] = data["payment_type"].replace({"boleto":"Boleto"})
data["payment_type"] = data["payment_type"].replace({"voucher":"Voucher "})
data["payment_sequential"] = data["payment_sequential"].replace({1:0})


# 4.Standardize text 
#data["payment_type"] = data["payment_type"].str.upper()

# 5. Fix data types
data["payment_sequential"] = data ["payment_sequential"].astype(bool)




#6. remove duplicate values 
data = data.drop_duplicates()

# ✅ Save cleaned data back to Excel
cleaned_path = "C:/Users/Nhlan/OneDrive/Documents/Personal projects/Python/Order_list/order_list_cleaned.xlsx"
data.to_excel(cleaned_path, index=False)
print("✅ Cleaned Excel file saved as:", cleaned_path)

# Show the first few rows
print(data.to_string())
# ✅ Save (overwrite) the cleaned data back to the same Excel file


