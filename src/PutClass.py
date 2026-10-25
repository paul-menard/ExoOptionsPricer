from OptionClass import (Option)
import numpy as np


class Put(Option):

    def __init__(self, S_0 = 100, K = 100, T = 1, q = 0.015, r = 0.04, kind = "european", model = "black-scholes", n_steps = 10, seed = 42):
        super().__init__(S_0, K, T, q, r, kind, model, n_steps, seed)


    ## maybe we should put these guardrails before.... whatever
    def ComputePayoffs(self, trajectories):
            payoff = None
            if self.kind == "european":
                payoffs = np.maximum(self.K - trajectories[:,-1], 0)
                pass
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