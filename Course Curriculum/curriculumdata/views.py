from django.shortcuts import render
import pyrebase
from django.http import JsonResponse
import json
import gensim
import nltk
import math
from nltk.tokenize import word_tokenize
from PyPDF2 import PdfFileReader, PdfFileWriter


def home(request):
    return render(request, "test.html")


aicte = ["Data Structure & Algorithms Discrete Mathematics Computer Organization & Architecture  Operating Systems  Design and Analysis of Algorithms Database Management Systems Formal Language & Automata Theory  Object Oriented Programming Complier Design Computer Networks",
         "Graph Theory software Engineering Embedded Systems Artificial Intellegence Cryptography & network Security Internet of Things Data Analytics Machine Learning",
         "Theory of Computation Advanced Computer Architecture Artificial Intelligence Image Processing Soft Skills and Interpersonal Communication Graph Theory Software Engineering Advanced Algorithms Distributed Systems Machine Learning Digital Signal Processing Human Resource Development and Organizational Behavior Parallel and Distributed Algorithms Embedded Systems Data Mining Cloud Computing Cyber Law and Ethics Computational Complexity Advanced Operating Systems Soft Computing Human Computer Interaction Computational Geometry Low Power Circuits and Systems Speech and Natural Language Processing Electronic Design Automation Comparative Study Queuing Theory and Modeling Fault Tolerant Computing  Data Analytics Computer Graphics Indian Music System"
         ]
coredata = "Data Structure & Algorithms Discrete Mathematics Computer Organization & Architecture  Operating Systems  Design and Analysis of Algorithms Database Management Systems Formal Language & Automata Theory  Object Oriented Programming Complier Design Computer Networks"
prodata = "Graph Theory software Engineering Embedded Systems Artificial Intellegence Cryptography & network Security Internet of Things Data Analytics Machine Learning"
opendata = "Theory of Computation Advanced Computer Architecture Artificial Intelligence Image Processing Soft Skills and Interpersonal Communication Graph Theory Software Engineering Advanced Algorithms Distributed Systems Machine Learning Digital Signal Processing Human Resource Development and Organizational Behavior Parallel and Distributed Algorithms Embedded Systems Data Mining Cloud Computing Cyber Law and Ethics Computational Complexity Advanced Operating Systems Soft Computing Human Computer Interaction Computational Geometry Low Power Circuits and Systems Speech and Natural Language Processing Electronic Design Automation Comparative Study Queuing Theory and Modeling Fault Tolerant Computing  Data Analytics Computer Graphics Indian Music System"

aictebs1= ["Physics","Mathematics","Mathematics","Chemistry","Biology","Mathematics","Environmental Sciences","Probability and Statistics","Discrete Mathematics"] 
aictees1= ["Electrical","Graphics","Programming","Workshop","Analog Electronic Circuits","Electronics","Signals and System","Materials Science","Mechanics","Electrical Engineering","Electronics","Programming","Simulation Laboratory","Thermodynamics","Mechanics","Solid Mechanics","Materials"]
pccaicte1=["Data Structure","Discrete Mathematics","Computer Organization and Architecture","Operating System","Algorithm","Database","Formal Language and Automata Theory","Object Oriented Programming","Complier Design","Computer Network","IT Workshop","Digital System","Software Engineering","Cryptography","Object Oriented Analysis and Design","Distributed","Graph Theory","Artificial Intelligence","Computer Graphics","Simulation and Modeling","Web","Embedded Computing System","Software Testing","Data Mining","Advanced Computer Architecture","Approximation of Algorithms","Mobile Computing","Pattern Recognition","Information Retrieval","Software Architecture","Design and Algorithm","Soft Computing","Game Theory","Combinational Optimization","Computer Vision","Software Project Management","Human Computer Interface","Cloud Computing","Web Service","Bioinformatics","Script Programming","Multimedia Computing"]
peaicte1=["Graph Theory","Software Engineering","Embedded System","Artificial Intelligence","Cryptography and Network Security","Internet of Things","Data Analytic","Machine Learning"]
oeaicte1=["Database","Software Engineering","Design and Analysis of Algorithms","Disaster Management","Project Management","Engineering Risk–Benefit Analysis","Infrastructure Systems Planning","Sustainable Development","Innovation","Enterpreneurship","Technology","Knowledge Management"]

