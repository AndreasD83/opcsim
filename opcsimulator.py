from opcua import ua, Server
import time

# Starte den OPC-UA-Server
server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4840/")
uri = "http://craziandi.com"
namespace = server.register_namespace(uri)
obj = server.get_objects_node()

# Erstelle ein neues Objekt in der OPC-UA-Namespace
lifebit_object = obj.add_object(namespace, "Production")

# Füge eine Variable hinzu
lifebit_signal = lifebit_object.add_variable(namespace, "lifebit", False)
lifebit_signal.set_writable()

production_signal = lifebit_object.add_variable(namespace, "production", True)
production_signal.set_writable()

counter_signal = lifebit_object.add_variable(namespace, "counter", 0)
counter_signal.set_writable()



# Starte den Server
server.start()

# Aktualisiere die Variable in einer Schleife
while True:
    lifebit_signal.set_value(not lifebit_signal.get_value())
    counter_signal.set_value(counter_signal.get_value()+1)
    time.sleep(1)
