import math
import numpy
import pylab


def cap_awgn(SNRdB):
    SNR=numpy.power(10,SNRdB*(0.1))
    return numpy.log2(1+SNR)/2

    
if __name__ == "__main__":
    SNRdB_min = -5
    SNRdB_max = 20
    SNRdB_range = range(SNRdB_min, SNRdB_max+1)
    cap_simu = [cap_awgn(x)      for x in SNRdB_range]
    print cap_simu
     
    f = pylab.figure()
    s = f.add_subplot(1,1,1)
    s.plot(SNRdB_range, cap_simu, 'r', label="capacidade do canal")
    s.set_title('Canal Vs SNR')
    s.set_xlabel('SNR')
    s.set_ylabel('Capacidade do Canal')
    s.legend(loc=4)
    s.grid()
    pylab.show()