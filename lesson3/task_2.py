from lesson3.smartphone import Smartphone

catalog = []
phone1 = Smartphone('nokia', '3310', '71782620521')
phone2 = Smartphone('fly', 'DS167', '70950579990')
phone3 = Smartphone('strawberry', 'V19', '74662427817')
phone4 = Smartphone('motorola', 'RAZR V3i', '78753843789')
phone5 = Smartphone('sony ericsson', 'T106', '79321933609')

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.number}')
