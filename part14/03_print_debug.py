def pages(total_items, per_page):
    print(f"{total_items=} {per_page=} {total_items / per_page=}")
    return total_items // per_page

print(pages(25, 10))          # 3쪽이어야 하는데
