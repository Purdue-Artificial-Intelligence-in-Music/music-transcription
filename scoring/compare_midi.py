#!/opt/homebrew/bin/python3
"""
Name: compare_midi.py
Purpose: To compare 2 .mid files to score the transcribed output compared to the original sheet music
"""

__author__ = "Ojas Chaturvedi"
__github__ = "github.com/ojas-chaturvedi"
__license__ = "MIT"

import argparse
import pretty_midi
import numpy as np
import mir_eval

def extract_notes_with_offset(midi_file):
    # Load the MIDI file
    midi_data = pretty_midi.PrettyMIDI(midi_file)
    # Extract onset, offset, and pitch
    note_events = []
    for instrument in midi_data.instruments:
        if not instrument.is_drum:
            for note in instrument.notes:
                onset = note.start
                offset = note.end
                pitch = note.pitch
                note_events.append((onset, offset, pitch))
    # Sort by onset time
    note_events.sort(key=lambda x: x[0])
    return note_events

def prepare_data_for_mir_eval(note_events):
    intervals = []
    pitches = []
    for onset, offset, pitch in note_events:
        intervals.append([onset, offset])
        pitches.append(pitch)
    # Convert to NumPy arrays
    intervals = np.array(intervals)
    pitches = np.array(pitches)
    return intervals, pitches

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Compare two MIDI files for transcription accuracy.')
    parser.add_argument('--reference', required=True, help='Path to the reference MIDI file')
    parser.add_argument('--transcription', required=True, help='Path to the transcribed MIDI file')
    parser.add_argument('--output', required=False, help='Path to save the F1 score')
    args = parser.parse_args()

    # Extract and prepare notes from reference and transcribed MIDI files
    reference_notes = extract_notes_with_offset(args.reference)
    estimated_notes = extract_notes_with_offset(args.transcription)

    # Prepare intervals and pitches for both reference and estimated notes
    ref_intervals, ref_pitches = prepare_data_for_mir_eval(reference_notes)
    est_intervals, est_pitches = prepare_data_for_mir_eval(estimated_notes)

    # Compare the transcriptions
    precision, recall, f1, overlap = mir_eval.transcription.precision_recall_f1_overlap(
        ref_intervals, ref_pitches, est_intervals, est_pitches, 
        onset_tolerance=0.05, pitch_tolerance=50.0, offset_ratio=0.2, offset_min_tolerance=0.05, strict=False
    )

    # Optionally, save the F1 score to a file if an output path is provided
    if args.output:
        with open(args.output, "w") as file:
            file.write(f"{f1:.4f}\n")
    else:
        # Print the results
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        print(f"F1 Score: {f1:.4f}")
        print(f"Overlap: {overlap:.4f}")


if __name__ == '__main__':
    main()