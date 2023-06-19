from testcase1 import ShouldTestCase1
from testcase2 import ShouldTestCase2
from testcase3 import ShouldTestCase3
from testcase4 import ShouldTestCase4
from testcase5 import ShouldTestCase5
from testcase6 import ShouldTestCase6

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

# Create a new PDF file
pdf_file = "Report_Should.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter)

result = []
report = "<b>Conformance Test report against SHOULD SPECS</b><br/><br/><br/>"
# Append all result to a lis
report += "- Validating against Should conformance request:<br/>"
report += "Therefore a data publisher SHOULD annotate a tree:Collection instance with a SHACL shape. The tree:shape " \
          "points to a SHACL description of the shape (sh:NodeShape).<br/>"
report += "- Conformance result:" + str(ShouldTestCase1().get_result()) + "<br/><br/>"
result.append(ShouldTestCase1().get_result())

report += "- Validating against Should conformance request:<br/>"
report += "Note: the shape can be a blank node, or a named node on which you should follow your nose when it is " \
          "defined at a different HTTP URL<br/>"
report += "- Conformance result:" + str(ShouldTestCase2().get_result()) + "<br/><br/>"
result.append(ShouldTestCase2().get_result())

report += "- Validating against Should conformance request:<br/>"
report += "The tree:Relation’s tree:value SHOULD be set.<br/>"
result.append(ShouldTestCase3().get_result())
report += "- Conformance result:" + str(ShouldTestCase3().get_result()) + "<br/><br/>"

report += "- Validating against Should conformance request:<br/>"
report += "The object of tree:value SHOULD be accompanied by a data type when it is a literal value.<br/>"
result.append(ShouldTestCase4().get_result())
report += "- Conformance result:" + str(ShouldTestCase4().get_result()) + "<br/><br/>"

report += "- Validating against Should conformance request:<br/>"
report += "Every tree:Relation SHOULD have a tree:path indicating the path from the member to the object on which " \
          "the tree:Relation applies.<br/>"
result.append(ShouldTestCase5().get_result())
report += "- Conformance result:" + str(ShouldTestCase5().get_result()) + "<br/><br/>"

report += "- Validating against Should conformance request:<br/>"
report += "VOCAB-DCAT-2 is the standard for Open Data Portals by W3C. In order to find TREE compliant datasets in " \
          "data portals, there SHOULD be a dcat:accessURL from the dcat:Distribution to the entrypoint where the " \
          "tree:Collections are described. Furthermore, there SHOULD be a dct:conformsTo this URI: " \
          "https://w3id.org/tree.<br/>"
result.append(ShouldTestCase6().get_result())
report += "- Conformance result:" + str(ShouldTestCase6().get_result()) + "<br/><br/>"

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
