from models.calculate import Calculate


def main() -> None:
    score: int = 0
    play(score)


def play(score: int) -> None:
    difficulty: int = int(input('Enter the desired difficulty level: '))

    calc: Calculate = Calculate(difficulty)

    print(f'Report the result for the following operation: ')
    calc.show_operation()

    result: int = int(input())

    if calc.check_result(result):
        score += 1
        print(f'You have {score} points.')

    continue_game: int = int(input('Do you want to continue in the game? [1 - Yes, 0 - No]: '))

    if continue_game:
        play(score)
    else:
        print(f'You finished with {score} points.')
        print('Until next time.')


if __name__ == '__main__':
    main()
