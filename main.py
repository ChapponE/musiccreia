import mido
import numpy as np
import tensorflow as tf

# Charger les données MIDI
mid = mido.MidiFile("my_song.mid")

# Obtenir les notes de la chanson
notes = []
for track in mid.tracks:
    for event in track:
        if event.type == "note_on":
            notes.append(event.note)

# Convertir les notes en un vecteur
notes_vector = np.array(notes)

# Normaliser les notes
notes_vector = notes_vector / 127.0

# Créer un ensemble de données
dataset = []
for i in range(len(notes_vector) - 1):
    x = notes_vector[i:i + 1]
    y = notes_vector[i + 1]
    dataset.append((x, y))

# Entrainer le LSTM
lstm = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(128, return_sequences=True),
    tf.keras.layers.LSTM(128),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(127, activation='sigmoid')
])

lstm.compile(optimizer='adam', loss='mse')

lstm.fit(dataset, epochs=100)

# Générer de la musique
generated_notes = lstm.predict(np.array([notes_vector[0:1]]))
generated_notes = generated_notes * 127.0

# Jouer la musique générée
mid = mido.MidiFile()
track = mido.Track()

for note in generated_notes:
    track.append(mido.Message('note_on', note=note, velocity=127, channel=0))
    track.append(mido.Message('note_off', note=note, velocity=127, channel=0))

mid.tracks.append(track)

mid.write("generated_song.mid")