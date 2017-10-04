def first_original_import_csv(name='/Users/marinapolyakova/PycharmProjects/odelife/csv_groups/1st-originalru_products_20170911_013618.csv'):
    import csv

    from aroma.models import Aroma
    from collaboration.models import Interaction
    from functools import reduce
    from operator import and_
    from django.db.models import Q

    print('here!')
    aroma_query = Aroma.objects.filter(is_public=True)
    keys = (['available', 'categoryId', 'country_of_origin', 'currencyId', 'delivery', 'delivery-options', 'description',
             'id', 'manufacturer_warranty',
             'market_category', 'model', 'modified_time', 'name', 'oldprice', 'param', 'picture', 'price', 'sales_notes',
             'type', 'typePrefix', 'url', 'vendor'])
    with open(name, 'r') as f:
        reader = csv.DictReader(f, keys, delimiter=';')
        next(reader, None)
        for row in reader:
            if row['name'] and row['vendor'] and int(row['price']) > 1000 and \
                            row['typePrefix'] in ['Набор', 'Парфюмерная вода', 'Туалетная вода', 'Духи', 'Одеколон']:
                aromas = aroma_query.filter(reduce(and_, [Q(title__icontains=row['name']),
                                                          Q(brand__title__icontains=row['vendor'])]))
                for aroma in aromas:
                    if row['name'].lower() == aroma.title.lower() or aroma.brand.title.lower() + ' ' + row['name'].lower() == aroma.title.lower():
                        interaction = Interaction.objects.filter(aroma=aroma).first()
                        if not interaction:
                            interaction, _ = Interaction.objects.get_or_create(name=row['name'], aroma=aroma, link=row['url'],
                                                                               price=row['price'], item_id=row['id'])
                        elif interaction.price > int(row['price']):
                            interaction.price = row['price']
                            interaction.item_id = row['id']
                        interaction.save()


first_original_import_csv()
#  python3 manage.py shell < scripts/1st_original.py
