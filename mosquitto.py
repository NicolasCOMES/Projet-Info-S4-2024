import paho.mqtt.client as mqtt
import turtle

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "vgi")
'#client.connect("srv-lora.isep.fr")'
client.connect("broker.hivemq.com")


def on_message_callback(client_inst, userdata, message):
    valeur = message.payload.decode("ansi")
    print(message.topic + " " + valeur)

    if valeur == "fin":
        turtle.bye()
        exit()
    elif valeur[0] == "p":
        try:
            xy = valeur.split(":")
            turtle.goto(int(xy[1]), int(xy[2]))
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
