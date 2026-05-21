def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """
    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)

def higher_card(card_one, card_two):
    # نجيب القيمة الرقمية لكل ورقة باستخدام الدالة اللي عملناها في التاسك الأول
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    
    # نقارن القيم الرقمية
    if value_one > value_two:
        return card_one
    elif value_one == value_two:
        return card_one, card_two  # إرجاع الورقتين مفصولين بفاصلة في حالة التعادل
    else:
        return card_two

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.
    """
    # 1. لو إيدك أصلاً فيها ورقة A، الورقة الجديدة قيمتها 1 فوراً
    if card_one == 'A' or card_two == 'A':
        return 1
    
    # 2. لو مفيش A، نحسب مجموع الورقتين اللي معانا
    current_hand_value = value_of_card(card_one) + value_of_card(card_two)
    
    # 3. نشوف لو ضفنا 11 هنعدي الـ 21 ولا لأ
    if current_hand_value + 11 <= 21:
        return 11
    else:
        return 1

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).
    """
    # تعريف مجموعة الأوراق اللي قيمتها 10
    ten_cards = ('10', 'J', 'Q', 'K')
    
    # التحقق من السيناريوهين الممكنين للبلاك جاك
    return (card_one == 'A' and card_two in ten_cards) or (card_two == 'A' and card_one in ten_cards)

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    # هنقارن قيمة الورقة الأولى بقيمة الورقة التانية
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    # بنحسب مجموع الورقتين
    hand_total = value_of_card(card_one) + value_of_card(card_two)
    
    # بنختبر لو المجموع بيساوي 9 أو 10 أو 11
    return hand_total in (9, 10, 11)
    

        
    