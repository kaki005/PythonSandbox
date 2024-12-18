import hydra
import omegaconf
import wandb
from configs import Config


@hydra.main(version_base=None, config_path="configs/", config_name="default")
def main(cfg: Config):
    wandb.login()
    wandb.config = omegaconf.OmegaConf.to_container(cfg, resolve=True, throw_on_missing=True)
    wandb.init(entity=cfg.wandb.entity, project=cfg.wandb.project)
    loss = 0
    wandb.log({"loss": loss})
    wandb.finish()


if __name__ == "__main__":
    main()
