class EnemyFSM:
    def __init__(self):
        self.state = "PATROL"

    def compute_next_state(self, distance, health):
        if health <= 0:
            self.state = "DEAD"
            return

        if self.state == "PATROL":
            if distance < 250: self.state = "CHASE"
        elif self.state == "CHASE":
            if distance > 300: self.state = "PATROL"
            elif distance < 50: self.state = "ATTACK"
        elif self.state == "ATTACK":
            if distance > 70: self.state = "CHASE"
            
    def get_current_state(self):
        return self.state