import numpy as np
import time
import argparse

def estimate_pi(n, seed=None):
    rng = np.random.default_rng(seed)
    x = rng.random(n)
    y = rng.random(n)
    hits = np.count_nonzero(x*x + y*y <= 1.0)
    return 4.0 * hits / n, hits

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=1_000_000)
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()

    t0 = time.time()
    pi_est, hits = estimate_pi(args.n, args.seed)
    print(f"Samples: {args.n}")
    print(f"Hits:    {hits}")
    print(f"pi ~     {pi_est:.6f}")
    print(f"Time:    {time.time()-t0:.3f} s")



# To Run: python mc_pi.py --n 1000000 --seed 42

