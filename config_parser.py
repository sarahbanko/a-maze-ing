
#função para abrir e ler o arquivo config.txt
def parse_config(filename: str) -> dict:
    #para melhor organização, criamos um dicionario com os pares chave valor do file
    config = {}

    # usamos o with pq ja fecha o arquivo automaticamente depois do uso
    try:
        with open(filename, "r") as file:
            for line in file:
                # ignora os espaços no começo/final da linha e o quebra linha
                line = line.strip()

                # para ignorar cometários e linhas vazias
                if not line or line.startswith("#"):
                    continue

                # para montarmos os pares de chave e valor no dicionário
                key, value = line.split("=")
                config[key] = value
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {filename}")

    return config

# função para validar se todos os parâmetros obrigatórios existem. Mas não valida o seu tipo ainda
def validate_config_keys(config: dict) -> None:
    # chaves obrigatórias pelo subject
    required_keys = [
        "WIDTH",
        "HEIGHT",
        "ENTRY",
        "EXIT",
        "OUTPUT_FILE",
        "PERFECT"
    ]

    for key in required_keys:
        # tratamos o erro para o programa não quebrar por falta de algum parâmetro obrigatório
        if key not in config:
            raise ValueError(f"Missing required key: {key}")

#função para converter os valores do dicionário de str no tipo certo
def convert_config(config: dict) -> dict:

    # usamos variáveis para atualizar o dicionário so se tudo der certo, para não quebrar no meio e ficar com valores corretos e incorretos
    try:
        width = int(config["WIDTH"])
    except ValueError:
        raise ValueError("WIDTH must be an integer")
    if width <= 0:
        raise ValueError("WIDTH must be greater than 0")

    try:
        height = int(config["HEIGHT"])
    except ValueError:
        raise ValueError("HEIGHT must be an integer")
    if height <= 0:
        raise ValueError("HEIGHT must be greater than 0")

    try:
        entry_x, entry_y = config["ENTRY"].split(",")
        entry = (int(entry_x), int(entry_y))
    except ValueError:
        raise ValueError("ENTRY must be in x,y format")

    try:
        exit_x, exit_y = config["EXIT"].split(",")
        exit = (int(exit_x), int(exit_y))
    except ValueError:
        raise ValueError("EXIT must be in x,y format")

    if entry == exit:
        raise ValueError("ENTRY and EXIT must be different")

    if not ((0 <= entry[0] < width) and (0 <= entry[1] < height)):
        raise ValueError("ENTRY is out of bounds")

    if not ((0 <= exit[0] < width) and (0 <= exit[1] < height)):
        raise ValueError("EXIT is out of bounds")

    if config["PERFECT"] == "True":
        perfect = True
    elif config["PERFECT"] == "False":
        perfect = False
    else:
        raise ValueError("PERFECT must be True or False")

    if "SEED" in config:
        try:
            seed = int(config["SEED"])
        except ValueError:
            raise ValueError("SEED must be an integer")

        config["SEED"] = seed

    config["WIDTH"] = width
    config["HEIGHT"] = height
    config["ENTRY"] = entry
    config["EXIT"] = exit
    config["PERFECT"] = perfect

    return config

# função chama todas na ordem correta, para na main chamarmos somente uma e facilitar a reutilização do código
def load_config(filename: str) -> dict:
    config = parse_config(filename)
    validate_config_keys(config)
    config = convert_config(config)

    return config


if __name__ == "__main__":
    config = load_config("config.txt")
    print(config)
