# -*- coding: utf-8 -*-

import ast
import csv
from aroma.models import Aroma, Brand, Note, Nose, AromaCounter, CategoryNotes, Group


def group_import_csv(name='/Users/marinapolyakova/PycharmProjects/fragrantica_parser/фужерные водяные.csv'):
    print('here!')
    keys = (['title', 'description', 'gender', 'designer', 'pic', 'noses', 'year', 'Ноты Аромата', 'верхние Ноты',
             'средние Ноты', 'база Ноты', 'comments'])
    with open(name, 'r') as f:
        reader = csv.DictReader(f, keys)
        next(reader, None)
        for row in reader:
            if row['comments'][0] != '0' or row['year'] and row['year'][0:4] == '2017':
                gender = 'u' if row['gender'] == 'мужчин и женщин' else 'f' if row['gender'] == 'женщин' else 'm'
                brand, _ = Brand.objects.get_or_create(title=row['designer'])
                aroma, _ = Aroma.objects.get_or_create(title=row['title'], gender=gender, brand=brand)
                group, _ = Group.objects.get_or_create(id=6)
                aroma.groups.add(group)
                aroma.pic = row['pic']
                if row['year'] != '':
                    aroma.year = int(row['year'][0:4])
                if row['noses'] != '[]':
                    for nose in ast.literal_eval(row['noses']):
                        nose, _ = Nose.objects.get_or_create(name=nose)
                        aroma.noses.add(nose)
                if row['Ноты Аромата']:
                    for note in ast.literal_eval(row['Ноты Аромата']):
                        note, _ = Note.objects.get_or_create(title=note)
                        note.save()
                        cnote, _ = CategoryNotes.objects.get_or_create(aroma=aroma, note=note, category=CategoryNotes.GENERAL_NOTES)
                        cnote.save()
                if row['верхние Ноты']:
                    for note in ast.literal_eval(row['верхние Ноты']):
                        note, _ = Note.objects.get_or_create(title=note)
                        note.save()
                        cnote, _ = CategoryNotes.objects.get_or_create(aroma=aroma, note=note, category=CategoryNotes.TOP_NOTES)
                        cnote.save()
                if row['средние Ноты']:
                    for note in ast.literal_eval(row['средние Ноты']):
                        note, _ = Note.objects.get_or_create(title=note)
                        note.save()
                        cnote, _ = CategoryNotes.objects.get_or_create(aroma=aroma, note=note, category=CategoryNotes.MIDDLE_NOTES)
                        cnote.save()
                if row['база Ноты']:
                    for note in ast.literal_eval(row['база Ноты']):
                        note, _ = Note.objects.get_or_create(title=note)
                        note.save()
                        cnote, _ = CategoryNotes.objects.get_or_create(aroma=aroma, note=note, category=CategoryNotes.BASE_NOTES)
                        cnote.save()
                aroma.save()
                AromaCounter.objects.get_or_create(aroma=aroma, num_comments=float(row['comments']))


group_import_csv()
# python3 manage.py shell < scripts/import.py
