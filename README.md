# Square Wave Approximation

## Description
This project demonstrates how a square wave can be approximated using a Fourier series by adding odd sine harmonics together.

The program uses NumPy for mathematical calculations and Matplotlib for visualization.

## Mathematical Formula

\[
f(x)=\frac{4}{\pi}\sum_{n=1,3,5,\ldots}^{25}\frac{\sin(nx)}{n}
\]

## Features
- Generates a square wave approximation using 13 odd harmonics.
- Uses NumPy for numerical calculations.
- Visualizes the resulting waveform using Matplotlib.
- Allows the number of harmonics to be adjusted.

## Requirements
- Python 3
- NumPy
- Matplotlib

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python main.py
```

## What I Learned
- Working with NumPy arrays.
- Using Fourier series to approximate periodic signals.
- Understanding odd harmonics.
- Using for loops to accumulate mathematical functions.
- Visualizing mathematical functions with Matplotlib.

## Future Improvements
- Add user-controlled harmonic counts.
- Visualize individual harmonics.
- Add an animation showing how the square wave develops as harmonics are added.