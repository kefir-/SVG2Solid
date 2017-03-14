from FreeCAD import Base
import importSVG
import Part

def extrudeSVG(filename, thickness):

    doc = App.ActiveDocument

    objcnt = len(doc.Objects)

    # Import SVG
    importSVG.insert(filename, doc.Name) # returns None
    Gui.SendMsgToActiveView("ViewFit")
    # Get latest object in document:
    for i in range(objcnt, len(doc.Objects)):
        SVG = doc.Objects[i]
        if 'Shape' not in dir(SVG):
            print "Skipping object {0}, it has no Shape".format(SVG.Name)
            continue
        if SVG.Shape.ShapeType not in ('Wire', 'Edge'):
            print "Skipping shape {0} of type {1}".format(SVG.Name, SVG.Shape.ShapeType)
            continue
        # Gui.ActiveDocument.activeObject()
        # Gui.ActiveDocument.path3400
        # All objects: App.ActiveDocument.Objects[0] etc

        # Try to create face, hide SVG
        try:
            tmp = Part.Face(Part.Wire(Part.__sortEdges__(SVG.Shape.Edges)))
            if tmp.isNull(): raise RuntimeError('Failed to create face')

            SVGFace = doc.addObject('Part::Feature', 'SVGFace')
            SVGFace.Shape = tmp
            del tmp
        except Exception:
            print "Can't create face from part:", SVG.Name
        finally:
            SVG.ViewObject.Visibility=False

        # Extrude face
        SVGExtrude = doc.addObject("Part::Extrusion", "SVGExtrude")
        SVGExtrude.Base = SVGFace
        SVGExtrude.Dir = (0, 0, thickness)
        SVGExtrude.Solid = (True)
        SVGExtrude.TaperAngle = (0)
        SVGFace.ViewObject.Visibility = False
    doc.recompute()

# Demo use:
# extrudeSVG(u"/path/to/file/design.svg", 4)
