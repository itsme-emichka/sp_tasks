class WrongNumberOfPlayersError(Exception):
    def __str__(self) -> str:
        return 'WrongNumberOfPlayersError'


class NoSuchStrategyError(Exception):
    def __str__(self) -> str:
        return 'NoSuchStrategyError'


class WrongIncomingData(Exception):
    def __str__(self) -> str:
        return 'WrongIncomingData'


STRATEGY_BEATS: dict = {
    'R': 'S',
    'S': 'P',
    'P': 'R',
}


def rps_game_winner(array: list[list[str, str]]) -> str:
    if len(array) > 2:
        raise WrongNumberOfPlayersError
    if len(array[0]) != 2 or len(array[1]) != 2:
        raise WrongIncomingData

    first_player_name, first_player_strategy = array[0]
    second_player_name, second_player_strategy = array[1]
    try:
        if STRATEGY_BEATS[first_player_strategy] == second_player_strategy:
            return f'{first_player_name} {first_player_strategy}'
        if STRATEGY_BEATS[second_player_strategy] == first_player_strategy:
            return f'{second_player_name} {second_player_strategy}'
        if first_player_strategy == second_player_strategy:
            return f'{first_player_name} {first_player_strategy}'
    except KeyError:
        raise NoSuchStrategyError


if __name__ == '__main__':
    test_data = [
        [['player1', 'P'], ['player2', 'S'], ['player3', 'S']],
        [['player1', 'P'], ['player2', 'A']],
        [['player1', 'P'], ['player2', 'S']],
        [['player1', 'P'], ['player2', 'P']],
    ]
    for data in test_data:
        try:
            print(rps_game_winner(data))
        except Exception as ex:
            print(ex)
