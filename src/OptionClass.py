import numpy as np

class Option:
    ## sert à initialiser tous les points communs entre les options vanilla
    def __init__(self, S_0 : float = 100, 
                 K : float = 100, 
                 T : float = 1, 
                 q:float = 0.015, 
                 r:float = 0.04, 
                 sigma:float = 0.1, 
                 kind : str = "european", 
                 model : str = "black-scholes", 
                 n_steps : int = 10 ,
                 B = None,
                 barrier_kind = None,
                 seed : int = 42):
        self.S_0 = S_0
        self.K = K
        self.T = T 
        self.q = q
        self.r = r
        self.sigma = sigma
        self.kind = kind ## ex : european, bermudan, american, asian... 
        self.model = model ## ex : Black-Scholes, Dumpire, Heston... for now on, we will only support black-scholes for its easy implementation.
        ## le problème à gérer est que la vol doit etre gerér différemment selon le modèle. Prendre en entrée une liste ?
        ## if european we need to ask 
        ## in general for different edge cases, multiple conditions will be needed as an addition
        self.n_steps = n_steps
        self.B = B
        self.barrier_kind = barrier_kind ## "down_and_in"....
        self.seed = seed


    def MonteCarlo(self, n_paths):
        ## I wonder if we can just pass an array called sigma whatever happens ?
        if self.model == "black-scholes":
            delta = self.T / self.n_steps
            print(delta)
            log_trajectories = (self.r - self.q - 0.5*(self.sigma**2))*delta + self.sigma*np.sqrt(delta)*np.random.normal(0, 1, (n_paths, self.n_steps))
            print(log_trajectories.shape)
            return self.S_0*np.exp(log_trajectories.cumsum(axis = 1))
            
        if self.model == "dumpire":
            pass
        if self.model == "heston":
            pass
        if self.model == "custom":
            pass

    def BinomialTree(self):
        pass

    def ComputeTrajectories(self, n_paths = 50):
            trajectories = None
            if self.kind == "european":
                trajectories = self.MonteCarlo(n_paths=n_paths)
                pass
            elif self.kind == "american":
                trajectories = self.BinomialTree()
                pass
            elif self.kind == "bermudan":
                trajectories = self.BinomialTree()
                pass
            elif self.kind == "asian":
                ## idk which kind is the best here ? my guess is montecarlo because you can only exercise at expiry
                pass
            else :
                print("This option kind is not currently supported")
                raise TypeError
            return trajectories