aictebs = ["Physics","Mathematics II","Mathematics I","Chemistry I","Biology ","Mathematics III","Environmental Sciences ","Probability and Statistics ","Discrete Mathematics"] 
aictees = ["Basic Electrical Engineering","Engineering Graphics & Design","Programming for Problem Solving","Workshop/Manufacturing Practices","Analog Electronic Circuits","Digital Electronics","Signals and Systems","Engineering Graphics ","Engineering Workshop ","Materials Science ","Basic Engineering Mechanics","Basic Electrical Engineering ","Basic Electrical Engineering Laboratory ","Basic Electronics Engineering ","Basic Electronics EngineeringLaboratory","Computer Programming ","Computer Programming Laboratory 0","Basic Simulation Laboratory ","Bassic Thermodynamics ","Solid Mechanics & Fluid Mechanics ","Solid Mechanics & Fluid Mechanics Laboratory","Engineering Mechanics ","Solid Mechanics ","Thermodynamics ","Engineering Materials"]
pccaicte=["Data Structure & Algorithms","Discrete Mathematics","Computer Organization &Architecture","Operating Systems","Design and Analysis of Algorithms","Database Management Systems","Formal Language & Automata Theory","Object Oriented Programming","Complier Design","Computer Networks","IT Workshop","Digital Systems  ","Software Engineering ","Cryptography & Information Security ","Object Oriented Analysis and Design ","Distributed Computing Systems ","Graph Theory ","Artificial Intelligence ","Computer Graphics and Visualization ","Simulation and Modeling ","Internet Web Programming ","Embedded Computing Systems ","Software Testing ","Data Mining ","Advanced Computer Architecture ","Approximation of Algorithms ","Mobile Computing ","Pattern Recognition ","Information Retrieval ","Software Architecture ","VLSI Design & Algorithms ","Soft Computing ","Game Theory ","Combinational Optimization ","Computer Vision ","Software Project Management ","Human Computer Interface ","Cloud Computing ","Web Service and Service Oriented Architecture","Bioinformatics ","Script Programming ","Multimedia Computing ","Project 1","Project 2"]
peaicte=["Graph Theory","Software Engineering","Embedded Systems","Artificial Intelligence","Cryptography & Network Security","Internet of Things","Data Analytics","Machine Learning"]
oeaicte=["Database Management Systems ","Software Engineering ","Design and Analysis of Algorithms ","Disaster Management","Project Management ","Engineering Risk–Benefit Analysis ","Infrastructure Systems Planning ","Planning for Sustainable Development ","Managing Innovation and Enterpreneurship","Global Strategy and Technology","Knowledge Management"] 

def pdfcompare(request):
    return render(request, "pdfcompare.html")

def test(request):
    return render(request, "test.html")

def fun(x,pdf):
    Present=[]
    notfoundlist=[]
    for sub in x:
        c=False
        for page in pdf.pages:
            page_text = page.extractText()
            if sub in page_text:
                Present.append(sub)
                c=True
                break
        if c==False:
            notfoundlist.append(sub)
    return Present,notfoundlist

def res(request):
    if request.method=="POST":
        file=request.POST.get('file_upload')
        pdf=PdfFileReader(file)
        l1,notfoundlistbs=(fun(aictebs1,pdf))
        l2,notfoundlistes=(fun(aictees1,pdf))
        l3,notfoundlistpcc=(fun(pccaicte1,pdf))
        l4,notfoundlistpe=(fun(peaicte1,pdf))
        l5,notfoundlistoe=(fun(oeaicte1,pdf))  

        p1=(len(l1)/len(aictebs1)*100)
        p2=(len(l2)/len(aictees1)*100)
        p3=(len(l3)/len(pccaicte1)*100)
        p4=(len(l4)/len(peaicte1)*100)
        p5=(len(l5)/len(oeaicte1)*100)

        r1=math.ceil(len(l1)/len(aictebs1)*10)
        r2=math.ceil(len(l2)/len(aictees1)*10)
        r3=math.ceil(len(l3)/len(pccaicte1)*10)
        r4=math.ceil(len(l4)/len(peaicte1)*10)
        r5=math.ceil(len(l5)/len(oeaicte1)*10)

        rating=(r1+r2+r3+r4+r5)/5
        print(notfoundlistpcc)
        params={"notfoundlistoe":notfoundlistoe,"notfoundlistpe":notfoundlistpe,"notfoundlistpcc":notfoundlistpcc,"notfoundlistbs":notfoundlistbs,"notfoundlistes":notfoundlistes,"rating":rating,"r1":r1,"r2":r2,"r3":r3,"r4":r4,"r5":r5,"l1":l1,"p1":p1,"l2":l2,"p2":p2,"l3":l3,"p3":p3,"l4":l4,"p4":p4,"l5":l5,"p5":p5,"aictebs1":aictebs1,"aictees1":aictees1,"pccaicte1":pccaicte1,"peaicte1":peaicte1,"oeaicte1":oeaicte1}
        return render(request,"res.html",params)
    return render(request,"home.html")

