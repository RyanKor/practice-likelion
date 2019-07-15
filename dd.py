 elif user == "보":
        if random.choice(["가위", "바위", "보"]) == "가위":
            print("패배했습니다")
        elif random.choice(["가위", "바위", "보"]) == "주먹":
            print("승리했습니다.")
            game = False
        else:
            print("비겼습니다.")