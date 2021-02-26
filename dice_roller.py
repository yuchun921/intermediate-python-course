import random


def main():

    dice_sum = 0
    dice_rolls = 2
    for i in range(dice_rolls):
      roll = random.randint(1, 6)
      dice_sum += roll
      print(f'You rolled a {roll}')  # 格式化字符串字面值

    print(f'You have rolled a total of {dice_sum}')


if __name__ == "__main__":
    main()
