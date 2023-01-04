import json

date_arr = []; bid_arr = []; ask_arr = [] 

with open("euro.json") as file:
    content = json.load(file)

for data in content["rates"]:   #sorting data into variables
    for k, v in data.items():
        date_arr.append(data["effectiveDate"])
        bid_arr.append(data["bid"])
        ask_arr.append(data["ask"])
        break

print("\nDate\t\tBuying Rate\t\tSelling Rate")
print("=" * 52)

for date, bid, ask in zip(date_arr, bid_arr, ask_arr):
    print(f"{date}\t{bid}\t\t\t{ask}")