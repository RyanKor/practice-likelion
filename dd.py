

a = "== == == == == == == == == == == == == == == 가위바위보 입니다. == == == == == == == == == == == == == == == ="
b = "                                [1.가위 / 2.바위 / 3.보] 중 하나를 입력해주세요                                "
c = "                                     승리/패배/무승부의 결과가 출력됩니다                                      "

print(a)
print(b)
print(c)

print("HTH의 즐거운 가위바위보")
game = True
while game:
    user = input("가위, 바위, 보! :")
    if user == "가위":
      if random.choice(["가위", "바위", "보"]) == "보":
          print("승리했습니다")
          game = False
      elif random.choice(["가위", "바위", "보"]) == "바위":
          print("패배했습니다.")
      else:
          print("비겼습니다.")
    elif user == "바위":
      if random.choice(["가위", "바위", "보"]) == "보":
          print("패배했습니다")
      elif random.choice(["가위", "바위", "보"]) == "가위":
          print("승리했습니다.")
          game = False
      else:
          print("비겼습니다.")
     elif user == "보":
        if random.choice(["가위", "바위", "보"]) == "가위":
            print("패배했습니다")
        elif random.choice(["가위", "바위", "보"]) == "주먹":
            print("승리했습니다.")
            game = False
        else:
            print("비겼습니다.")
print("끝~~, 고생하셨습니다!!")

