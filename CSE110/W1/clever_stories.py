adjective = input("Adjective: ")
animal = input("Animal: ")
verb = input("Verb: ")
exclamation = input("Exclamation: ")
verb2 = input("Verb: ")
verb3 = input("Verb: ")
bold = "\033[1m"
end = "\033[0m"

#I put the blod mode in the variables nameded "bold" and "end" to highlight the words that were written by the user.

print(
    f"The other day, I was really in trouble. It all started when I saw a very {bold}{adjective}{end} {bold}{animal}{end} {bold}{verb}{end} down the hallway. \"{exclamation.capitalize()}!\" I yelled. "
    f"But all I could think to do was to {bold}{verb2}{end} over and over.\nMiraculously, that caused it to stop, but not before it tried to {bold}{verb3}{end} right in front of my family."
)