from lesson3.address import Address
from lesson3.mailing import Mailing

to_address = Address('55555', 'Москва', 'Пушкина', "1", "6")
from_address = Address('66666', 'Владивосток', 'дветыщи', '6', '1')
mailing = Mailing(to_address, from_address, 2000, 'DONTPLS')

print(f'Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city},'
      f' {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment}'
      f' в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street},'
      f'{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.')
