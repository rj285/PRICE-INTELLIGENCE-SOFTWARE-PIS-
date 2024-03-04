import pandas as pd
data = {
    'name': ['apple', 'ice cream', 'carrot', 'orange', 'chocolate', 'broccoli'],
    'price': ['$1', '$23', '$2', '$1.5', '$15', '$3'],
    'unit': ['each', 'pack', 'each', 'each', 'bar', 'bunch'],
    'category': ['fruit', 'dessert', 'vegetable', 'fruit', 'dessert', 'vegetable'],
    'stock': [100, 50, 75, 120, 30, 60],
    'brand': ['FruitCo', 'SweetTreats', 'FarmFresh', 'CitrusDelight', 'ChocoHeaven', 'GreenHarvest'],
    'expiry_date': ['2024-02-15', '2024-03-10', '2024-02-28', '2024-02-20', '2024-04-05', '2024-03-01'],
    'origin': ['USA', 'Italy', 'Local', 'Spain', 'Switzerland', 'Mexico'], 
    'weight': ['150g', '500g', '200g', '200g', '100g', '400g'],
    'discount': ['5%', '10%', '2%', '8%', '15%', '3%'], 
    'is_organic': [True, False, True, False, False, True]
}


df = pd.DataFrame(data)

df.to_csv("sample_data.csv",index=False)