def series_resistance(resistances):
    total_resistance = sum(resistances)
    return f"{total_resistance:.1f} ohm{'s' if total_resistance != 1 else ''}"

# Examples
print(series_resistance([1, 5, 6, 3]))   # ➞ "15 ohms"
print(series_resistance([16, 3.5, 6]))    # ➞ "25.5 ohms"
print(series_resistance([0.5, 0.5]))      # ➞ "1.0 ohm"
