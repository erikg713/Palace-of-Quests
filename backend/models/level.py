from typing import List, Callable, Optional

class Level:
    """
    Represents a game level with XP requirements and rewards.

    Attributes:
        levelNumber (int): The number of the level.
        xpRequired (int): XP required to reach the level.
        rewards (list): List of rewards for the level.
    """

    def __init__(self, levelNumber: int, xpRequired: int, rewards: Optional[List[str]] = None):
        if levelNumber <= 0:
            raise ValueError("levelNumber must be a positive integer.")
        if xpRequired <= 0:
            raise ValueError("xpRequired must be a positive integer.")
        self.levelNumber = levelNumber
        self.xpRequired = xpRequired
        self.rewards = rewards if rewards is not None else []

    def __repr__(self) -> str:
        return f"Level(levelNumber={self.levelNumber}, xpRequired={self.xpRequired}, rewards={self.rewards})"

    @staticmethod
    def generate_levels(maxLevel: int, xpIncrement: int, reward_generator: Optional[Callable[[int], List[str]]] = None) -> List['Level']:
        """
        Dynamically generates levels with XP scaling and rewards.

        Args:
            maxLevel (int): Total number of levels to generate.
            xpIncrement (int): XP increment per level.
            reward_generator (callable, optional): A function that takes the level number as input and returns a list of rewards.

        Returns:
            list[Level]: List of generated Level objects.

        Example:
            def sample_reward_generator(level):
                return [f"Reward for level {level}"]

            levels = Level.generate_levels(5, 100, sample_reward_generator)
            # Output: [Level(1, 100, ['Reward for level 1']), Level(2, 200, ['Reward for level 2']), ...]
        """
        if maxLevel <= 0 or xpIncrement <= 0:
            raise ValueError("maxLevel and xpIncrement must be positive integers.")

        if reward_generator is None:
            reward_generator = lambda level: [f"Default reward for level {level}"]

        levels = []
        for i in range(1, maxLevel + 1):
            rewards = reward_generator(i)
            levels.append(Level(i, i * xpIncrement, rewards))
        return levels
