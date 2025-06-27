import pikepdf

# Open the PDF
pdf = pikepdf.open(r"F:\resume\nikita_chaubey.pdf")

# Modify the Title in the metadata
pdf.docinfo['/Title'] = 'Nikita Chaubey'

# Save the modified PDF
pdf.save("Nikita.pdf")
pdf.close()
