import pandas
data = pandas.read_csv('app_stats.csv')

payments = list(data['payments'])  # список с числом платежей
installs = list(data['installs'])  # список с числом установок

campaign_weeks = [7, 9, 13, 15, 17, 19, 29, 31, 33, 45]

installs_from_ads = []  # список с числом «рекламных» установок
payments_from_ads = []  # список с числом «рекламных» платежей

for week_number in campaign_weeks:
    installs_from_ads.append(installs[week_number] - installs[week_number - 1])
    payments_from_ads.append(payments[week_number] - payments[week_number - 1])

conversions_from_ads = []  # значения конверсии для «рекламных» установок

for index in range(len(installs_from_ads)):
    conversions_from_ads.append(payments_from_ads[index] / installs_from_ads[index])

# ваш код здесь
ads_install_average_profit = [] # доходы от одной «рекламной» установки

for conversion in conversions_from_ads:
    ads_install_average_profit.append(conversion * 600)

print(ads_install_average_profit)  # выводим результаты на экран