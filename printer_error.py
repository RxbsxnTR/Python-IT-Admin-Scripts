def printer_error(s):
    errors=0
    for l in s:
        if l in "abcdefghijklm":
            continue
        elif l in "nopqrstuvwxyz":
            errors += 1
    return f"{errors}/{len(s)}"

print(printer_error("aaabbbbhaijjjmdasfafdxzczx")) 