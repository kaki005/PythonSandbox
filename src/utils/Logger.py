from abc import ABC

import omegaconf

import wandb
from config import Config


class Logger(ABC):
    def init(self, config:Config):
        pass
    def finish(self):
        pass
    def log(self, key, value):
        pass



class WandbLogger(Logger):
    def init(self, config:Config):
        wandb.login()
        wandb.config = omegaconf.OmegaConf.to_container(config, resolve=True, throw_on_missing=True)
        wandb.init(project=config.wandb.project)
    def finish(self):
        wandb.finish()
    def log(self, key, value):
        wandb.log({f"{key}": value})


class NullLogger(Logger):
    def init(self, config:Config):
        pass
    def finish(self):
        pass
    def log(self, key, value):
        print(f"{key} ={value} ")
