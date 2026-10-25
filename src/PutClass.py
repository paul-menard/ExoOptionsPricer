from OptionClass import (Option)
import numpy as np


class Put(Option):

    def __init__(self, S_0 = 100, K = 100, T = 1, q = 0.015, r = 0.04, kind = "european", model = "black-scholes", n_steps = 10, seed = 42):
        super().__init__(S_0, K, T, q, r, kind, model, n_steps, seed)


    ## maybe we should put these guardrails before.... whatever
    def ComputePayoffs(self, trajectories):
            payoff = None
            payoffs = None
            if self.kind == "european":
                ## is it easier to use the barrier type at the end or at the beginning ??
                if self.B is None : 
                    payoffs = np.maximum(trajectories[:,-1] - self.K, 0)
                else : 
                    if self.barrier_kind == "down_and_in":
                        ## underlying must pass under the barrier to be priced
                        valid = np.any(payoffs <= self.B, axis = 1)
                        payoffs = np.maximum(self.K - trajectories[:,-1], 0)*valid
                        pass
                    elif self.barrier_kind == "down_and_out":
                        ## underlying must not pass under the barrier to be priced
                        valid = np.any(payoffs > self.B, axis = 1)
                        payoffs = np.maximum(self.K - trajectories[:,-1], 0)*valid
                        pass
                    elif self.barrier_kind == "up_and_in":
                        ## underlying has to go above the barrier
                        valid = np.any(payoffs >= self.B, axis = 1)
                        payoffs = np.maximum(self.K - trajectories[:,-1], 0)*valid
                        pass
                    elif self.barrier_kind == "up_and_out":
                        ## underlying must not go above the barrier
                        valid = np.any(payoffs < self.B, axis = 1)
                        payoffs = np.maximum(self.K - trajectories[:,-1], 0)*valid
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
            pass

    def ValueOption(self, payoffs):
        return np.exp(-self.r*self.T)*np.mean(payoffs)
    pass