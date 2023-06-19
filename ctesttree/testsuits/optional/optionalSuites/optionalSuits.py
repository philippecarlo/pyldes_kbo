from testcase1 import OptionalTestCase1
from testcase2 import OptionalTestCase2
from testcase3 import OptionalTestCase3
from testcase4 import OptionalTestCase4
from testcase5 import OptionalTestCase5
from testcase6 import OptionalTestCase6

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

# Create a new PDF file
pdf_file = "Report_Optional.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter)

result = []
report = "<b>Conformance Test report against Optional SPECS</b><br/><br/><br/>"
# Append all result to a lis
report += "- Validating against Optional conformance request:<br/>"
report += "Note: For compatibility with the Solid specifications, a ShEx shape may also be given (see the chapter on " \
          "compatibility bellow).<br/>"
report += "- Conformance result:" + str(OptionalTestCase1().get_result()) + "<br/><br/>"
result.append(OptionalTestCase1().get_result())

report += "- Validating against Optional conformance request:<br/>"
report += "Multiple tree:view links MAY be provided <br/>"
report += "- Conformance result:" + str(OptionalTestCase2().get_result()) + "<br/><br/>"
result.append(OptionalTestCase2().get_result())

report += "- Validating against Optional conformance request:<br/>"
report += " A tree:Node element MAY have one or more tree:relation properties.<br/>"
result.append(OptionalTestCase3().get_result())
report += "- Conformance result:" + str(OptionalTestCase3().get_result()) + "<br/><br/>"

report += "- Validating against Optional conformance request:<br/>"
report += "All possible combinations of e.g., shacl:alternativePath, shacl:inversePath or shacl:inLanguage in the " \
          "SHACL spec can be used.<br/>"
result.append(OptionalTestCase4().get_result())
report += "- Conformance result:" + str(OptionalTestCase4().get_result()) + "<br/><br/>"

report += "- Validating against Optional conformance request:<br/>"
report += "Check that LDES Server supports tree:path refers to an implicit property.<br/>"
result.append(OptionalTestCase5().get_result())
report += "- Conformance result:" + str(OptionalTestCase5().get_result()) + "<br/><br/>"

report += "- Validating against Optional conformance request:<br/>"
report += "When a tree:path is defined, mind that you also may have to check the language of the element using the " \
          "property shacl:inLanguage More languages MAY be set. When no language is set, all strings are compared.<br/>"
result.append(OptionalTestCase6().get_result())
report += "- Conformance result:" + str(OptionalTestCase6().get_result()) + "<br/><br/>"

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