def result(request):
    collegename = request.POST.get("collegename")
    branch = request.POST.get("dropdown")
    corelist = []
    prolist = []
    openlist = []
    pelist=[]
    oelist=[]
    bs = request.POST.get("core")
    es = request.POST.get("professional")
    pcc = request.POST.get("open")
    pe = request.POST.get("pe")
    oe = request.POST.get("oe")
    oecnt=0
    pecnt=0
    bscnt=0
    escnt=0
    pcccnt=0
    string=""
    for i, v in enumerate(bs):
        if v != ',':
            string = string+v
        elif i == len(bs):
            bscnt=bscnt+1
            break
        else:
            bscnt=bscnt+1
            string=""
    string = ""
    for i, v in enumerate(es):
        if v != ',':
            string = string+v
        elif i == len(es):
            escnt=escnt+1
            break
        else:
            escnt=escnt+1
            string=""
    string = ""
    for i, v in enumerate(pcc):
        if v != ',':
            string = string+v
        elif i == len(pcc):
            pcccnt=pcccnt+1
            break
        else:
            pcccnt=pcccnt+1
            string=""
    string = ""
    for i, v in enumerate(pe):
        if v != ',':
            string = string+v
        elif i == len(pe):
            pecnt=pecnt+1
            break
        else:
            pecnt=pecnt+1
            string=""
    string = ""
    for i, v in enumerate(oe):
        if v != ',':
            string = string+v
        elif i == len(oe):
            oecnt=oecnt+1
            break
        else:
            oecnt=oecnt+1
            string=""
    doc=[]
    doc.append(bs)
    doc.append(es)
    doc.append(pcc)
    doc.append(pe)
    doc.append(oe)
    raw_documents=["Physics Mathematics II Mathematics I Chemistry I Biology  Mathematics III Environmental Sciences  Probability and Statistics  Discrete Mathematics"
    ,"Basic Electrical Engineering Engineering Graphics & Design Programming for Problem Solving Workshop/Manufacturing Practices Analog Electronic Circuits Digital Electronics Signals and Systems Engineering Graphics  Engineering Workshop  Materials Science  Basic Engineering Mechanics Basic Electrical Engineering  Basic Electrical Engineering Laboratory  Basic Electronics Engineering  Basic Electronics EngineeringLaboratory Computer Programming  Computer Programming Laboratory 0 Basic Simulation Laboratory  Bassic Thermodynamics  Solid Mechanics & Fluid Mechanics  Solid Mechanics & Fluid Mechanics Laboratory Engineering Mechanics  Solid Mechanics  Thermodynamics  Engineering Materials" 
    ,"Data Structure & Algorithms Discrete Mathematics Computer Organization &Architecture Operating Systems Design and Analysis of Algorithms Database Management Systems Formal Language & Automata Theory Object Oriented Programming Complier Design Computer Networks IT Workshop Digital Systems   Software Engineering  Cryptography & Information Security  Object Oriented Analysis and Design  Distributed Computing Systems  Graph Theory  Artificial Intelligence  Computer Graphics and Visualization  Simulation and Modeling  Internet Web Programming  Embedded Computing Systems  Software Testing  Data Mining  Advanced Computer Architecture  Approximation of Algorithms  Mobile Computing  Pattern Recognition  Information Retrieval  Software Architecture  VLSI Design & Algorithms  Soft Computing  Game Theory  Combinational Optimization  Computer Vision  Software Project Management  Human Computer Interface  Cloud Computing  Web Service and Service Oriented Architecture Bioinformatics  Script Programming  Multimedia Computing  Project 1 Project 2","Graph Theory Software Engineering Embedded Systems Artificial Intelligence Cryptography & Network Security Internet of Things Data Analytics Machine Learning"
,"Database Management Systems  Software Engineering  Design and Analysis of Algorithms  Disaster Management Project Management  Engineering Risk–Benefit Analysis  Infrastructure Systems Planning  Planning for Sustainable Development  Managing Innovation and Enterpreneurship Global Strategy and Technology Knowledge Management" 
]
 
    gen_docs = [[w.lower() for w in word_tokenize(text)] 
            for text in raw_documents]
    dictionary = gensim.corpora.Dictionary(gen_docs)
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
    tf_idf = gensim.models.TfidfModel(corpus)
    sims = gensim.similarities.Similarity('',tf_idf[corpus],num_features=len(dictionary))

    for line in doc:
        query_doc = [w.lower() for w in word_tokenize(line)]
        query_doc_bow = dictionary.doc2bow(query_doc)

    query_doc_tf_idf = tf_idf[query_doc_bow]
    r1=int(sims[query_doc_tf_idf][0]*10)
    r2=int(sims[query_doc_tf_idf][1]*10)
    r3=int(sims[query_doc_tf_idf][2]*10)
    r4=int(sims[query_doc_tf_idf][3]*10)
    r5=int(sims[query_doc_tf_idf][4]*10)
    params={"ans1":sims[query_doc_tf_idf][0]*100,"ans2":sims[query_doc_tf_idf][1]*100,"ans3":sims[query_doc_tf_idf][2]*100,"ans4":sims[query_doc_tf_idf][3]*100,"ans5":sims[query_doc_tf_idf][4]*100,"aictebs": aictebs,
            "aictees": aictees, "pccaicte": pccaicte,"peaicte":peaicte,"oeaicte":oeaicte,"bscnt":str(bscnt),"escnt":str(escnt),"pcccnt":str(pcccnt),"pecnt":str(pecnt),"oecnt":str(oecnt),"r1":r1,"r2":r2,"r3":r3,"r4":r4,"r5":r5}
    return render(request, "result.html", params)


