from web3 import Web3

# Conectar a un nodo de la red Goerli
infura_url = "https://goerli.infura.io/v3/tu_api_key"  # Sustituye con tu propia API Key de Infura
web3 = Web3(Web3.HTTPProvider(infura_url))

# Verificar la conexión
if web3.isConnected():
    print("Conexión exitosa a Ethereum")
else:
    print("Error al conectar")
