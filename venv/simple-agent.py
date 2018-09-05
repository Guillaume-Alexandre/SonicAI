from retro import make
import gym_remote.exceptions as gre
import gym_remote.client as grc
import random

# Mapping des touches
UP = 4
DOWN = 5
LEFT = 6
RIGHT = 7
BTN_1 = 0
BTN_2 = 1
BTN_3 = 8

def intializeActions(action):
    length = len(action)
    cc=0
    while (cc < length):
        action[cc]=0
        cc=cc+1
    return action

def main():
    print('connecting to remote environment')
    env = make(game='SonicTheHedgehog-Genesis', state='GreenHillZone.Act1')
    print('starting episode')
    obs = env.reset()

    cc=0
    while True:
        action = env.action_space.sample()
        action=intializeActions(action)
        cc=random.randint(0, 3)
        if(cc==0) :
            action[BTN_1] = 1
            action[RIGHT] = 1
            obs, rew, done, info = env.step(action)
            env.render()
            action = env.action_space.sample()
            action = intializeActions(action)
            action[BTN_1] = 1
            action[UP]=1
            action[RIGHT] = 1
            action = env.action_space.sample()
            action = intializeActions(action)
            action[BTN_1] = 1
            action[UP]=1
            action[RIGHT] = 1
            action = env.action_space.sample()
            action = intializeActions(action)
            action[BTN_1] = 1
            action[DOWN]=1
            action[RIGHT] = 1
            action = env.action_space.sample()
            action = intializeActions(action)
            action[BTN_1] = 1
            action[DOWN]=1
            action[RIGHT] = 1
            action = env.action_space.sample()
            action = intializeActions(action)
            action[BTN_1] = 1
            action[DOWN]=1
            action[RIGHT] = 1
        else :
            action[RIGHT] = 1

        obs, rew, done, info = env.step(action)
        env.render()
        if done:
            print('episode complete')
            obs = env.reset()


if __name__ == '__main__':
    try:
        main()
    except gre.GymRemoteError as e:
        print('exception', e)