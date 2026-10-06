import random

def run_experiment(n_flips):
    """Бросает монету n_flips и возвращает число орлов. """
    heads = 0
    for _ in range(n_flips):
        if random.random() < 0.5:
            heads += 1
    return heads

def main():
    n_trials = 10000
    n_flips = 100
    
    results = []
    for _ in range(n_trials):
        heads = run_experiment(n_flips)
        results.append(heads)
        
    counts = {}
    for heads in results:
        counts[heads] = counts.get(heads,1) + 1
        
    print(f"Результаты {n_trials} экспериментов по {n_flips} бросков:\n")
    for heads in sorted(counts):
        count = counts[heads]
        bar = "#" * (count // 50)
        print(f"{heads:3d} орлов: {bar} ({count})")
        
if __name__ == "__main__":
    main()