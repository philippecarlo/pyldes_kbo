from testcase1 import mustTestCase1
from testcase2 import mustTestCase2
from testcase3 import mustTestCase3
from testcase4 import mustTestCase4

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

# Create a new PDF file
pdf_file = "Report_must.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter)


result = []
report = ""
#Append all result to a lis
report+="- Validating against MUST conformance request:<br/>"
report+="A node from which all members of a collection can be discovered,can be found through a triple stating ex:C1 tree:view ex:N1 with ex:C1 being a tree:Collection and ex:N1 being a tree:Node.<br/>"
report+="- Conformance result:" + str(mustTestCase1().get_result()) + "<br/><br/>"
result.append(mustTestCase1().get_result())

report+="- Validating against MUST conformance request:<br/>"
report+="When the current page is a tree:Node, there MUST be a property linking the current page URL to the URI of the tree:Collection.<br/>"
report+="- Conformance result:" + str(mustTestCase2().get_result()) + "<br/><br/>"
result.append(mustTestCase2().get_result())


report+="- Validating against MUST conformance request:<br/>"
report+="Every entity linked from tree:view MUST be an entry point to retrieve all members of the collection.<br/>"
result.append(mustTestCase3().get_result())
report+="- Conformance result:" + str(mustTestCase3().get_result()) + "<br/><br/>"


report+="- Validating against MUST conformance request:<br/>"
report+="A tree:Relation MUST have one tree:node object of the type tree:Node.<br/>"
result.append(mustTestCase3().get_result())
report+="- Conformance result:" + str(mustTestCase3().get_result()) + "<br/><br/>"

#Calculate the final score
report+="The TREE conformance percentage for the Must requirement of current VSDS implementation is: "+ str((result.count(True)/len(result)*100))+" percent"

# Define the style for the paragraph
styles = getSampleStyleSheet()
paragraph_style = styles["Normal"]

# Create the Paragraph object with automatic content adjustment
paragraph = Paragraph(report, paragraph_style)

# Build the PDF document
elements = [paragraph]
doc.build(elements)