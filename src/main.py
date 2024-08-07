import argparse  # 1. argparseをインポート

import hydra
import omegaconf
import wandb
from pyacclaim import loadAMC, loadASF

from config.Config import Config

parser = argparse.ArgumentParser(description='このプログラムの説明（なくてもよい）')


@hydra.main(version_base=None, config_path="config/", config_name="default")
def main(cfg: Config):
    asf = loadASF('test.asf')
    amc = loadAMC(asf, 'test.amc')

if __name__ == "__main__":
    main()
