import random

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