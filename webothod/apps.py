from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    name = 'webothod.components.companies'
    verbose_name = 'Компании'


class DictsConfig(AppConfig):
    name = 'webothod.components.dicts'
    verbose_name = 'Словари'


class WasteCodesConfig(AppConfig):
    name = 'webothod.components.waste_codes'
    verbose_name = 'Коды отходов'


class QueriesConfig(AppConfig):
    name = 'webothod.components.queries'
    verbose_name = 'Заявки'
