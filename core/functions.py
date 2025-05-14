LIMITS_LIST = [2_400_000.00, 5_000_000.00, 20_000_000.00, 50_000_000.00]
PERCENTS_LIST = [13.00, 15.00, 18.00, 20.00, 22.00]


def separate_gross_sum(gross_sum: float) -> list[float]:
    tmp_sum = gross_sum * 12
    separated_list = []
    i = 1
    tmp_limits_list = [0.00] + LIMITS_LIST + [1_000_000_000_000.00]
    while tmp_sum > 0:
        tmp_delta = tmp_limits_list[i] - tmp_limits_list[i - 1]
        tmp_remainder = tmp_sum - tmp_delta
        if tmp_remainder > 0:
            separated_list.append(tmp_delta)
            i += 1
        else:
            separated_list.append(tmp_sum)
        tmp_sum = tmp_remainder
    return separated_list


def calculate_net_sum(gross_sum: float) -> float:
    net_sum = 0
    i = 0
    for elem in separate_gross_sum(gross_sum):
        net_sum += elem * (100 - PERCENTS_LIST[i]) / 100
        i += 1
    return net_sum / 12


def separate_net_sum(net_sum: float) -> list[float]:
    tmp_sum = net_sum * 12
    separated_list = []
    i = 1
    tmp_limits_list = [0.00] + LIMITS_LIST + [1_000_000_000_000.00]
    while tmp_sum > 0:
        tmp_delta = (tmp_limits_list[i] - tmp_limits_list[i - 1]) * (100 - PERCENTS_LIST[i - 1]) / 100
        tmp_remainder = tmp_sum - tmp_delta
        if tmp_remainder > 0:
            separated_list.append(tmp_delta)
            i += 1
        else:
            separated_list.append(tmp_sum)
        tmp_sum = tmp_remainder
    return separated_list


def calculate_gross_sum(net_sum: float) -> float:
    gross_sum = 0
    i = 0
    for elem in separate_net_sum(net_sum):
        gross_sum += elem / ((100 - PERCENTS_LIST[i]) / 100)
        i += 1
    return gross_sum / 12


def calculate_net_by_month(gross_sum: float) -> list[float]:
    i = 0
    count = 0
    tmp_limits_list = LIMITS_LIST + [1_000_000_000_000.00]
    tmp_delta = tmp_limits_list[i]
    result_list = list()
    while count < 12:
        if tmp_delta >= gross_sum:
            tmp_delta -= gross_sum
            result_list.append(gross_sum * (100 - PERCENTS_LIST[i]) / 100)
        else:
            remain_delta = gross_sum - tmp_delta
            remain = tmp_delta * (100 - PERCENTS_LIST[i]) / 100
            i += 1
            tmp_delta = tmp_limits_list[i] - tmp_limits_list[i - 1] - remain_delta
            remain_delta = remain_delta * (100 - PERCENTS_LIST[i]) / 100
            result_list.append(remain_delta + remain)
        count += 1
    return result_list


def get_report_text(gross_sum: float, net_sum: float, report_list: list[float]) -> str:
    months_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                   'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    number_len = '14'

    avg_percent = 100 - ((net_sum * 12) / (gross_sum * 12)) * 100
    tax_by_year = gross_sum * 12 - net_sum * 12
    gross_by_year = gross_sum * 12
    net_by_year = net_sum * 12

    text = f'⭐️ Summary\n'
    text += f'<code>-----------------------------------</code>\n'
    text += f'<code>Gross (ср. в мес.): {f"{gross_sum:,.2f}":>{number_len}}</code>\n'
    text += f'<code>Net (ср. в мес.):   {f"{net_sum:,.2f}":>{number_len}}</code>\n\n'
    text += f'<code>Gross (в год):      {f"{gross_by_year:,.2f}":>{number_len}}</code>\n'
    text += f'<code>Net (в год):        {f"{net_by_year:,.2f}":>{number_len}}</code>\n\n'
    text += f'<code>Налог (в год):      {f"{tax_by_year:,.2f}":>{number_len}}</code>\n'
    text += f'<code>Процент (ср. в год):{f"{avg_percent:,.2f}":>{number_len}}</code>\n\n'

    text += '📜 List by month\n'
    text += '<code>-----------------------------------</code>\n'
    for i in range(12):
        text += f'<code>{months_list[i]:<9}{f"{report_list[i]:,.2f}":>{number_len}}</code>\n'

    text = text.replace(',', ' ')
    return text
