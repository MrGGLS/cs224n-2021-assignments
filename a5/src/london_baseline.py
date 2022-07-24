# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import argparse
import utils
# run this command to start: python src/london_baseline.py --dev_set_path birth_dev.tsv
argp = argparse.ArgumentParser()
argp.add_argument('--dev_set_path',
                  help="dev dat set for london_baseline", default=None)
args = argp.parse_args()

dev_set = open(args.dev_set_path, encoding='utf-8').read()
total_pairs = len(dev_set.split('\n')) - 1

total, correct = utils.evaluate_places(args.dev_set_path, ['London'] * total_pairs)
print(f'ACC for london_baseline is: {correct * 100. / total}%')
