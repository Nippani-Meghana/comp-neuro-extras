from brian2 import *


class LIF:
    def __init__(self,tau,Vt,Vr,El,R,I):
        # Load parameters
        self.tau = tau        # membrane time constant
        self.Vt = Vt       # spike threshold
        self.Vr = Vr
        self.El = El
        self.R = R
        self.I = I



    def determinisitc(self):
        eqs = '''
        dV/dt = (El - V + R*I)/tau : volt
        '''
        G = NeuronGroup(1, eqs, threshold='V > Vt', reset='V = Vr', method='exact')

        G.V = self.El
        G.El = self.El
        G.R = self.R
        G.I = self.I
        G.tau = self.tau
        
        M = StateMonitor(G, 'V', record=True)
        spikemon = SpikeMonitor(G)
        run(100*ms)
        print("Spike times:", spikemon.t)
        return spikemon.t




if __name__ == "__main__":
        # Simulation parameters
        tau = 10*ms        # membrane time constant
        Vt = -50*mV        # spike threshold
        Vr = -65*mV        # reset potential
        El = -65*mV        # resting potential
        R = 100*Mohm       # membrane resistance
        I = 0.3*nA         # input current

        model = LIF(tau,Vt,Vr,El,R,I)

