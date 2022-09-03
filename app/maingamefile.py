def check(level: str, code: str):
    with open(f"python-levels/{level}.answer", 'r') as f:
        output = ''.join((line) for line in f)
        print(output)
        if output == code:
            return True
        else:
            return False