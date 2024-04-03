import paho.mqtt.client as mqtt
import turtle

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Yuefan")
client.connect("broker.hivemq.com")

# 初始化Turtle图形设置
turtle.setup(500, 500)  # 设置窗口大小
turtle.penup()  # 提起画笔，以便移动时不画线

def on_message_callback(client_inst, userdata, message):
    valeur = message.payload.decode("ansi")
    print(message.topic + " " + valeur)

    if valeur == "fin":
        turtle.bye()
        exit()
    elif valeur[0] == "p":
        try:
            parts = valeur.split(":")
            x, y = int(parts[1]), int(parts[2])
            turtle.goto(x, y)  # 移动到指定位置
            
            # 如果消息包含温度信息
            000
        except Exception as e:
            print(f"Erreur de position - {e}")
    elif valeur[0] == "c":
        try:
            couleur = valeur.split(":")[1]
            turtle.color(couleur)
        except Exception as e:
            print(f"Erreur de couleur - {e}")
    else:
        print("Erreur : commande inconnue...")

client.on_message = on_message_callback

client.subscribe("hal/val")
client.loop_start()

turtle.mainloop()
