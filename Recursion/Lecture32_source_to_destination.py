def src_to_dest(src, dest):
    if src > dest:
        return -1
    if src == dest:
        print(dest)
        return
    print(src, end='->')
    src_to_dest(src+1, dest)

if __name__ == '__main__':
    src = int(input('Enter source: '))
    dest = int(input('Enter destination: '))
    src_to_dest(src, dest)