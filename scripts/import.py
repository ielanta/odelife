# -*- coding: utf-8 -*-


def group_import_csv(name='/Users/marinapolyakova/PycharmProjects/odelife/csv_groups/цветочные фруктовые сладкие.csv'):
    import csv
    import ast
    from aroma.models import Aroma, Brand, Note, Nose, AromaCounter, CategoryNotes, Group

    def note_parser(notes, category):
        for note in ast.literal_eval(notes):
            note = note.strip()
            note, _ = Note.objects.get_or_create(title=note)
            note.save()
            cnote, _ = CategoryNotes.objects.get_or_create(aroma=aroma, note=note, category=category)
            cnote.save()

    print('here!')
    keys = (['title', 'description', 'gender', 'designer', 'pic', 'noses', 'year', 'Ноты Аромата', 'верхние Ноты',
             'средние Ноты', 'база Ноты', 'comments'])
    with open(name, 'r') as f:
        reader = csv.DictReader(f, keys)
        next(reader, None)
        for row in reader:
            if (float(row['comments']) > 5) or (row['year'] and row['year'][0:4] == '2017'):
                gender = 'u' if row['gender'] == 'мужчин и женщин' else 'f' if row['gender'] == 'женщин' else 'm'
                brand, _ = Brand.objects.get_or_create(title=row['designer'])
                aroma, _ = Aroma.objects.get_or_create(title=row['title'], gender=gender, brand=brand)
                group, _ = Group.objects.get_or_create(id=5)
                aroma.groups.add(group)
                group, _ = Group.objects.get_or_create(id=9)
                aroma.groups.add(group)
                group, _ = Group.objects.get_or_create(id=15)
                aroma.groups.add(group)
                aroma.pic = row['pic']
                if row['year'] != '':
                    aroma.year = int(row['year'][0:4])
                if row['noses'] != '[]':
                    for nose in ast.literal_eval(row['noses']):
                        nose, _ = Nose.objects.get_or_create(name=nose)
                        aroma.noses.add(nose)
                if row['Ноты Аромата']:
                    note_parser(row['Ноты Аромата'], CategoryNotes.GENERAL_NOTES)

                if row['верхние Ноты']:
                    note_parser(row['верхние Ноты'], CategoryNotes.TOP_NOTES)

                if row['средние Ноты']:
                    note_parser(row['средние Ноты'], CategoryNotes.MIDDLE_NOTES)

                if row['база Ноты']:
                    note_parser(row['база Ноты'], CategoryNotes.BASE_NOTES)

                aroma.save()
                AromaCounter.objects.get_or_create(aroma=aroma, num_comments=float(row['comments']))


group_import_csv()
# python3 manage.py shell < scripts/import.py
