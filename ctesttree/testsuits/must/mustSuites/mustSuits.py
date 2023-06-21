# from testcase1 import MustTestCase1
from datetime import datetime
from testcase1 import MustTestCase1
from testcase2 import MustTestCase2
from testcase3 import MustTestCase3
from testcase4 import MustTestCase4
from testcase5 import MustTestCase5
from testcase6 import MustTestCase6
from testcase7 import MustTestCase7
from testcase8 import MustTestCase8
from testcase9 import MustTestCase9

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

# Create a new PDF file
output_directory = "../../../reports"
output_file = "report_must_spec.pdf"
output_path = f"{output_directory}/{output_file}"
doc = SimpleDocTemplate(output_path, pagesize=letter)

result = []
report = "<b>Conformance Test report against MUST SPECS at: "+str(datetime.now())+"</b><br/><br/><br/>"
# Append all result to a list
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
report += "- Conformance result:" + str(result[-1]) + "<br/><br/>"

report += "- Validating against MUST conformance request:<br/>"
report += "A tree:Relation MUST have one tree:node object of the type tree:Node.<br/>"
result.append(MustTestCase4().get_result())
report += "- Conformance result:" + str(MustTestCase4().get_result()) + "<br/><br/>"
#
report += "- Validating against MUST conformance request:<br/>"
report += "The result of the evaluation of the tree:path, is the value that MUST be compared to the tree:value.<br/>"
result.append(MustTestCase5().get_result())
report += "- Conformance result:" + str(MustTestCase5().get_result()) + "<br/><br/>"

report += "- Validating against MUST conformance request:<br/>"
report += "When no tree:path is defined," \
          "the tree:value MUST be compared to all members’ triples that can be compared to the tree:value as defined " \
          "by the type of the relation (or when no members or collection are defined," \
          "on every triple in the page). When due to rdfs:range incompatibility," \
          "the object cannot be compared, the object will not be considered for comparison.<br/>"
result.append(MustTestCase6().get_result())
report += "- Conformance result:" + str(MustTestCase6().get_result()) + "<br/><br/>"

report += "- Validating against MUST conformance request:<br/>"
report += "The strings MUST then be compared according to case-sensitive unicode ordering.<br/>"
result.append(MustTestCase7().get_result())
report += "- Conformance result:" + str(MustTestCase7().get_result()) + "<br/><br/>"

report += "- Validating against MUST conformance request:<br/>"
report += "When using tree:GeospatiallyContainsRelation, the tree:path MUST refer to a literal containing a WKT " \
          "string, such as geosparql:asWKT.<br/>"
result.append(MustTestCase8().get_result())
report += "- Conformance result:" + str(result[-1]) + "<br/><br/>"

report += "- Validating against MUST conformance request:<br/>"
report += "When using relations such as tree:LessThanRelation or tree:GreaterThanRelation, the time literals need to " \
          "be compared according to these 3 possible data types: xsd:date, xsd:dateTime or xsd:dateTimeStamp.<br/>"
result.append(MustTestCase9().get_result())
report += "- Conformance result:" + str(MustTestCase9().get_result()) + "<br/><br/>"

# Calculate the final score
report += "The conform Percentage of current implementation to the MUST TREE SPEC is: " + str(
    (result.count(True) / len(result) * 100)) + " percent<br/>"

if False in result:
    report += "The conform score: 0"
else:
    report += "The conform score: 100 "

# Define the style for the paragraph
styles = getSampleStyleSheet()
paragraph_style = styles["Normal"]

# Create the Paragraph object with automatic content adjustment
paragraph = Paragraph(report, paragraph_style)

# Build the PDF document
elements = [paragraph]
doc.build(elements)
