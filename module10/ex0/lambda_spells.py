def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_power = max(mages, key=lambda x: x["power"])
    min_power = min(mages, key=lambda x: x["power"])

    total_power = sum(map(lambda x: x["power"], mages))
    avg_power = round(total_power / len(mages), 2)

    return {

        'max_power': max_power["power"],
        'min_power': min_power["power"],
        'avg_power': avg_power
    }


if __name__ == "__main__":

    artifacts = [
        {"name": "Fire Staff", "power": 27, "type": "focus"},
        {"name": "Wind Cloak", "power": 83, "type": "accessory"},
        {"name": "Light Prism", "power": 55, "type": "armor"},
        {"name": "Storm Crown", "power": 16, "type": "weapon"},
    ]

    mages = [
        {"name": "Alex", "power": 34, "elements": "lightning"},
        {"name": "Storm", "power": 72, "elements": "wind"},
        {"name": "Nova", "power": 49, "elements": "shadow"},
        {"name": "Railey", "power": 97, "elements": "ice"},
    ]

    spells = ["fireball", "heal", "freeze", "tsunami"]

    sorted_ = artifact_sorter(artifacts)

    for item in sorted_:
        print(f"{item['name']} ({item['power']} power)")

    print()
    filtered = power_filter(mages, 50)

    for item in filtered:
        print(item)

    print()
    transformed = spell_transformer(spells)

    for i in transformed:
        print(i)

    print()
    max_, min_, avg_ = mage_stats(mages).values()

    print(f"max_power: {max_}, min_power: {min_}, avg_power: {avg_}")
