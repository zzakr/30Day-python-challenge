parser = argparse.ArgumentParser(description="Set default language")
parser.add_argument("--language", type=str, default="English", help="Preferred language")

args = parser.parse_args()
print(f"Language: {args.language}")
