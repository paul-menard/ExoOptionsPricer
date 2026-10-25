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
                 B=None, 
                 barrier_kind=None, 
                 seed = 42):
        super().__init__(S_0, K, T, q, r, sigma, kind, model, n_steps, B, barrier_kind, seed)


    def ComputePayoffs(self, trajectories : np.array):
        payoffs = None
        if self.kind == "european":
            ## is it easier to use the barrier type at the end or at the beginning ??
            if self.B is None : 
                payoffs = np.maximum(trajectories[:,-1] - self.K, 0)
            else : 
                if self.barrier_kind == "down_and_in":
                    ## underlying must pass under the barrier to be priced
                    valid = np.any(payoffs <= self.B, axis = 1)
                    payoffs = np.maximum(trajectories[:,-1] - self.K, 0)*valid
                    pass
                elif self.barrier_kind == "down_and_out":
                    ## underlying must not pass under the barrier to be priced
                    valid = np.any(payoffs > self.B, axis = 1)
                    payoffs = np.maximum(trajectories[:,-1] - self.K, 0)*valid
                    pass
                elif self.barrier_kind == "up_and_in":
                    ## underlying has to go above the barrier
                    valid = np.any(payoffs >= self.B, axis = 1)
                    payoffs = np.maximum(trajectories[:,-1] - self.K, 0)*valid
                    pass
                elif self.barrier_kind == "up_and_out":
                    ## underlying must not go above the barrier
                    valid = np.any(payoffs < self.B, axis = 1)
                    payoffs = np.maximum(trajectories[:,-1] - self.K, 0)*valid
                    pass
                else :
                    print("Barrier kind is not supported")
                    raise TypeError
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