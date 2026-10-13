from multiprocessing import Process

basket = []

def cook(dish):
    basket.append(dish)
    print(dish, "담음 →", basket)

if __name__ == "__main__":
    cook("김밥")
    p = Process(target=cook, args=("국수",))
    p.start()
    p.join()
    print("원래 주방:", basket)
