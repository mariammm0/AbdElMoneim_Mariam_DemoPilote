import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent

class Agent7(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "Abd El Moneim Mariam 7"  #on modifie le nom ici
        
        self.stuck_steps= 0
        self.en_marche_arriere=False #par defaut 
        self.recovery_steps = 0
       

    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []

    def endOfTrack(self):
        return self.isEnd
        
    def recul(self, obs, vitesse,steering):
        phase = obs.get("phase", 0)

        # on ne compte les blocages qu'en phase de course pour ignorer le compte à rebours
        if phase > 2 and  self.stuck_steps<200:  #si on est déja partie du départ
            self.stuck_steps += 1

        # déclenchement de la marche arrière si le seuil est dépassé
        if self.stuck_steps ==200 and not self.en_marche_arriere:  #decision d'activer marche arriere
            self.en_marche_arriere = True
            self.recovery_steps = 200  #durée de la marche arriere

        if self.en_marche_arriere:  #execution de marche arriere
            self.recovery_steps -= 1 #decrementer

            #on reprend la conduite normale
            if self.recovery_steps <= 0:
                self.en_marche_arriere = False

            return {
                "acceleration": 0.0,
                "steer": steering,
                "brake": True,   #activation marche arrière 
                "drift": False,
                "nitro": False,
                "rescue": False,
                "fire": False,
            }

        
    def choose_action(self, obs):
        acceleration = random.random()
        steering = random.random()

        recul= recul(self, obs, vitesse,steering)
        
        action = {
            "acceleration": acceleration,
            "steer": steering,
            "brake": False, # bool(random.getrandbits(1)),
            "drift": bool(random.getrandbits(1)),
            "nitro": bool(random.getrandbits(1)),
            "rescue":bool(random.getrandbits(1)),
            "fire": bool(random.getrandbits(1)),
        }
        return action
