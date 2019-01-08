"""A Script to run/test the RandomAgent class"""

import argparse
import gym
import retro
from random_agent import RandomAgent

def main():
    script_args = parse_args()
    if script_args.use_retro:
        env = retro.make(script_args.env_name)
    else:
        env = gym.make(script_args.env_name)

    random_agent = RandomAgent(env)
    random_agent.train(script_args.num_episodes, script_args.render_train)

    play_reward = random_agent.play()
    print(f'Reward after playing: {play_reward}')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--env-name', type=str,
        dest='env_name', default='CartPole-v0',
        help='The name of the gym/retro environment.')
    parser.add_argument('--retro',
        dest='use_retro', action='store_true',
        help='The name of the gym/retro environment.')
    parser.add_argument('--num-episodes', type=int,
        dest='num_episodes', default=500,
        help='The number of episodes to train.')
    parser.add_argument('--render-train',
        dest='render_train', action='store_true',
        help='Should we render during training.')

    return parser.parse_args()

if __name__ == "__main__":
    main()