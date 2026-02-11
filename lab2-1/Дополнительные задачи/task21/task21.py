import time
import tracemalloc


def convert(data):
    cover_cards = {}
    for value, suit in data:
        if suit not in cover_cards:
            cover_cards[suit] = []
        cover_cards[suit].append(value)
    for key in cover_cards:
        cover_cards[key] = sorted(cover_cards[key], key=lambda r: rank_order[r], reverse=True)
    return cover_cards

def solve(cover_cards, attacked_cards, r):
    for value, suit in attacked_cards:
        # Атакующая карта козырная
        if suit == r:
            # Если козырей нет или все козыри младше, то покрыть нельзя
            if r not in cover_cards or rank_order[cover_cards[r][0]] < rank_order[value]:
                return False
            cover_cards[r].pop(0)
            continue
        # Атакующая карта не козырная. Если карта такой же масти есть и ее ранг выше, то бьем
        if suit in cover_cards and rank_order[cover_cards[suit][0]] > rank_order[value]:
            cover_cards[suit].pop(0)
            continue
        # Атакующая карта не козырная. Карты такой же масти нет или она младше. Если есть козырь, то бьем им
        if r in cover_cards and len(cover_cards[r]) > 0:
            cover_cards[r].pop(0)
            continue
        # Карту покрыть невозможно
        return False

    # Все карты покрыты
    return True

def main():
    with open("input.txt") as inp:
        n, m, r = inp.readline().split()
        cover_cards = inp.readline().split()
        attacked_cards = inp.readline().split()
    cover_cards = convert(cover_cards)
    attacked_cards = sorted(attacked_cards,
                     key=lambda card: (
                         # 1. Сначала козыри, потом остальные
                         0 if card[1] == r else 1,
                         # 2. Группировка по мастям
                         card[1],
                         # 3. По убыванию ранга внутри масти
                         -"6789TJQKA".index(card[0])
                     ))
    result = "YES" if solve(cover_cards, attacked_cards, r) else "NO"
    with open("output.txt", "w") as out:
        out.write(result)

if __name__ == "__main__":
    rank_order = {'6': 0, '7': 1, '8': 2, '9': 3,
                  'T': 4, 'J': 5, 'Q': 6, 'K': 7, 'A': 8}
    t_start = time.time()
    main()
    print(f"Время работы программы: {time.time() - t_start}")
    tracemalloc.start()
    main()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Текущий объем памяти: {current / 2 ** 20} Mбайт, максимальный объем выделенной памяти: {peak / 2 ** 20} Mбайт\n")
