import requests

pnr = input("Enter PNR: ")

url = "https://irctc1.p.rapidapi.com/api/v3/getPNRStatus"
headers = {
    "x-rapidapi-key": "YOUR_API_KEY",
    "x-rapidapi-host": "irctc1.p.rapidapi.com"
}
params = { "pnrNumber": pnr}
response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()["data"]

    print("Train Name   :", data["TrainName"])
    print("Train Number :", data["TrainNo"])
    print("From Station :", data["SourceName"])
    print("To Station   :", data["DestinationName"])
    print("PNR Status   :", "Chart Prepared" if data["ChartPrepared"] 
          else "Chart Not Prepared")

    print("\nPassenger Details")

    for passenger in data["PassengerStatus"]:
        print("Coach  :", passenger["Coach"])
        print("Seat   :", passenger["Berth"])
        print("Status :", passenger["CurrentStatus"])
        print()
else:
    print("Unable to fetch PNR status.")
