from OptionClass import (Option)
import numpy as np

class Call(Option):
    ## qu'est-ce qui change selon le type d'option ? le payoff, et c'est a peu pret tout ? donc on fait les simulations en dehors car 
    ## ne nécessite pas le type d'action, on fait juste le calcul final dans la classe de fin. 
    def __init__(self, 
                 S_0 = 100, 
                 K = 100, 
                 T = 1, 
                 q = 0.015, 
                 r = 0.04, 
                 sigma = 0.1, 
                 kind = "european", 
                 model = "black-scholes", 
                 n_steps = 10, 
                 seed = 42):
        
        super().__init__(S_0, K, T, q, r, sigma, kind, model, n_steps, seed)


    def ComputePayoffs(self, trajectories : np.array):
        payoffs = None
        if self.kind == "european":
            payoffs = np.maximum(trajectories[:,-1] - self.K, 0)

        elif self.kind == "american":
            pass
        elif self.kind == "bermudan":
            pass
        elif self.kind == "asian":
            pass
        else :
            print("This option kind is not currently supported")
            raise TypeError
        
        return payoffs

    def ValueOption(self, payoffs):
        return np.exp(-self.r*self.T)*np.mean(payoffs)