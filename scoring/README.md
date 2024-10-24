# MIDI Comparison Script

This script compares two MIDI files (a reference and a transcribed version) using evaluation metrics such as precision, recall, F1 score, and overlap. It is designed for analyzing the performance of Automatic Music Transcription (AMT) models, making it useful for competitions like the 2025 Automatic Music Transcription Challenge held by the AI for Musicians group at Purdue University.

## Features

- Extracts note events (onset, offset, pitch) from MIDI files using `pretty_midi`.
- Evaluates transcription accuracy using `mir_eval` with metrics like precision, recall, F1 score, and overlap.
- Outputs results to the terminal or saves the F1 score to a file.

## Prerequisites

Make sure you have Python 3 installed along with the required libraries:

```bash
pip install pretty_midi mir_eval numpy
```

## Usage

Run the script from the terminal using:

```bash
python compare_midi.py --reference <path_to_reference_midi> --transcription <path_to_transcribed_midi>
```

**Optional: Save the F1 Score to a File**
To save the F1 score to a file, use the --output flag:

```bash
python compare_midi.py --reference <path_to_reference_midi> --transcription <path_to_transcribed_midi> --output f1_score.txt
```

## Parameters

--reference: Path to the reference MIDI file.
--transcription: Path to the transcribed MIDI file generated by the AMT model.
--output (optional): Path to save the computed F1 score as a text file.

## Output

Given no --output flag, the script prints the following metrics to the terminal:

- Precision: Proportion of correctly identified notes in the transcribed MIDI.
- Recall: Proportion of reference notes correctly identified in the transcription.
- F1 Score: Harmonic mean of precision and recall, providing a balanced measure of transcription accuracy.
- Overlap: Average overlap ratio between matched notes, reflecting timing alignment accuracy.

If the --output flag is specified, the F1 score is saved to a file and the metrics are not displayed to the terminal.
