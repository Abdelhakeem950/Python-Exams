def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000:
        return True
    return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    # 1. حساب الطاقة المولدة
    generated_power = voltage * current
    
    # 2. حساب نسبة الكفاءة
    efficiency = (generated_power / theoretical_max_power) * 100
    
    # 3. تحديد اللون بناءً على الشروط
    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60:
        return 'orange'
    elif efficiency >= 30:
        return 'red'
    else:
        return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.
    
    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').
    """
    # حساب حاصل الضرب
    product = temperature * neutrons_produced_per_second
    
    # التحقق من الشروط
    if product < 0.9 * threshold:
        return 'LOW'
    elif 0.9 * threshold <= product <= 1.1 * threshold:
        return 'NORMAL'
    else:
        return 'DANGER'