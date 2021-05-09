import numpy as np


def norm_dict(data, sig_factor=6):
    # construct norm
    std = np.std(data, ddof=1)
    mu = np.mean(data)

    lower = mu - std * sig_factor / 2
    upper = mu + std * sig_factor / 2
    return {"bounds": [lower, upper], "mu": mu, "std": std}


def is_latest_extreme(data, bounds):
    latest = data[-1]

    if latest < bounds[0] or latest > bounds[1]:
        return True
    else:
        return False