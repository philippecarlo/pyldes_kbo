from testcase1 import MustTestCase1
from testcase2 import MustTestCase2
from testcase3 import MustTestCase3
from testcase4 import MustTestCase4

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

# Create a new PDF file
pdf_file = "Report_must.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter)

result = []
report = ""
# Append all result to a lis
report += "- Validating against MUST conformance request:<br/>"
report += "A node from which all members of a collection can be discovered,can be found through a triple stating " \
          "ex:C1 tree:view ex:N1 with ex:C1 being a tree:Collection and ex:N1 being a tree:Node.<br/>"
report += "- Conformance result:" + str(MustTestCase1().get_result()) + "<br/><br/>"
result.append(MustTestCase1().get_result())

report += "- Validating against MUST conformance request:<br/>"
report += "When the current page is a tree:Node, there MUST be a property linking the current page URL to the URI of " \
          "the tree:Collection.<br/>"
report += "- Conformance result:" + str(MustTestCase2().get_result()) + "<br/><br/>"
result.append(MustTestCase2().get_result())

report += "- Validating against MUST conformance request:<br/>"
report += "Every entity linked from tree:view MUST be an entry point to retrieve all members of the collection.<br/>"
result.append(MustTestCase3().get_result())
report += "- Conformance result:" + str(MustTestCase3().get_result()) + "<br/><br/>"

report += "- Validating against MUST conformance request:<br/>"
report += "A tree:Relation MUST have one tree:node object of the type tree:Node.<br/>"
result.append(MustTestCase3().get_result())
report += "- Conformance result:" + str(MustTestCase3().get_result()) + "<br/><br/>"

# Calculate the final score
report += "The conform score of current implementation to the TREE SPEC is: " + str(
    (result.count(True) / len(result) * 100)) + " percent"

# Define the style for the paragraph
styles = getSampleStyleSheet()
paragraph_style = styles["Normal"]

# Create the Paragraph object with automatic content adjustment
paragraph = Paragraph(report, paragraph_style)

# Build the PDF document
elements = [paragraph]
doc.build(elements)
