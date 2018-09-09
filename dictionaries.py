catalog_item = {
    "type": "phone",
    "vendor": "Apple",
    "model": "iPhone 7 black",
    "price": 36.5
}
print(catalog_item)

catalog_item['audio_jack'] = False
catalog_item['price'] = 70
print(catalog_item)

print(catalog_item['price'])

item_name = catalog_item['vendor'] + " " + catalog_item['model']
print(item_name)

print("Стоимость телефона: " + str(catalog_item.get('price')))

item_name = catalog_item.get('vendor') + " " + catalog_item.get('model')
print("Название вендора и модели телефона: " + item_name)

discount = "Скидки: {}".format(catalog_item.get('discount', 'Скидок нет'))
print(discount)

'model' in catalog_item

for key, value in catalog_item.items():
    print('{}: {}'.format(key, value))

del catalog_item["price"]
print(catalog_item)

try:
    del catalog_item["discount"]
except KeyError:
    pass
