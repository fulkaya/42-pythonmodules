from abc import ABC, abstractmethod
from ex0 import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory


class InvalidStrategyError(Exception):
	pass

class BattleStrategy(ABC):

	@abstractmethod
	def is_valid(self, factory: CreatureFactory, factory2: CreatureFactory) -> bool:
		pass

	@abstractmethod
	def act(self, factory:CreatureFactory) -> tuple[str, str]:
		pass

class NormalStrategy(BattleStrategy):


class AggressiveStrategy(BattleStrategy):


class DefensiveStrategy(BattleStrategy):
