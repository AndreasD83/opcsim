import asyncio
from asyncua import ua, Server

async def main():
    server = Server()

    # Setze den Server-Namen auf "Simulator"
    server.set_server_name("Simulator")

    await server.init()

    # Erstelle einen Namensraum
    uri = "urn:craziandi.server"
    idx = await server.register_namespace(uri)

    # Erstelle ein Objekt mit einer Variable
    obj = await server.nodes.objects.add_object(idx, "production")
    automatic = await obj.add_variable(idx, "automatic", True)
    lifebit = await obj.add_variable(idx, "lifebit", True)
    counter = await obj.add_variable(idx, "counter", 0)
    await lifebit.set_writable()
    await counter.set_writable()

    # Starte den Server
    await server.start()

    print(f"OPC UA Server gestartet. Endpoint: {server.endpoint}")
    try:
        # Keep the server running until interrupted
        while True:
            await asyncio.sleep(1)
            val = await counter.get_value()
            await counter.set_value(val + 1)
            print(f"Variable counter geändert. Neuer Wert: {val+1}")
            
            val = await lifebit.get_value()
            await lifebit.set_value(not(val))
            print(f"Variable lifebit geändert. Neuer Wert: {not(val)}")
    finally:
        # Schließe den Server
        await server.stop()

if __name__ == "__main__":
     asyncio.run(main())
