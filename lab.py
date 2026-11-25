import argparse
import sys
from ollama import generate

def main():
    parser = argparse.ArgumentParser(description="Genera text amb Ollama.")
    parser.add_argument("prompt", type=str, help="El prompt a utilitzar.")
    parser.add_argument("--vegades", type=int, default=5, 
help="Nombre de vegades a generar text.")
    parser.add_argument("--temperature", type=float, 
default=1.0, help="Temperatura de la generació.")
    parser.add_argument("--seed", type=int, default=None,
help="Sembra per la generació.")
    parser.add_argument("--top_k", type=int, default=None,
help="Top K per la generació.")
    parser.add_argument("--top_p", type=float, default=None,
help="Top P per la generació.")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    print(f"Prompt: {args.prompt}")
    print(f"vegades: {args.vegades}")
    print(f"temperature: {args.temperature}")
    if args.seed is not None:
        print(f"seed: {args.seed}")
    if args.top_k is not None:
        print(f"top_k: {args.top_k}")
    if args.top_p is not None:
        print(f"top_p: {args.top_p}")

    for i in range(args.vegades):
        r = generate(model="gemma3:4b", prompt=args.prompt, 
options={"temperature": args.temperature, "seed": args.seed, "top_k": args.top_k, "top_p": args.top_p})
        print(f"{i+1}. {r['response'].strip()}")

if __name__ == "__main__":
    main()