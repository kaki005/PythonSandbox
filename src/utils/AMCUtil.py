
from pyacclaim import loadAMC, loadASF
from typing import Dict, List

class AMCUtil:
    def load(self, amc_path:str, asf_path:str):
        asf = loadASF('test.asf')
        amc = loadAMC(asf, 'test.amc')
        return asf, amc
    def Show(self, asf: Dict, amc:List) :
