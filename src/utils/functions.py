from src.config.bot_config import config as cfg

from src.texts import messages as m


def calculate_net_amount(amount: float, percent_idx: int) -> float:
    return amount * (1 - cfg.PERCENTS_LIST[percent_idx] / 100)


def calculate_net_by_month(gross_sum: float) -> list[float]:
    result = []
    limits = cfg.LIMITS_LIST + [cfg.MAX_YEAR_GROSS]
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


def validate(raw_input: str) -> float | str:
    if not raw_input.strip():
        return m.NO_VALUE_REASON_TEXT
    try:
        float_value = float(raw_input.replace(' ', ''))
    except ValueError:
        return m.INVALID_FORMAT_REASON_TEXT
    if not 0 < float_value < cfg.MAX_FLOAT_VALUE:
        formatted_max = f'{cfg.MAX_FLOAT_VALUE:,.0f}'.replace(',', ' ')
        return m.INVALID_RANGE_REASON_TEXT.format(max_value=formatted_max)
    else:
        return float_value
