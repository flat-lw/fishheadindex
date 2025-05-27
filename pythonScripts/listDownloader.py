import gspread
import pandas as pd

spreadSheet_url = "https://docs.google.com/spreadsheets/d/1xb9yLv0eAPgBQjisjLrR6ib_Q8pER2loDVIUYnqH8n4/edit"

gc = gspread.service_account(filename="./service_account.json")
sheet = gc.open_by_url(spreadSheet_url).sheet1

data = sheet.get_all_values()

df = pd.DataFrame(data[1:], columns=data[0])

csv_filename = "fishList.csv"
df.to_csv(csv_filename, index=False)

print("complete")
