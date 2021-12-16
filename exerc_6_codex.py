import json
import requests

link = "http://worldclockapi.com/api/json/utc/now"
f = requests.get(link)

# Filtering the information in the link
text = f.text.split(",")

# Separating the data
dataTime = text[1].split('T')
data = dataTime[1].split(":")[1]

#Separating the time
Time = list(dataTime[-1])
Time[1] = str(int(Time[1])-3)
Time = "".join(Time)


def DataTime():
    # Creating dictionary with data and time formatted
    value = {
        "Data": data[1:],
        "Time": Time[:5]
    }
    # Return JSON object
    return json.dumps(value)

print(DataTime())
