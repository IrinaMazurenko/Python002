seconds = 1234565
days = seconds // (24 * 60 * 60)
seconds = seconds % (24 * 60 * 60)
hours = seconds // (3600)
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print((f'{days}:{hours}:{minutes}:{seconds}'))
