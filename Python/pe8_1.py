def seizoen(maand):
    if  3 <= maand <= 5 :
        print('lente')
    elif 9 <= maand <= 11:
        print('hefst')
    elif 6 <= maand <= 8:
        print('zomer')
    else :
        print('winter')
seizoen(12)