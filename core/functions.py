from typing import Union

from core import messages as m

LIMITS_LIST = [2_400_000.00, 5_000_000.00, 20_000_000.00, 50_000_000.00]
PERCENTS_LIST = [13.00, 15.00, 18.00, 20.00, 22.00]

MAX_YEAR_GROSS = 1_000_000_000_000.00
MAX_FLOAT_VALUE = 100_000_000.00


def separate_gross_sum(gross_sum: float) -> list[float]:
    tmp_sum = gross_sum * 12
    separated_list = []
    limits = [0.0] + LIMITS_LIST + [MAX_YEAR_GROSS]

    for i in range(1, len(limits)):
        if tmp_sum <= 0: break
        gross_delta = limits[i] - limits[i - 1]
        amount = min(gross_delta, tmp_sum)
        separated_list.append(amount)
        tmp_sum -= amount

    return separated_list


def calculate_net_sum(gross_sum: float) -> float:
    net_sum = sum(
        elem * (100 - percent) / 100
        for elem, percent in zip(separate_gross_sum(gross_sum), PERCENTS_LIST)
    )
    return net_sum / 12


def separate_net_sum(net_sum: float) -> list[float]:
    tmp_sum = net_sum * 12
    separated_list = []
    limits = [0.0] + LIMITS_LIST + [MAX_YEAR_GROSS]

    for i in range(1, len(limits)):
        if tmp_sum <= 0: break
        net_delta = (limits[i] - limits[i - 1]) * (1 - PERCENTS_LIST[i - 1] / 100)
        amount = min(net_delta, tmp_sum)
        separated_list.append(amount)
        tmp_sum -= amount

    return separated_list


def calculate_gross_sum(net_sum: float) -> float:
    gross_sum = sum(
        elem / (1 - percent / 100)
        for elem, percent in zip(separate_net_sum(net_sum), PERCENTS_LIST)
    )
    return gross_sum / 12


def calculate_net_amount(amount: float, percent_idx: int) -> float:
    return amount * (1 - PERCENTS_LIST[percent_idx] / 100)


def calculate_net_by_month(gross_sum: float) -> list[float]:
    result = []
    limits = LIMITS_LIST + [MAX_YEAR_GROSS]
    remaining = limits[0]
    percent_idx = 0

    for _ in range(12):
        if remaining >= gross_sum:
            remaining -= gross_sum
            result.append(calculate_net_amount(gross_sum, percent_idx))
        else:
            overflow = gross_sum - remaining
            net_total = calculate_net_amount(remaining, percent_idx) + calculate_net_amount(overflow, percent_idx + 1)
            remaining = limits[percent_idx + 1] - limits[percent_idx] - overflow
            percent_idx += 1
            result.append(net_total)

    return result


def get_report_text(gross_sum: float, net_sum: float, report_list: list[float]) -> str:
    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
              'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

    gross_year = gross_sum * 12
    net_year = net_sum * 12
    tax_year = gross_year - net_year
    avg_percent = 100 - (net_year / gross_year) * 100

    num_len = '14'

    def frmt(num):
        return f"{num:{num_len},.2f}".replace(',', ' ')

    text = ['⭐️ Summary',
            '<code>-----------------------------------</code>',
            f'<code>Gross (ср. в мес.): {frmt(gross_sum)}</code>',
            f'<code>Net (ср. в мес.):   {frmt(net_sum)}</code>',
            '',
            f'<code>Gross (в год):      {frmt(gross_year)}</code>',
            f'<code>Net (в год):        {frmt(net_year)}</code>',
            '',
            f'<code>Налог (в год):      {frmt(tax_year)}</code>',
            f'<code>Процент (ср. в год):{frmt(avg_percent)}</code>',
            '',
            '📜 List by month',
            '<code>-----------------------------------</code>']

    for month, amount in zip(months, report_list):
        text.append(f'<code>{month:<9}{frmt(amount)}</code>')

    return '\n'.join(text)


def validate(raw_input: str) -> Union[float, str]:
    if not raw_input.strip():
        return m.no_value_error_text
    try:
        float_value = float(raw_input.replace(' ', ''))
    except ValueError:
        return m.invalid_format_error_text
    if not 0 < float_value < MAX_FLOAT_VALUE:
        formatted_max = f'{MAX_FLOAT_VALUE:,.0f}'.replace(',', ' ')
        return f'{m.invalid_number_error_text}{formatted_max}'
    else:
        return float_value
