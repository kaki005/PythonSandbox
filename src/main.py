import argparse  # 1. argparseをインポート

import hydra
import omegaconf
import wandb

from config.Config import Config

parser = argparse.ArgumentParser(description='このプログラムの説明（なくてもよい）')


@hydra.main(version_base=None, config_path="configs/", config_name="default")
def main(cfg: Config):
    wandb.login()
    wandb.config = omegaconf.OmegaConf.to_container(
        cfg, resolve=True, throw_on_missing=True
    )
    wandb.init(entity=cfg.wandb.entity, project=cfg.wandb.project)
    wandb.log({"loss": loss})
    model = Model(**wandb.config.model_cfg)
    wandb.finish()

if __name__ == "__main__":
    main()
