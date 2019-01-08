"""RandomAgent

A class that interacts with gym-like environments.
"""

class RandomAgent():
    """Our RandomAgent class"""

    def __init__(self, env):
        self.env = env
        self.best_reward = None
        self.best_actions = []

    def train(self, num_episodes, should_render):
        for _ in range(num_episodes):
            initial_state = self.env.reset()
            if should_render:
                self.env.render()
            # one episode
            done = False
            total_reward = 0
            actions = []
            while not done:
                # (heading, speed) -> (0-359, 0-255)
                action = self.env.action_space.sample()
                actions.append(action)
                new_state, reward, done, _ = self.env.step(action)
                if should_render:
                    self.env.render()
                total_reward += reward

            if self.best_reward is None or self.best_reward < total_reward:
                self.best_reward = total_reward
                self.best_actions = actions
        print(f'Best reward during training: {total_reward}')

    def play(self):
        self.env.reset()
        self.env.render()
        total_reward = 0
        for action in self.best_actions:
            _, reward, _, _ = self.env.step(action)
            self.env.render()
            total_reward += reward
        return total_reward
