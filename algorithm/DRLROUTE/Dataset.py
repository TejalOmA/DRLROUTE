# -*- coding: utf-8 -*-
import numpy as np
from torch.utils.data import Dataset

class DRL4RouteDataset(Dataset):
    def __init__(
            self,
            mode: str,
            params: dict, #parameters dict
    )->None:
        super().__init__()
        if mode not in ["train", "val", "test"]:
            raise ValueError
        path_key = {'train':'train_path', 'val':'val_path','test':'test_path'}[mode]
        path = params[path_key]
        self.data = np.load(path, allow_pickle=True).item()

    def __len__(self):
        return len(self.data['label_len'])

    def __getitem__(self, index):
        V = self.data['V'][index]
        V_reach_mask = self.data['constraint_mask'][index]
        label = self.data['label'][index]
        label_len = self.data['label_len'][index]

        return V, V_reach_mask, label, label_len

if __name__ == '__main__':
    pass
