import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import time
import wave

CHUNK = 4096	# it's the number ob bytes read by the mic 
RATE = 44100	# it's the sample frequence
padding = 100	# padding => better fft line
nfft = padding*CHUNK
freq = np.linspace(0, RATE, nfft)
fig, ax = plt.subplots()

# open audio stream
p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,
			  channels=1,rate=RATE,
			  input=True,
              frames_per_buffer=CHUNK)


# init graph
line, = ax.plot(freq, np.zeros(nfft))
ax.set_ylim(-10, 10**5)
ax.set_xlim(0, 0.5*RATE)
fig.show()

while True: 
	data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
	auto_corr = np.fft.fft(data, nfft)
	line.set_ydata(np.abs(auto_corr))
	fig.canvas.draw()
	fig.canvas.flush_events()

# close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()

