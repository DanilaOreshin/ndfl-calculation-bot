from src.config.bot_config import config as cfg
from src.texts.messages import VALIDATION_ERROR_TEXT
from src.utils.functions import validate, calculate_net_by_month, get_report_text


async def get_gross_text(inner_value):
    validated_result = validate(inner_value)
    if type(validated_result) is not float:
        text = VALIDATION_ERROR_TEXT.format(reason=validated_result)
    else:
        gross_sum = validated_result
        net_sum = calculate_net_sum(gross_sum)
        result_list = calculate_net_by_month(gross_sum)
        text = get_report_text(gross_sum, net_sum, result_list)
    return text


def separate_gross_sum(gross_sum: float) -> list[float]:
    tmp_sum = gross_sum * 12
    separated_list = []
    limits = [0.0] + cfg.LIMITS_LIST + [cfg.MAX_YEAR_GROSS]

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
        for elem, percent in zip(separate_gross_sum(gross_sum), cfg.PERCENTS_LIST)
    )
    return net_sum / 12
