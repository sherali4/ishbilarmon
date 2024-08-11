from django import template
import json
import urllib.request
import locale
import copy

from mb.models import Malumot

locale.setlocale(locale.LC_NUMERIC, 'uz_UZ.UTF-8')
def format_european(value):
    return locale.format_string("%.1f", value, grouping=True)

register = template.Library()

@register.inclusion_tag('tags/table.html')
def show_davr(siat_api_id, davr):
    turi = Malumot.objects.get(raqami=siat_api_id)
    turi = turi.name
    url = f'https://api.siat.stat.uz/media/uploads/sdmx/sdmx_data_{str(siat_api_id)}.json'
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))
            data = data[0].get('data', [])
            keys = data[0].keys()
            keys_list = list(keys)
            to_remove = ['Klassifikator_en', 'Klassifikator_ru', 'Code', 'Klassifikator']

            # Remove items from list
            filtered_keys = [key for key in keys_list if key not in to_remove]
            tags = tuple(filtered_keys)

            keys_to_filter = copy.deepcopy(tags)
            key_index = keys_to_filter.index(davr) +1
            cutting = keys_to_filter[0:key_index]
            filtered_keys = cutting

            last_item = filtered_keys[-1]
            try:
                to_last_item = filtered_keys[-2]
            except:
                to_last_item = filtered_keys[-1]

            if last_item == to_last_item:
                teng = 1
                for item in data:
                    if item:
                        item['last_key'] = last_item
                        item['last_value1'] = item[item['last_key']]
                        item['last_value'] = format_european(item['last_value1'])


            else:
                teng = 0
                for item in data:
                    if item:
                        item['last_key'] = last_item
                        item['last_value1'] = item[item['last_key']]
                        tq = item['last_value1']
                        item['last_value'] = format_european(item['last_value1'])
                        item['to_last_key'] = to_last_item
                        item['to_last_value'] = item[item['to_last_key']]
                        item['to_last_value1'] = item[item['to_last_key']]
                        tq1 = item['to_last_value1']
                        item['to_last_value1'] = format_european(item['to_last_value1'])
                        if tq > 0 and tq1 > 0:
                            item['to_last_value'] = item['last_value1'] / item['to_last_value'] * 100 - 100
                            item['to_last_value'] = format_european(item['to_last_value'])
                        else:
                            item['to_last_value'] = '-'


    except:
        print(f"{id} - xatolik bor")




    return { "data": data,
             'last': last_item,
             'turi': turi,
             'tags': tags,
             'siat_api_id': siat_api_id,
             'davr': davr,
             'to_last': to_last_item,
             'teng': teng
             }



@register.inclusion_tag('tags/table.html')
def show_table(siat_api_id, davr = '2022'):
    turi = Malumot.objects.get(raqami=siat_api_id)
    turi = turi.name
    url = f'https://api.siat.stat.uz/media/uploads/sdmx/sdmx_data_{str(siat_api_id)}.json'
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))
            data = data[0].get('data', [])
            keys = data[0].keys()
            keys_list = list(keys)
            to_remove = ['Klassifikator_en', 'Klassifikator_ru', 'Code', 'Klassifikator']

            # Remove items from list
            filtered_keys = [key for key in keys_list if key not in to_remove]
            tags = tuple(filtered_keys)

            keys_to_filter = copy.deepcopy(tags)
            key_index = keys_to_filter.index(davr)+1
            cutting = keys_to_filter[0:key_index]
            filtered_keys = cutting

            last_item = filtered_keys[-1]

            try:
                to_last_item = filtered_keys[-2]
            except:
                to_last_item = filtered_keys[-1]

            if last_item == to_last_item:
                teng = 1
                for item in data:
                    if item:
                        item['last_key'] = last_item
                        item['last_value1'] = item[item['last_key']]
                        item['last_value'] = format_european(item['last_value1'])


            else:
                teng = 0
                for item in data:
                    if item:
                        item['last_key'] = last_item
                        item['last_value1'] = item[item['last_key']]
                        tq = item['last_value1']
                        item['last_value'] = format_european(item['last_value1'])
                        item['to_last_key'] = to_last_item
                        item['to_last_value'] = item[item['to_last_key']]
                        item['to_last_value1'] = item[item['to_last_key']]
                        tq1 = item['to_last_value1']
                        item['to_last_value1'] = format_european(item['to_last_value1'])
                        if tq > 0 and tq1 > 0:
                            item['to_last_value'] = item['last_value1'] / item['to_last_value'] * 100 - 100
                            item['to_last_value'] = format_european(item['to_last_value'])
                        else:
                            item['to_last_value'] = '-'
    except:
        print(f"{id} - xatolik bor")




    return {
             "data": data,
             'last': last_item,
             'turi': turi,
             'tags': tags,
             'siat_api_id': siat_api_id,
             'davr': davr,
             'to_last': to_last_item,
             'teng': teng
             }
