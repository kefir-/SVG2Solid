from FreeCAD import Base
import importSVG
import Part

def extrudeSVG(filename, thickness):

    doc = App.ActiveDocument

    # Import SVG
    importSVG.insert(filename, doc.Name) # returns None
    Gui.SendMsgToActiveView("ViewFit")
    # Get latest object in document:
    SVG = doc.Objects[-1]
    # Gui.ActiveDocument.activeObject()
    # Gui.ActiveDocument.path3400
    # All objects: App.ActiveDocument.Objects[0] etc

    # Create face, hide SVG
    tmp = Part.Face(Part.Wire(Part.__sortEdges__(SVG.Shape.Edges)))
    if tmp.isNull(): raise RuntimeError('Failed to create face')

    doc.addObject('Part::Feature', 'SVGFace').Shape = tmp
    del tmp
    SVG.ViewObject.Visibility=False

    # Extrude face
    SVGFace = doc.Objects[-1]
    SVGExtrude = doc.addObject("Part::Extrusion", "SVGExtrude")
    SVGExtrude.Base = doc.SVGFace
    SVGExtrude.Dir = (0, 0, thickness)
    SVGExtrude.Solid = (True)
    SVGExtrude.TaperAngle = (0)
    doc.SVGFace.ViewObject.Visibility = False
    doc.recompute()

# Demo use:
# extrudeSVG(u"/path/to/file/design.svg", 4)
