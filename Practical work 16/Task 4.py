cia_agents = set(input('Введите имена агентов из ЦРУ: ').split())
mi6_agents = set(input('Введите имена агентов из МИ-6: ').split())
kgb_agents = set(input('Введите имена агентов из КГБ: ').split())

print('Список пересекающихся агентов в ЦРУ и МИ-6, но неизвестных в КГБ:',
      *cia_agents.intersection(mi6_agents).difference(kgb_agents))

