import gym
from IPython.display import clear_output
from time import sleep
import numpy as np
import random

def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        print(frame['frame'])
        print(f"Timestep: {i + 1}")
        # print(f"State: {frame['state']}")
        # print(f"Action: {frame['action']}")
        # print(f"Reward: {frame['reward']}")
        sleep(0.2)


env = gym.make("Taxi-v3").env

env.reset()

env.s = 328  # set environment to illustration's state

env.render()

q_table = np.zeros([env.observation_space.n, env.action_space.n])


# Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.1

# For plotting metrics
all_epochs = []
all_penalties = []

for i in range(1, 10001):
    state = env.reset()

    epochs, penalties, reward, = 0, 0, 0
    done = False
    
    while not done:
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample() # Explore action space
        else:
            action = np.argmax(q_table[state]) # Exploit learned values

        next_state, reward, done, info = env.step(action) 
        
        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])
        
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state, action] = new_value

        if reward == -10:
            penalties += 1

        state = next_state
        epochs += 1
        
    if i % 100 == 0:
        clear_output(wait=True)
        print(f"Episode: {i}")

print("Training finished.\n")

frames = [] # for animation


total_epochs, total_penalties = 0, 0
episodes = 1

for _ in range(episodes):
    state = env.reset()
    epochs, penalties, reward = 0, 0, 0
    

    done = False
    
    while not done:
        action = np.argmax(q_table[state])
        state, reward, done, info = env.step(action)

        if reward == -10:
            penalties += 1

        epochs += 1

        frames.append({
            'frame': env.render(mode='ansi'),
            'state': state
            }
        )

    
    total_penalties += penalties
    total_epochs += epochs

print_frames(frames)

print(f"Results after {episodes} episodes:")
print(f"Average timesteps per episode: {total_epochs / episodes}")
print(f"Average penalties per episode: {total_penalties / episodes}")


    
    

