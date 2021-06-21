# Webserver for the SGU Dashboard

## Specifications

- Webserver: Flask
- Client/Server communication protocol: WebSocket
- Message format from SGU to Server: JSON

## Running the server

```
$ python public/app.py
```

This will make the http://localhost:5000 available with the following routes:

- / - Index page
- /dashboard - Dashboard page
- /data_from_sgu - Receive POST requests from SGU on JSON format

## Testing with curl

```
$ curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/data_from_sgu -d '{"id": "3", "time":"HH:MM:SS", "temp" : "36", "mascara" : "nao", "img" : "xxxxxxx"}'

```