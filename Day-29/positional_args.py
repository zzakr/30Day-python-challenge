parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="The filename to process")

args = parser.parse_args()
print(f"Processing file: {args.filename}")