def result1(request):
    collegename = request.POST.get("collegename")
    print("collegname", collegename)

    corelist = []
    prolist = []
    openlist = []
    pelist=[]
    oelist=[]
    core = request.POST.get("core")
    professional = request.POST.get("professional")
    open = request.POST.get("open")
    pe = request.POST.get("pe")
    oe = request.POST.get("oe")
    string = ""
    for i, v in enumerate(core):
        if v != ',':
            string = string+v
        elif i == len(core):
            corelist.append(string)
            break
        else:
            corelist.append(string)
            string = ""
    string = ""
    for i, v in enumerate(professional):
        if v != ',':
            string = string+v
        elif i == len(professional):
            prolist.append(string)
            break
        else:
            prolist.append(string)
            string = ""
    string = ""
    for i, v in enumerate(open):
        if v != ',':
            string = string+v
        elif i == len(open):
            openlist.append(string)
            break
        else:
            openlist.append(string)
            string = ""
    string = ""
    for i, v in enumerate(pe):
        if v != ',':
            string = string+v
        elif i == len(pe):
            pelist.append(string)
            break
        else:
            pelist.append(string)
            string = ""
    string = ""
    for i, v in enumerate(oe):
        if v != ',':
            string = string+v
        elif i == len(oe):
            oelist.append(string)
            break
        else:
            oelist.append(string)
            string = ""
    string = ""
    
    return render(request, "result.html")

def display(request):
    aictebs = ["Physics","Mathematics II","Mathematics I","Chemistry I","Biology ","Mathematics III","Environmental Sciences ","Probability and Statistics ","Discrete Mathematics"] 


    aictees = ["Basic Electrical Engineering","Engineering Graphics & Design","Programming for Problem Solving","Workshop/Manufacturing Practices","Analog Electronic Circuits","Digital Electronics","Signals and Systems","Engineering Graphics ","Engineering Workshop ","Materials Science ","Basic Engineering Mechanics","Basic Electrical Engineering ","Basic Electrical Engineering Laboratory ","Basic Electronics Engineering ","Basic Electronics EngineeringLaboratory","Computer Programming ","Computer Programming Laboratory 0","Basic Simulation Laboratory ","Bassic Thermodynamics ","Solid Mechanics & Fluid Mechanics ","Solid Mechanics & Fluid Mechanics Laboratory","Engineering Mechanics ","Solid Mechanics ","Thermodynamics ","Engineering Materials"]

    aictepcc = ["Data Structure & Algorithms","Discrete Mathematics","Computer Organization &Architecture","Operating Systems","Design and Analysis of Algorithms","Database Management Systems","Formal Language & Automata Theory","Object Oriented Programming","Complier Design","Computer Networks","IT Workshop","Digital Systems  ","Software Engineering ","Cryptography & Information Security ","Object Oriented Analysis and Design ","Distributed Computing Systems ","Graph Theory ","Artificial Intelligence ","Computer Graphics and Visualization ","Simulation and Modeling ","Internet Web Programming ","Embedded Computing Systems ","Software Testing ","Data Mining ","Advanced Computer Architecture ","Approximation of Algorithms ","Mobile Computing ","Pattern Recognition ","Information Retrieval ","Software Architecture ","VLSI Design & Algorithms ","Soft Computing ","Game Theory ","Combinational Optimization ","Computer Vision ","Software Project Management ","Human Computer Interface ","Cloud Computing ","Web Service and Service Oriented Architecture","Bioinformatics ","Script Programming ","Multimedia Computing"]
    params = {"aictecore": aictebs,"aictepro": aictees, "aicteopen": aictepcc}
    return render(request, "display.html", params)

'''def as():
    for i, v in enumerate(core):
        if v != ',':
            string = string+v
        elif i == len(core):
            print(string)
            break
        else:
            corelist.append(string)
            string = ""
    string = ""
    for i, v in enumerate(professional):
        if v != ',':
            string = string+v
        elif i == len(professional):
            prolist.append(string)
            break
        else:
            prolist.append(string)
            string = ""
    string = ""
    for i, v in enumerate(open):
        if v != ',':
            string = string+v
        elif i == len(open):
            openlist.append(string)
            break
        else:
            openlist.append(string)
            string = ""
            '''
