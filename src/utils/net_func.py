from src.config.bot_config import config as cfg
from src.texts.messages import VALIDATION_ERROR_TEXT
from src.utils.functions import validate, calculate_net_by_month, get_report_text


async def get_net_text(inner_value):
    validated_result = validate(inner_value)
    if type(validated_result) is not float:
        text = VALIDATION_ERROR_TEXT.format(reason=validated_result)
    else:
        net_sum = validated_result
        gross_sum = calculate_gross_sum(net_sum)
        result_list = calculate_net_by_month(gross_sum)
        text = get_report_text(gross_sum, net_sum, result_list)
    return text


def separate_net_sum(net_sum: float) -> list[float]:
    tmp_sum = net_sum * 12
    separated_list = []
    limits = [0.0] + cfg.LIMITS_LIST + [cfg.MAX_YEAR_GROSS]

    for i in range(1, len(limits)):
        if tmp_sum <= 0: break
        net_delta = (limits[i] - limits[i - 1]) * (1 - cfg.PERCENTS_LIST[i - 1] / 100)
        amount = min(net_delta, tmp_sum)
        separated_list.append(amount)
        tmp_sum -= amount

    return separated_list


def calculate_gross_sum(net_sum: float) -> float:
    gross_sum = sum(
        elem / (1 - percent / 100)
        for elem, percent in zip(separate_net_sum(net_sum), cfg.PERCENTS_LIST)
    )
    return gross_sum / 12
