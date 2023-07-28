import decouple

port = int(decouple.config("PORT", 3000))
host = decouple.config("HOST", "0.0.0.0")