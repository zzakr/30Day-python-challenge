parser = argparse.ArgumentParser(description="User Info")
parser.add_argument("--name", type=str, required=True, help="Your name")
parser.add_argument("--age", type=int, required=True, help="Your age")

args = parser.parse_args()
print(f"Name: {args.name}, Age: {args.age}")
