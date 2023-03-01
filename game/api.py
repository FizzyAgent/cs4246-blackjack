from game.game_models import ActionOutcome, GameState


class BlackjackWrapper:
    """
    Mid-layer APIs to be implemented for RL training
    Wraps around the blackjack game implementation
    Processes input from RL training process and returns output from blackjack game
    """

    def __init__(self):
        ...

    def reset(self) -> None:
        ...

    def get_state(self) -> GameState:
        ...

    def bet_step(self, bet_percent: float) -> ActionOutcome:
        ...

    def card_step(self, take_card: bool) -> ActionOutcome:
        ...
