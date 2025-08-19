import numpy as np, time, argparse



def estimate_pi(n, seed=None):

    rng = np.random.default_rng(seed)

    x = rng.random(n); y = rng.random(n)

    hits = np.count_nonzero(x*x + y*y <= 1.0)

    return 4.0*hits/n, hits



if __name__ == "__main__":

    ap = argparse.ArgumentParser()

    ap.add_argument("--n", type=int, default=1_000_000)

    ap.add_argument("--seed", type=int, default=42)

    args = ap.parse_args()

    t0=time.time()

    pi, hits = estimate_pi(args.n, args.seed)

    print(f"Samples: {args.n}")

    print(f"Hits:    {hits}")

    print(f"pi ~     {pi:.8f}")

    print(f"Time:    {time.time()-t0:.3f}s")


# To Run, use: python mc_pi.py --n 1000000


