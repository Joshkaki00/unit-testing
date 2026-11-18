def extract_position(line):
    """Return the x position from a log line, or None if missing/invalid."""
    if not line:
        return None
    if 'debug' in line or 'error' in line:
        return None
    if 'x:' not in line:
        return None
    start_index = line.find('x:') + 2
    return line[start_index:].split()[0] if line[start_index:].strip() else None


if __name__ == "__main__":
    print(extract_position('|error| numerical calculations could not converge.'))
    print(extract_position('|update| the positron location in the particle accelerator is x:21.432'))
