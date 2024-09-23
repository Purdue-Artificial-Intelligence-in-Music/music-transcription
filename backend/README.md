# Code Running Backend

This part of the project will run transcription models input by contestants. The input will be a **GitHub** repository with the model and a script in the format specified later. The model will be run on the Gilbreth computing cluster and will be scored after the model is run. The backend will run each model once every day with the latest version of the model from the main branch of the given Github repo.

## Input Script Overview

A Python script (`main.py`) that accepts command line arguments to process an audio file and generate a MIDI file.

### Command Line Arguments

- `-i`: Command line argument for the **input audio file**.
- `-o`: Command line argument for the **output MIDI file**.

### Script Functionality

The script will:

1. **Read the input audio file**.
2. **Use a model** to process the input.
3. **Write the resulting MIDI file** to the specified output location.

### Dependencies

A `requirements.txt` file will list all required Python packages.

- All dependencies must be installable via `pip`.
- If any Linux packages (other than FFmpeg) are required, they must be specified.

### Linux Packages

- We need to be notified of all Linux packages necessary other than FFmpeg
  - All packages must be loaded with **Lmod** or installed by an administrator if unavailable.
