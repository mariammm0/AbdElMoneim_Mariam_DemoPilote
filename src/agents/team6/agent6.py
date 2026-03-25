import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent


class Agent6(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "Abd El Moneim Mariam"  #on modifie le nom ici
        
    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []

    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs):
        acceleration = random.random()
        steering = random.random()
        
        #Pour que l’agent6 effectue un tour complet sur lui-même, il faut les valeur suivante: 
        action = {
            "acceleration": acceleration,
            "steer": True,
            "brake": bool(random.getrandbits(1)), # bool(random.getrandbits(1)),
            "drift": True,
            "nitro": True,
            "rescue": True,
            "fire": True,
        }
        return action
        
 
