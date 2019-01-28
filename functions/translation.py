from Bio import SeqIO
from Bio.Seq import Seq
from tkinter import *
from tkinter import filedialog
import tkinter as tk

def protein(codonstop , tostop):


    win =tk.Tk()
    sv1 = StringVar()
    sv2 = StringVar()
    Label(win, text="Input File").grid(row=0)
    Label(win, text="Output File").grid(row=1)

    e1 = Entry(win, textvariable=sv1)
    e2 = Entry(win, textvariable=sv2)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)


    outfile = e2.get()

    def inpo1():
        namein = filedialog.askopenfilename(parent=win)
        e1.insert(END, namein)
        print(e1.get())


    def inpo2():
        namein = filedialog.asksaveasfilename(parent=win)
        e2.insert(END, namein)
        print(e2.get())


    def out():

        for record in SeqIO.parse(str(e1.get()), "fasta"):
            codon_table = codonstop
            to_stop = tostop
            file = open(e2.get(), "w")

        for record in SeqIO.parse(str(e1.get()), "fasta"):
            if codon_table == "Standard":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=1, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=1, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))

            elif codon_table == "Vertebrate Mitochondrial":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=2, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=2, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))

            elif codon_table == "Yeast Mitochondrial":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=3, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=3, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))

            elif codon_table == "Mold Mitochondrial; Protozoan Mitochondrial; Coelenterate Mitochondrial; Mycoplasma; Spiroplasma":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=4, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=4, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))



            elif codon_table == "Invertebrate Mitochondrial":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=5, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=5, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))


            elif codon_table == "Ciliate Nuclear; Dasycladacean Nuclear; Hexamita Nuclear":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=6, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=6, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))



            elif codon_table == "Echinoderm Mitochondrial; Flatworm Mitochondrial":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=9, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=9, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))



            elif codon_table == "Euplotid Nuclear":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=10, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=10, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))



            elif codon_table == "Bacterial, Archaeal and Plant Plastid":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=11, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=11, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))



            elif codon_table == "Alternative Yeast Nuclear":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=12, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=12, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))



            elif codon_table == "Ascidian Mitochondrial":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=13, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=13, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))




            elif codon_table == "Alternative Flatworm Mitochondrial":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=14, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=14, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))



            elif codon_table == "Blepharisma Macronuclear":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=15, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=15, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))



            elif codon_table == "Chlorophycean Mitochondrial":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=16, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=16, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))




            elif codon_table == "Trematode Mitochondrial":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=21, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=21, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))





            elif codon_table == "Scenedesmus obliquus Mitochondrial":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=22, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=22, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))





            elif codon_table == "Thraustochytrium Mitochondrial":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=23, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=23, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))


            elif codon_table == "Pterobranchia Mitochondrial":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=24, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=24, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))

            elif codon_table == "Candidate Division SR1 and Gracilibacteria":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=25, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=25, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))


            elif codon_table == "Pachysolen tannophilus Nuclear":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=26, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=26, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))


            elif codon_table == "Karyorelict Nuclear":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=27, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=27, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))


            elif codon_table == "Condylostoma Nuclear":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=28, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=28, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))


            elif codon_table == "Mesodinium Nuclear":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=29, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=29, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))



            elif codon_table == "Peritrich Nuclear":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=30, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=30, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))



            elif codon_table == "Blastocrithidia Nuclear":
                if to_stop == 1:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=31, to_stop=True)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))
                else:
                    print(">%s" % record.id)
                    coding_dna = Seq("%s" % record.seq)
                    translate = coding_dna.translate(table=31, to_stop=False)
                    print("%s" % translate)
                    file.write(str(">%s\n%s\n\n" % (record.id, translate)))


        file.close()


        r = open(e2.get(), 'r').read()
        root = Tk()
        S = Scrollbar(root)
        T = Text(root, height=50, width=500)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        S.config(command=T.xview)
        T.config(yscrollcommand=S.set)
        T.config(xscrollcommand=S.set)
        quote = r
        T.insert(END, quote, 'color')
        mainloop()






    Button(win, text='choose..', command=inpo1).grid(row=0, column=2, sticky=W, pady=4)
    Button(win, text='choose..', command=inpo2).grid(row=1, column=2, sticky=W, pady=4)
    Button(win, text='Done', command=out).grid(row=2, column=1, sticky=W, pady=4, padx=40)

    mainloop()










