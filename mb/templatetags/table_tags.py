from django import template
import json
import urllib.request
import locale

from mb.models import Malumot

locale.setlocale(locale.LC_NUMERIC, 'uz_UZ.UTF-8')
def format_european(value):
    return locale.format_string("%.1f", value, grouping=True)

register = template.Library()

@register.inclusion_tag('tags/table.html')
def show_table(siat_api_id):
    turi = Malumot.objects.get(raqami=siat_api_id)
    turi = turi.name
    url = f'https://api.siat.stat.uz/media/uploads/sdmx/sdmx_data_{str(siat_api_id)}.json'
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))
            datas = {}
            data = data[0].get('data', [])
            keys = data[0].keys()
            keys_list = list(keys)
            to_remove = ['Klassifikator_en', 'Klassifikator_ru', 'Code', 'Klassifikator']

            # Remove items from list
            filtered_keys = [key for key in keys_list if key not in to_remove]
            last_item = filtered_keys[-1]
            for item in data:
                if item:
                    lists = list(item.keys())
                    item['last_key'] = lists[-1]
                    item['last_value1'] = item[item['last_key']]
                    item['last_value'] = format_european(item['last_value1'])

                    item['to_last_key'] = lists[-2]
                    item['to_last_value'] = item[item['to_last_key']]
                    item['to_last_value'] = item['last_value1']/item['to_last_value']*100-100
                    item['to_last_value'] = format_european(item['to_last_value'])



    except:
        print(f"{id} - xatolik bor")


    return { "data": data,
             'last': last_item,
             'turi': turi
             }
