import io
import json

stat_names = [
    'durability',
    'armor_durability',
    'enchantability',
    'harvest_level',
    'harvest_speed',
    'melee_damage',
    'magic_damage',
    'attack_speed',
    'armor',
    'armor_toughness',
    'magic_armor',
    'ranged_damage',
    'ranged_speed',
    'chargeability'
]

metals = {
    "copper": [175, 8, 12, 1, 4, 1, 2, 0.3, 10, 0, 4, 0, 0.2, 1.3],
    "tin": [240, 13, 10, 2, 5, 1.5, 1, 0, 12, 0, 1, 0.5, 0, 0.9],
    "silver": [200, 7, 16, 1, 6, 2, 3, 0.1, 14, 0, 10, 1, 0.1, 1.5],
    "lead": [150, 6, 8, 2, 5, 1.5, 0.5, -0.3, 12, 0, 2, 1, -0.1, 0.8],
    "nickel": [300, 14, 13, 2, 7, 3, 1.5, 0.1, 12, 0, 6, 0, -0.2, 1.0],
    "platinum": [900, 21, 14, 3, 12, 4, 4, 0, 18, 2, 12, 1, 0, 1.2],
    "aluminum": [300, 14, 10, 2, 7, 2.5, 1, 0.4, 15, 0, 3, 1.5, -0.1, 1.1],
    "zinc": [200, 6, 11, 1, 3, 1.5, 2.5, 0.1, 12, 0, 5, 0, -0.1, 0.9],
    "titanium": [1600, 37, 12, 3, 8, 6, 1, 0, 24, 4, 4, 1, -0.2, 1.2],
    "osmium": [500, 14, 10, 2, 7, 4, 2, 0.1, 17, 0, 5, 1, 0, 1.1],
    "bronze": [500, 18, 14, 2, 6, 3, 1, 0.1, 17, 2, 6, 2, 0, 1.3],
    "brass": [200, 8, 14, 2, 5, 1, 2.5, 0.1, 12, 0, 10, 0, 0.2, 1.6],
    "steel": [1000, 27, 9, 2, 8, 4, 1.5, -0.2, 20, 4, 6, 2.5, 0, 1.0],
    "invar": [450, 17, 10, 2, 7, 2.5, 3, 0, 18, 2, 6, 2, 0, 1.1],
    "electrum": [100, 10, 20, 2, 14, 1.5, 4, 0.3, 15, 0, 10, 1, 0.3, 1.5],
    "enderium": [1100, 34, 13, 4, 18, 6, 4, 0, 22, 4, 8, 3, 0, 1.3]
}

colors = {
    "copper": "FF8000",
    "tin": "FFFFCC",
    "silver": "D4D4D4",
    "lead": "B494D4",
    "nickel": "FFCC99",
    "platinum": "B3B3FF",
    "aluminum": "FFFFFF",
    "zinc": "DDCCFF",
    "titanium": "2E4CE6",
    "osmium": "92A6B8",
    "bronze": "FF5400",
    "brass": "FFAA33",
    "steel": "606060",
    "invar": "D5FFCC",
    "electrum": "FFFF80",
    "enderium": "468C75"
}

tiers = {
    "copper": 1,
    "tin": 1,
    "silver": 2,
    "lead": 2,
    "nickel": 2,
    "platinum": 3,
    "aluminum": 2,
    "zinc": 1,
    "titanium": 3,
    "osmium": 2,
    "bronze": 2,
    "brass": 2,
    "steel": 2,
    "invar": 2,
    "electrum": 2,
    "enderium": 4,
}


def get_json(metal: str):
    colorStr = '#' + colors[metal]
    data = {
        'type': 'silentgear:main',
        'traits': [
            {
                'name': 'silentgear:malleable',
                'level': 2
            }
        ],
        'crafting_items': {
            'normal': {
                'tag': 'forge:ingots/' + metal
            },
            'small': {
                'tag': 'forge:nuggets/' + metal,
                'size': 9
            }
        },
        'name': {
            'translate': False,
            'name': metal[0].upper() + metal[1:]
        },
        'textures': {
            'all': {
                'texture_domain': 'silentgear',
                'texture_suffix': 'generic_hc',
                'normal_color': colorStr,
                'broken_color': colorStr
            }
        },
        'availability': {
            'tier': tiers[metal]
        }
    }

    partStats = []
    for name, value in zip(stat_names, metals[metal]):
        partStats.append({
            'name': name,
            'value': value
        })

    data['stats'] = partStats
    return data


if __name__ == '__main__':
    for metal in metals:
        data = get_json(metal)
        with open('output/' + metal + '.json', 'w', encoding='utf8') as f:
            json.dump(data, f, indent=4, sort_keys=True)
