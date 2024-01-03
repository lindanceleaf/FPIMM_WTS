import abjad

def getLily(path, mode):
    file = open(f'{path}/{mode}_sheet.txt', 'r')
    data = file.readlines()
    voice = abjad.Voice(data[0], name = 'voice')
    staff = abjad.Staff([voice], name = 'staff')
    abjad.persist.as_pdf(staff, pdf_file_path=f'{path}/{mode}.pdf')
