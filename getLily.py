import abjad

def getLily(path, mode, BPM):
    file = open(f'{path}/{mode}_sheet.txt', 'r')
    data = file.readlines()
    # voice = abjad.Voice(data[0], name = 'voice')
    staff = abjad.Staff(data[0], name = 'staff')
    mark = abjad.MetronomeMark((1, 4), BPM)
    abjad.attach(mark, staff[0])

    abjad.persist.as_pdf(staff, pdf_file_path=f'{path}/{mode}.pdf')
