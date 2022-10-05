from lightning_lite.plugins.collectives.collective import Collective
from lightning_lite.plugins.collectives.deepspeed_collective import DeepSpeedCollective
from lightning_lite.plugins.collectives.single_device_collective import SingleDeviceCollective
from lightning_lite.plugins.collectives.torch_collective import TorchCollective

__all__ = [
    "Collective",
    "DeepSpeedCollective",
    "TorchCollective",
    "SingleDeviceCollective",
]