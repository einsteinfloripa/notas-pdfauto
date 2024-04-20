from fpdf import FPDF
#import main
class PDF(FPDF):
    def header(self):
        #logo
        self.image('einsteinlogo.png',10,8,25)
        self.image('einsteinlogo.png',177,8,25)
        #font
        self.set_text_color(113, 120, 197)
        pdf.set_font('times', 'BI', 26)
        #padding
        self.cell(80)
        #titulo
        self.cell(30,20,'Relatório Simulinho',ln=True,align='C')
        
        #lineSpace - espaço entre o titulo e o corpo do PDF
        self.ln(20)
#pdf config:
pdf = PDF('P','mm','a4')
pdf.add_page()
pdf.set_font('helvetica', 'BIU', 16)

#pdf.set_auto_page_break(auto=True, margin=15)
#def createPDFofStudent(nome,cpf,portugues,matematica,fisica,quimica,historia,biologia,geografia,filosofia,interdisciplinar,total_abs,total_per):
    


def tableNotes(data):
    pdf.add_page()
    pdf.set_font('helvetica', 'BIU', 16)
    tabledata = [["Questão","Disciplina","Alunos que acertaram","Alunos que erraram"]]
    for c in range(1,len(data)):
        questão = f'Questão{c}'
        lista = [data[questão]['discplina'],data[questão]['erros'],data[questão]['acertos']]
        tabledata.append(lista_de_questoes)
    with pdf.table() as table:
        for data_row in tabledata:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    

    