def get_var(payment, percent=18):
    try:
        payment = float(payment)
        percent = int(percent)
        vat = payment / 100 * percent
        vat = round(vat, 2)
        return "Сумма НДС: {}".format(vat)
    except (TypeError, ValueError):
        return("Не могу посичтать, проверьте вводимые данные.")

result = get_var(400)
print(result)