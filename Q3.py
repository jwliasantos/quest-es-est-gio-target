import json

# Modelo de dados de faturamento em JSON
faturamento_json = '''
{
    "janeiro": {
        "1": 200.0,
        "2": 250.0,
        "3": 0.0,
        "4": 300.0,
        "5": 0.0,
        "6": 150.0,
        "7": 0.0,
        "8": 400.0,
        "9": 350.0,
        "10": 0.0,
        "11": 450.0,
        "12": 300.0,
        "13": 200.0,
        "14": 0.0,
        "15": 0.0,
        "16": 350.0,
        "17": 300.0,
        "18": 250.0,
        "19": 0.0,
        "20": 400.0,
        "21": 0.0,
        "22": 450.0,
        "23": 300.0,
        "24": 500.0,
        "25": 0.0,
        "26": 600.0,
        "27": 700.0,
        "28": 0.0,
        "29": 800.0,
        "30": 900.0,
        "31": 0.0
    }
}
'''

# Carregar as informações de faturamento
faturamento_data = json.loads(faturamento_json)['janeiro']

# Definir variáveis
faturamentos = [valor for valor in faturamento_data.values() if valor > 0]
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_faturamento = sum(faturamentos) / len(faturamentos)
dias_acima_media = sum(1 for valor in faturamentos if valor > media_faturamento)

# Resultados
print(f'Menor faturamento: R${menor_faturamento:.2f}')
print(f'Maior faturamento: R${maior_faturamento:.2f}')
print(f'Dias com faturamento acima da média: {dias_acima_media}')
