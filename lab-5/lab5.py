from abc import ABC, abstractmethod

# ===== Strategy Pattern =====

class AttackStrategy(ABC):
  @abstractmethod
  def attack(self):
    pass

class SwordAttack(AttackStrategy):
  def attack(self):
    print("Атакує мечем!")

class BowAttack(AttackStrategy):
  def attack(self):
    print("Стріляє з лука!")

class MagicAttack(AttackStrategy):
  def attack(self):
    print("Використовує магію!")

# ===== State Pattern =====

class State(ABC):
  @abstractmethod
  def handle(self, character):
    pass

class NormalState(State):
  def handle(self, character):
    print("Персонаж у нормальному стані.")
    character.can_attack = True

class InjuredState(State):
  def handle(self, character):
    print("Персонаж поранений. Може атакувати, але слабше.")
    character.can_attack = True

class DeadState(State):
  def handle(self, character):
    print("Персонаж мертвий. Не може атакувати.")
    character.can_attack = False

# ===== Character Class =====

class Character:
  def __init__(self, name):
    self.name = name
    self.attack_strategy = SwordAttack()
    self.state = NormalState()
    self.can_attack = True

  def set_attack_strategy(self, strategy: AttackStrategy):
    self.attack_strategy = strategy

  def set_state(self, state: State):
    self.state = state
    self.state.handle(self)

  def attack(self):
    if self.can_attack:
      print(f"{self.name} ", end="")
      self.attack_strategy.attack()
    else:
      print(f"{self.name} не може атакувати у поточному стані.")

# ===== Main Program =====

def main():
  hero = Character("Герой")

  # Вибір стратегій
  hero.attack()
  hero.set_attack_strategy(BowAttack())
  hero.attack()
  hero.set_attack_strategy(MagicAttack())
  hero.attack()

  print("\n=== Зміна станів ===")
  hero.set_state(InjuredState())
  hero.attack()

  hero.set_state(DeadState())
  hero.attack()

if __name__ == "__main__":
  main()
