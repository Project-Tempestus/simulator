class Weapon:
    def __init__(self, stats):
        self.stats = stats
        self.notifications = []

    def notify(self):
        """
        TODO: Setup notifications system
        """
        print("TODO: Notifying simulator about some events")
        pass

    def attack(self, ranged=True):
        num_attacks = self._attack_ranged() if ranged else self._attack_melee()

        return num_attacks

    def reload(self):
        """
        Reload the weapon
        """
        self.stats.clip_current = self.stats.clip_capacity

    def _attack_ranged(self):
        """
        Return number of attacks
        """
        if self.stats.clip_current <= 0:
            print("WEAPON:::Ran out of ammo!")
            return 0

        num_bullets = self.stats.clip_current - self.stats.burst
        if num_bullets < 0:
            self.stats.clip_current = 0
        else:
            self.stats.clip_current -= self.stats.burst
        return num_bullets

    def _attack_melee(self):
        """
        Return number of attacks
        """
        return 1
