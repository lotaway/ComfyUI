import torch_directml
import torch
import time

dml = torch_directml.device()


def show_dml_info():
    print("dml: " + format(dml))

    num_devices = torch_directml.device_count()
    print(f"Number of DirectML devices: {num_devices}")

    for i in range(num_devices):
        device_name = torch_directml.device_name(i)
        print(f"DirectML device {i}: {device_name}")

    print(f"Default device is:{torch_directml.default_device()}")

    print("ROCm version:", torch.version.hip)


class MyModule:
    size: int

    def __init__(self, _size=8192 * 2):
        self.size = _size

    def bench(self, device):
        print(f"Running on {device}")
        a = torch.rand((self.size, self.size), device=device)
        b = torch.rand((self.size, self.size), device=device)
        start = time.time()
        c = torch.mm(a, b)
        torch.cuda.synchronize() if torch.cuda.is_available() else None
        print(f"{device} matrix multiplication:", time.time() - start, "Seconds")


def test_perform():
    module = MyModule()
    # CPU
    module.bench("cpu")
    # DirectML
    module.bench(dml)


show_dml_info()
test_perform()
