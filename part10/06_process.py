from multiprocessing import Process

basket = []

def cook(dish):
    basket.append(dish)
    print("새 주방 :", basket)

if __name__ == "__main__":
    p = Process(target=cook, args=("국수",))
    p.start()
    p.join()
    print("원래 주방:", basket)
