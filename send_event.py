import requests
import json

event = {
    "id": "sample-id",
    "eventType": "recordInserted",
    "subject": "sample-subject",
    "eventTime": "2024-07-02T15:28:51.1234567Z",
    "data": {
        "message": "This is a sample event"
    },
    "dataVersion": "1.0"
}


headers = {
    "Content-Type": "application/json",
    "Content-Length": str(len(event)),
    "host": "localhost:7071",
    "aeg-event-type": "Notification"
}

response = requests.post("http://localhost:7071/runtime/webhooks/EventGrid?functionName=displayLogs",
                         headers=headers, data=json.dumps([event]))

print(response.status_code)
print(response.text)
