from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

with open("alertas.txt", "w") as f:
    for message in consumer:
        data = message.value.decode('utf-8')
        print("Recebido:", data)

        # Filtrar temperatura
        if "temp=" in data:
            temp_value = float(data.split(",")[0].split("=")[1])
            if temp_value > 22:
                alerta = f"ALERTA: Temperatura alta - {temp_value}\n"
                print(alerta.strip())
                f.write(alerta)
