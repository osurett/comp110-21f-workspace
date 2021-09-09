"""Repeating a beat in a loop."""

__author__ = "730530127"

# Begin your solution here...
beat: str = str(input("What beat do you want to repeat? "))
reps: int = int(input("How many times do you want to repeat it? "))
beat_its: str = str(beat)
counter: int = 1
if reps <= 0:
    print("No beat...")
else:
    while counter < reps:
        beat_its = beat + " " + beat_its
        counter = counter + 1
    print(beat_its)
    