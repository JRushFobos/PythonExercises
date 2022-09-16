def convert(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'Days:{days} Hours:{hours} Minutes:{minutes} Seconds:{seconds}')

convert(1234565)