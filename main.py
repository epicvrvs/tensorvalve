import sys

import scipy.io.wavfile
from lstm import LSTMNet
from profiler import Profiler

def read_wav(path):
	print(f'Loading WAV file from "{path}".')
	rate, data = scipy.io.wavfile.read(path)
	return data

if len(sys.argv) != 6:
	print('Usage:')
	print(f'{sys.argv[0]} <dry training WAV file> <wet training WAV file> <dry validation WAV file> <wet validation WAV file> <session directory>')
	sys.exit(1)

dry_training_wav_path = sys.argv[1]
wet_training_wav_path = sys.argv[2]

dry_validation_wav_path = sys.argv[3]
wet_validation_wav_path = sys.argv[4]

save_path = sys.argv[5]

profiler = Profiler()

dry_training_wav = read_wav(dry_training_wav_path)
wet_training_wav = read_wav(wet_training_wav_path)

dry_validation_wav = read_wav(dry_validation_wav_path)
wet_validation_wav = read_wav(wet_validation_wav_path)

profiler.stop('Done loading WAV files.')

if len(dry_training_wav) != len(wet_training_wav) or len(dry_validation_wav) != len(wet_validation_wav):
	raise Exception('Dry and wet WAVs must be same length.')

net = LSTMNet(32, 512, 96, 64, save_path)
net.train(dry_training_wav, wet_training_wav, dry_validation_wav, wet_validation_wav)