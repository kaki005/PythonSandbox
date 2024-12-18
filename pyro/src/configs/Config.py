from dataclasses import dataclass, field

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ModelConfig:
    name: str = "bert"
    input_max_length: int = 32


@dataclass_json
@dataclass
class TrainConfig:
    lr: float = 1e-5
    epochs: int = 10
    batch_size: int = 16


@dataclass_json
@dataclass
class WandbConfig:
    entity: str = ""
    project: str = ""


@dataclass_json
@dataclass
class Config:
    model_cfg: ModelConfig = field(default_factory=ModelConfig)
    train_cfg: TrainConfig = field(default_factory=TrainConfig)
    wandb: WandbConfig = field(default_factory=WandbConfig)
    data_dir: str = ""
    output_dir: str = ""
